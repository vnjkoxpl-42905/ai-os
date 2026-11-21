import json
from pathlib import Path
repo = Path('C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-confirmed-fixes-20261025')
p = repo/'src/features/activity-centre/content/spot-the-relationship.json'
bank = json.loads(p.read_text(encoding='utf-8'))
items = {i['order']: i for i in bank['items']}
items[7]['prompt'] = "Salt spray corroded the bolts at the base of the bridge."
items[7]['answer_key']['relationships'][0]['connects'] = "salt spray -> corrosion of the bolts at the base of the bridge"
items[7]['answer_key']['relationships'][0]['why'] = "'Corroded' identifies salt spray as producing damage to the bolts."
items[7]['answer_key']['traps'] = ["Missing the causal verb 'corroded'", "Treating the bolts' location as a relationship"]
items[26]['prompt'] = "Because the sluice was left open, the meadow flooded."
items[26]['answer_key']['relationships'][0]['connects'] = "the sluice being left open -> flooding of the meadow"
items[26]['answer_key']['relationships'][0]['why'] = "'Because' identifies the open sluice as the cause of flooding."
items[26]['answer_key']['traps'] = ["Missing the cause introduced by 'because'", "Treating the flooding as causing the open sluice"]
items[15]['prompt'] = "A stable emulsion requires added lecithin."
explanations = {
3: "1 relationship in this sentence. *Whenever* says the readings shift each time the gauge is recalibrated. Recalibration is enough for the stated shift, just as it would be if the sentence began with *if*. The sentence does not claim that recalibration causes the shift.",
7: "1 relationship in this sentence. *Corroded* says salt spray damaged the bolts. The verb itself expresses the cause; a word such as *because* is not needed. *At the base of the bridge* tells us where the bolts are.",
12: "1 relationship in this sentence. *As strong as* compares the oak beam with the steel channel in strength. The sentence says they are equal in strength, so neither support has to be stronger for this to be a comparison.",
14: "1 relationship in this sentence. *Raises* says closing the damper brings the kiln to cone 10. The previous sentence describes the same kiln and damper, but makes a different claim: closing the damper is required. This sentence says the closing causes the rise.",
15: "1 relationship in this sentence. *Requires* makes added lecithin necessary for a stable emulsion. It does not say that adding lecithin guarantees stability or causes it.",
18: "1 relationship in this sentence. *Secured* says the county's matching pledge brought the grant about. The previous sentence makes the pledge a requirement for the grant. This sentence gives it a causal role.",
21: "1 relationship in this sentence. *Unless* makes a conservator's signed report necessary for cataloguing. Without the signature, the manuscript is not catalogued. A signature alone does not guarantee that it will be catalogued.",
23: "1 relationship in this sentence. *More extensive than* compares the extent of the archive's holdings with the university library's. It says the archive's holdings are more extensive, without claiming what caused that difference.",
24: "1 relationship in this sentence. *Better than* compares how well peat soils and sandy soils hold water. The sentence gives peat soils the advantage; it does not explain what causes that advantage.",
26: "1 relationship in this sentence. *Because* identifies the open sluice as the cause of the meadow flooding. Here it explains what made an event happen. In an argument, *because* can instead introduce evidence for a conclusion, so read the whole sentence before deciding.",
38: "3 relationships in this sentence. *Only where* makes a canopy denser than sixty percent a requirement for seedling survival. *Denser than* compares the canopy with that numerical benchmark. *Because* and *dries* explain the cause: direct sun dries the litter layer. A canopy above sixty percent alone does not guarantee survival.",
45: "3 relationships in this sentence. *Provided* gives a sufficient condition for a null result to be meaningful: the assay's detection limit is finer than the regulatory threshold. *Finer than* compares the detection limit with that threshold. *Since* and *produces* give the reason: a coarse assay produces nulls that tell us nothing. The sentence does not say this detection limit is necessary for a meaningful result.",
}
for order, text in explanations.items():
    items[order]['explanation'] = text
items[41]['answer_key']['relationships'][2]['connects'] = "water following the gradient -> the explanation for the stated osmolality requirement for concentration"
items[41]['answer_key']['relationships'][2]['why'] = "'Because' uses water following the gradient to explain the osmolality requirement. The word 'follows' alone describes water movement; it does not express that explanatory link."
items[42]['answer_key']['relationships'][2]['connects'] = "spurious matches increasing at short series lengths -> the explanation for the coefficient threshold required for acceptance"
items[42]['answer_key']['relationships'][2]['why'] = "'Since' uses the increase in spurious matches at short lengths to explain the acceptance requirement. 'Inflate' alone describes an increase without expressing that explanatory link."
rubric = bank['instructions']['coach']['grading_rubric']
rubric.insert(2, "A quotation must identify the supporting word or phrase for its type. Repeating the whole sentence, or repeating the same span containing several types under every label, does not identify which words support each type. Mark that work partial when the types are right, and ask for a separate focused quotation for each. Do not require the shortest possible quotation: a wider clause is valid if it makes the supporting words clear.")
bank['instructions']['task'] = "Give each relationship type and quote the word or phrase that tells you the type. One quotation per type is enough."
p.write_text(json.dumps(bank, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
print('Updated 12 explanations, three prompts, paired key fields and the quotation rubric; all 48 orders preserved.')
