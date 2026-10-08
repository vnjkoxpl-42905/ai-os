from prop import *
it='PT144-S2-Q22: the Evaluate diagrams lost their negations'
P(it,'PT144-S2-Q22','6c503547-8ab5-4452-aaa5-d5de30ff6ac7',
 [("is a sufficient (left side) indicators.","is a sufficient (left side) indicator."),
  ("  - provides legal protection → serves purpose\n","  - no legal protection → serves no purpose\n"),
  ("  - email suggests something illegal → provides legal protection","  - email suggests something illegal → no legal protection")],
 'transcription','The diagrams lost their negations: the contrapositive must read "no legal protection → serves no purpose" and the third sentence "suggests something illegal → no legal protection"; as printed they reversed the argument. Also fixes "indicators" to "indicator".',
 'Stimulus: "The only purpose this disclaimer could serve is to provide legal protection for the company. But if the e-mail elsewhere suggests that the client do something illegal, then the disclaimer offers no legal protection."')
for rid,L in (('90f2a52e-cf6f-4182-8e90-6e1edbb25a67','D'),('cf779811-c5d6-466c-9b6c-39db840fe19c','E')):
    P('Overbroad guessing rule found while fixing PT144-S2-Q22','PT144-S2-Q22',rid,
     [("we would always avoid guessing a weakly worded answer","we would generally avoid guessing a weakly worded answer")],'register',
     'Softens an overbroad "always" rule about guessing to a tendency, keeping the teaching point.','Brief: overbroad rules stated as fact should be softened.')
