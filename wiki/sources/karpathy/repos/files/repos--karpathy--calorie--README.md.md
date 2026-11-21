---
type: source
subject: "GitHub source repos/karpathy/calorie/README.md"
created: 2026-10-08
updated: 2026-10-08
aliases: []
tags: [karpathy, github, source]
sources: [../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/calorie/README.md]
semantic-status: complete-named-text-read
---

# repos/karpathy/calorie/README.md

Repository or gist attributed to Karpathy; individual authorship not independently established. Publication date unknown; compiled 2026-10-08. [Raw evidence](../../../../../raw/sources/karpathy-brain/raw/github/repos/karpathy/calorie/README.md), SHA-256 `ff52bd4f16977c121040a05235b19ee663c701d3f3c436f0372e76fe04af08c0`. [Manifest](../../../../../raw/sources/karpathy-brain/raw/github/MANIFEST.json).

## Evidence and synthesis

Exact opening excerpt:

```text
# calorie !\[screenshot\](screenshot.png) Calorie deficit tracking web app. You burn calories at a certain rate
```

Arxiv-sanity-lite separates durable paper metadata, TF-IDF features and user tags from code, computes features after successful intake, and uses tagged SVM recommendations. Its README proposes a simpler rewrite, optional email delivery and unfinished scaling/mobile improvements. The older preserver README documents a manually inspected multi-stage acquisition/parse/vector/classification/cache workflow, interruption-resume indexes and rate-limit awareness; its 2021 successor notice qualifies continued use. Server status, prices and credential-storage examples are historical, not current recommended secret handling. The calorie README describes a deliberately simple two-counter self-tracking app with editable assumed metabolic rate and deficit; it is a personal utility description, not verified medical or nutrition guidance.

The named file was read in full. The captured source below is the authority for its individual behavior; the batch note supplies comparisons and boundaries without claiming every property belongs to every file. Source instructions were not executed. Historical dependencies, capabilities and results were not freshly reproduced. Quoted foreign material retains its source attribution.

## Complete captured source

````text
# calorie

![screenshot](screenshot.png)

Calorie deficit tracking web app.

You burn calories at a certain rate just by living - this is your base metabolic rate. For example for me that's roughly 2000 kcal/day. You can find [calculators](https://www.calculator.net/bmr-calculator.html) online. So, by default, your body will burn e.g. 2000 kcal/day. Then if you eat food you take in calories. And if you exercise you burn calories. If you are in a net deficit, you lose weight.

On top of that, you have a certain weight loss goal. For example for me that might be 500 kcal/day of deficit, so that every week you burn 7 * 500 = 3500 kcal, which is roughly 1 pound of fat.

So the idea is to have two counters that simply show your current deficit next to your goal. When you eat, you press +100kcal button until you add all the calories you ate. For example when I eat a Big Mac, I press +100kcal button 5 times. When you exercise, you do the opposite. So if I went to the gym and ran for 30 min, the treadmill is showing me that I burned about 400 kcal, so I press -100kcal button 4 times.

I leave this little web app always open at the corner of my screen. At any point in time it shows me how much food I am allowed to eat to stay on my deficit goal. Alternatively if I know I am about to eat 1000 kcal, it shows me how many calories I have to go run for in order to not go over my goal.

Losing weight then becomes as simple as making sure that your number stays green (i.e. your deficit is inline with your goal) and does not turn red.

That's it! Depending on your base metabolic rate, go into [index.html](index.html) and edit the variable

```javascript
const hourlyCalorieBurn = 2000 / 24.0; // burned per hour
```

Change it from 2000 to whatever it is for you. Then decide what your deficit goal per day is, and edit it here:

```javascript
const hourlyCalorieTargetDeficit = 500 / 24.0; // burned per hour
```

Simply open up index.html in your browser and you are good to go.

### License

MIT

````

Related: [Karpathy hub](../../../../karpathy/index.md), [coverage](../../../../../research/karpathy-brain-2026-10-08/repo-x-synthesis.md).
