---
type: source
subject: "GitHub source repos/karpathy/arxiv-sanity-preserver/twitter_daemon.py"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/twitter_daemon.py]
semantic-status: complete-named-text-read
---

# repos/karpathy/arxiv-sanity-preserver/twitter_daemon.py

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/arxiv-sanity-preserver/twitter_daemon.py), SHA-256 `916082305c707ded2342b7ce13cf6a68cff8359feb8b739191f5eac6b6c60daa`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt: "\"\"\" Periodically checks Twitter for tweets about arxiv papers we recognize and logs the tweets".

The main template combines infinite scrolling with an explicit Load more fallback and time/version filters. Its hosting-cost prompt is optional and dismissible. Thumbnail extraction uses an inelegant intermediate-file approach because it was observed to succeed more often, limits a stuck converter to 20 seconds and substitutes a missing-image marker. Twitter daemon deduplicates IDs, filters recognized papers and banned accounts, explicitly labels popularity as hype, and favors meaningful commentary while capping displayed records. Its old authenticated API and unlimited retry loop were not executed or assumed usable now. Popularity weighting and fallback markers are operational heuristics, not correctness or completeness evidence.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

```text
"""
Periodically checks Twitter for tweets about arxiv papers we recognize
and logs the tweets into mongodb database "arxiv", under "tweets" collection.
"""

import os
import re
import pytz
import time
import math
import pickle
import datetime

from dateutil import parser
import twitter # pip install python-twitter
import pymongo

from utils import Config

# settings
# -----------------------------------------------------------------------------
sleep_time = 60*10 # in seconds, between twitter API calls. Default rate limit is 180 per 15 minutes
max_tweet_records = 15

# convenience functions
# -----------------------------------------------------------------------------
def get_keys():
  lines = open('twitter.txt', 'r').read().splitlines()
  return lines

def extract_arxiv_pids(r):
  pids = []
  for u in r.urls:
    m = re.search('arxiv.org/abs/(.+)', u.expanded_url)
    if m: 
      rawid = m.group(1)
      pids.append(rawid)
  return pids

def get_latest_or_loop(q):
  results = None
  while results is None:
    try:
      results = api.GetSearch(raw_query="q=%s&result_type=recent&count=100" % (q, ))
    except Exception as e:
      print('there was some problem (waiting some time and trying again):')
      print(e)
      time.sleep(sleep_time)
  return results

epochd = datetime.datetime(1970,1,1,tzinfo=pytz.utc) # time of epoch

def tprepro(tweet_text):
  # take tweet, return set of words
  t = tweet_text.lower()
  t = re.sub(r'[^\w\s]','',t) # remove punctuation
  ws = set([w for w in t.split() if not w.startswith('#')])
  return ws

# -----------------------------------------------------------------------------

# authenticate to twitter API
keys = get_keys()
api = twitter.Api(consumer_key=keys[0],
                  consumer_secret=keys[1],
                  access_token_key=keys[2],
                  access_token_secret=keys[3])

# connect to mongodb instance
client = pymongo.MongoClient()
mdb = client.arxiv
tweets = mdb.tweets # the "tweets" collection in "arxiv" database
tweets_top1 = mdb.tweets_top1
tweets_top7 = mdb.tweets_top7
tweets_top30 = mdb.tweets_top30
print('mongodb tweets collection size:', tweets.count())
print('mongodb tweets_top1 collection size:', tweets_top1.count())
print('mongodb tweets_top7 collection size:', tweets_top7.count())
print('mongodb tweets_top30 collection size:', tweets_top30.count())

# load banned accounts
banned = {}
if os.path.isfile(Config.banned_path):
  with open(Config.banned_path, 'r') as f:
    lines = f.read().split('\n')
  for l in lines:
    if l: banned[l] = 1 # mark banned
  print('banning users:', list(banned.keys()))

# main loop
last_db_load = None
while True:

  dnow_utc = datetime.datetime.now(datetime.timezone.utc)

  # fetch all database arxiv pids that we know about (and handle an upadte of the db file)
  if last_db_load is None or os.stat(Config.db_path).st_mtime > last_db_load:
    last_db_load = time.time()
    print('(re-) loading the paper database', Config.db_path)
    db = pickle.load(open(Config.db_path, 'rb'))

  # fetch the latest mentioning arxiv.org
  results = get_latest_or_loop('arxiv.org')
  to_insert = []
  for r in results:
    arxiv_pids = extract_arxiv_pids(r)
    arxiv_pids = [p for p in arxiv_pids if p in db] # filter to those that are in our paper db
    if not arxiv_pids: continue # nothing we know about here, lets move on
    if tweets.find_one({'id':r.id}): continue # we already have this item
    if r.user.screen_name in banned: continue # banned user, very likely a bot

    # create the tweet. intentionally making it flat here without user nesting
    d = parser.parse(r.created_at) # datetime instance
    tweet = {}
    tweet['id'] = r.id
    tweet['pids'] = arxiv_pids # arxiv paper ids mentioned in this tweet
    tweet['inserted_at_date'] = dnow_utc
    tweet['created_at_date'] = d
    tweet['created_at_time'] = (d - epochd).total_seconds() # seconds since epoch
    tweet['lang'] = r.lang
    tweet['text'] = r.text
    tweet['user_screen_name'] = r.user.screen_name
    tweet['user_image_url'] = r.user.profile_image_url
    tweet['user_followers_count'] = r.user.followers_count
    tweet['user_following_count'] = r.user.friends_count
    to_insert.append(tweet)

  if to_insert: tweets.insert_many(to_insert)
  print('processed %d/%d new tweets. Currently maintaining total %d' % (len(to_insert), len(results), tweets.count()))

  # run over 1,7,30 days
  pid_to_words_cache = {}
  for days in [1,7,30]:
    tweets_top = {1:tweets_top1, 7:tweets_top7, 30:tweets_top30}[days]

    # precompute: compile together all votes over last 5 days
    dminus = dnow_utc - datetime.timedelta(days=days)
    relevant = tweets.find({'created_at_date': {'$gt': dminus}})
    raw_votes, votes, records_dict = {}, {}, {}
    for tweet in relevant:
      # some tweets are really boring, like an RT
      tweet_words = tprepro(tweet['text'])
      isok = not(tweet['text'].startswith('RT') or tweet['lang'] != 'en' or len(tweet['text']) < 40)

      # give people with more followers more vote, as it's seen by more people and contributes to more hype
      float_vote = min(math.log10(tweet['user_followers_count'] + 1), 4.0)/2.0
      for pid in tweet['pids']:
        if not pid in records_dict: 
          records_dict[pid] = {'pid':pid, 'tweets':[], 'vote': 0.0, 'raw_vote': 0} # create a new entry for this pid
        
        # good tweets make a comment, not just a boring RT, or exactly the post title. Detect these.
        if pid in pid_to_words_cache:
          title_words = pid_to_words_cache[pid]
        else:
          title_words = tprepro(db[pid]['title'])
          pid_to_words_cache[pid] = title_words
        comment_words = tweet_words - title_words # how much does the tweet have other than just the actual title of the article?
        isok2 = int(isok and len(comment_words) >= 3)

        # add up the votes for papers
        tweet_sort_bonus = 10000 if isok2 else 0 # lets bring meaningful comments up front.
        records_dict[pid]['tweets'].append({'screen_name':tweet['user_screen_name'], 'image_url':tweet['user_image_url'], 'text':tweet['text'], 'weight':float_vote + tweet_sort_bonus, 'ok':isok2, 'id':str(tweet['id']) })
        votes[pid] = votes.get(pid, 0.0) + float_vote
        raw_votes[pid] = raw_votes.get(pid, 0) + 1

    # record the total amount of vote/raw_vote for each pid
    for pid in votes:
      records_dict[pid]['vote'] = votes[pid] # record the total amount of vote across relevant tweets
      records_dict[pid]['raw_vote'] = raw_votes[pid] 

    # crop the tweets to only some number of highest weight ones (for efficiency)
    for pid, d in records_dict.items():
      d['num_tweets'] = len(d['tweets']) # back this up before we crop
      d['tweets'].sort(reverse=True, key=lambda x: x['weight'])
      if len(d['tweets']) > max_tweet_records: d['tweets'] = d['tweets'][:max_tweet_records]

    # some debugging information
    votes = [(v,k) for k,v in votes.items()]
    votes.sort(reverse=True, key=lambda x: x[0]) # sort descending by votes
    print('top votes:', votes[:min(len(votes), 10)])

    # write the results to mongodb
    if records_dict:
      tweets_top.delete_many({}) # clear the whole tweets_top collection
      tweets_top.insert_many(list(records_dict.values())) # insert all precomputed records (minimal tweets) with their votes

  # and sleep for a while
  print('sleeping', sleep_time)
  time.sleep(sleep_time)

```

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
