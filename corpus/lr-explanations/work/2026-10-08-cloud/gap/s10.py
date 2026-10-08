from prop import *
it='PT115-S2-Q21: the A note ends mid-sentence ("Most skilled artists are")'
P(it,'PT115-S2-Q21','330df05a-d14b-42ff-bba0-1520fa0e293f',
 [("Most skilled artists are Very Creative + Very Creative → Good at abstract reasoning ----------------------------------------------------------- Most skilled artists are Good at abstract reasoning",
   "```\nMost skilled artists are Very Creative\n+ Very Creative → Good at abstract reasoning\n---------------------------------------------\nMost skilled artists are Good at abstract reasoning\n```"),
  ("There's no way this recipe of claims: Most skilled artists are good at abstract reasoning Most skilled artists are",
   "There's no way this recipe of claims:\n\n```\nMost skilled artists are good at abstract reasoning\nMost skilled artists are very creative\nAll very creative people are good at abstract reasoning\nSome skilled artists are not famous\n```\n\ncould let us derive that \"some people good at abstract reasoning are famous\", because none of those claims tells us anything about famous people.")],
 'transcription','The note was cut off mid-sentence and its derivation was flattened onto one line; the rebuild lists the claims A plus the evidence give us and finishes the sentence the same way the B and D notes do.',
 'Stimulus: "The majority of skilled artists are very creative people, and all people who are very creative are also good at abstract reasoning. However, not all skilled artists are famous."; choice A: "Most skilled artists are good at abstract reasoning."')
P('Flattened claim list found while fixing PT115-S2-Q21','PT115-S2-Q21','adc64626-714f-4f75-a711-bb276360e921',
 [("to work with: Most very-creative are skilled artists Most skilled artists are very-creative All very-creative are good at abstract reasoning Some skilled artists are not famous",
   "to work with:\n\n```\nMost very-creative are skilled artists\nMost skilled artists are very-creative\nAll very-creative are good at abstract reasoning\nSome skilled artists are not famous\n```")],
 'transcription','The list of claims was run together on one line; each claim now sits on its own line, words unchanged.','Choice B: "Most people who are very creative are skilled artists."')
P('Flattened claim list found while fixing PT115-S2-Q21','PT115-S2-Q21','5b0d556f-4ea0-47ce-a00a-93e3b9feb0c8',
 [("to work with: All good at abstract reasoning are very-creative All very-creative are good at abstract reasoning Most skilled artists are very-creative Some skilled artists are not famous",
   "to work with:\n\n```\nAll good at abstract reasoning are very-creative\nAll very-creative are good at abstract reasoning\nMost skilled artists are very-creative\nSome skilled artists are not famous\n```")],
 'transcription','The list of claims was run together on one line; each claim now sits on its own line, words unchanged.','Choice D: "All people who are good at abstract reasoning are very creative."')
P('Flattened diagrams found while fixing PT115-S2-Q21','PT115-S2-Q21','3c70ec26-be6c-4c60-94f9-5f5bef5108ac',
 [("Most skilled artists are Very Creative + Very Creative → Good at Abstract Reasoning ------------------------------------------------------------ Most SA's are Good at Abstract Reasoning",
   "```\nMost skilled artists are Very Creative\n+ Very Creative → Good at Abstract Reasoning\n---------------------------------------------\nMost SA's are Good at Abstract Reasoning\n```"),
  ("Most A's are B + Most A's are C -------------------------- Some B's are C (Some C's are B)",
   "```\nMost A's are B\n+ Most A's are C\n---------------\nSome B's are C (Some C's are B)\n```")],
 'transcription','Both derivations were flattened onto single lines; each premise and the result now sit on their own lines, words unchanged.','Choice E: "Most skilled artists are famous."')
P('Typo found while fixing PT115-S2-Q21','PT115-S2-Q21','f42af413-2a7b-479e-bb22-a7a0d080d3be',[("people who are very create are","people who are very creative are")],'slip',
 '"very create" is a typo for "very creative".','Stimulus: "all people who are very creative are also good at abstract reasoning"')
P('Flattened translation list found while fixing PT115-S2-Q21','PT115-S2-Q21','ecf4ac2a-3de1-4b5b-9a0f-edf619bce0db',
 [("**Negative to Positive** translation: No A's are B = All A's are ~B Few A's are B = Most A's are ~B Not all A's are B = Some A's are ~B",
   "**Negative to Positive** translation:\n  No A's are B = All A's are ~B\n  Few A's are B = Most A's are ~B\n  Not all A's are B = Some A's are ~B")],
 'transcription','The three translations were run together on one line; each now sits on its own line, words unchanged.','Stimulus: "not all skilled artists are famous"')
