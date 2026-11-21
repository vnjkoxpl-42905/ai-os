# Opening source rewrite for review

Drafted 2026-10-02. Applied to the four owned units after the coordinating agent authorized implementation under Joshua's build request. Claude plan round 2 returned REVISE; the host accepted the warranted corrections. Final actual Claude inspection is still required.

Read in full: `references/lsat-teaching-voice-standard.md`. Also read the project-owned `.agents/skills/lsat-u-voice/SKILL.md`, `wiki/teaching-voice.md`, and `wiki/COPY-CORRECTIONS.md`.

The first two units keep the same original ready/packed rule. They move from definition and purpose to a fact, an unsupported reverse, the two roles, and a useful diagram. Group 1 and Group 2 then explain each core expression individually. The What Test, complete ideas, clear labels, placement, Personalized If/Then and English readback stay visible. The newly authored opening teaches no contraposition, combining rules, Groups 3/4 or quantities. Historical questions remain outside new practice. The optional wording extensions are removed following the actual Claude scope review. The fourteen core expressions remain developed individually.

The 62 practice prompts, option text and order, answer keys, and level membership remain as captured in `visual-proof/voice-application/curriculum-before.json`. Feedback is rewritten below. The four guided prompts and their options also remain. All units after Group 2 remain byte-for-byte authored content.

Three earlier replacements reused IDs whose HEAD originals have a different meaning. Actual inspection also retires group-2-a1 because its original assessed a later operation; its current replacement is group-2-a1-v2, a direct-direction translation preserving the full emergency appointment and permission. Rename the current replacements to `group-1-a3-v2`, `group-2-m2-v2`, and `group-2-a3-v2`. Keep the exact four originals from `visual-proof/voice-application/historical-questions-v2.json` in a historical-only lookup; the earlier three-row proof is preserved. New practice never receives those originals. This preserves old numeric choices and saved diagrams under the questions they actually answered.

The proposed data below is organized by authored fields so application can be narrow and mechanically checked. Unit IDs and titles stay as they are. The feedback arrays contain a hint followed by the reasoning steps; the existing source helper derives `explanation` from those steps. Each explanation gives the reason beside the answer.

```json
{
  "units": {
    "orientation": {
      "goal": "Explain what a conditional says, use it with a fact, and say what the information leaves open.",
      "teaching": [
        "A conditional tells us that if one condition is true, another has to be true too. A condition is something we can say about a situation, such as an order being marked ready or its having been packed. The conditional connects those two ideas. It doesn't tell us that either one has happened.",
        "Why learn this? A conclusion on the LSAT can depend on which way that connection runs. If you know what the rule promises, you can explain why a conclusion follows. If an answer uses the rule in the other direction, you can see the missing connection instead of accepting a conclusion that sounds reasonable.",
        "Let's use one rule: Every order marked ready has been packed. Take that claim as true for this exercise. Every ready order has to be packed. Orders marked ready are usually packed would say something weaker, because usually leaves room for an exception. Our rule doesn't.",
        "Now we get a fact: Order A is marked ready. What do you know about A? Take a moment to explain your answer before reading on. A has been packed. The rule covers every order marked ready, and the fact puts A in that group. A ready order that hadn't been packed would break the rule.",
        "Keep the rule and change the fact: Order B has been packed. Must B be marked ready? Try to explain why before reading on. We don't know. The rule told us about ready orders. It didn't say every packed order is marked ready. B could be marked ready or packed without being marked ready. Either possibility fits what we've been told.",
        "We can now shorten the relationship to Marked ready → Packed. Read that as: if an order is marked ready, it has been packed. The arrow records the connection we've already understood. It doesn't add a cause, a time sequence, or a fact about a particular order.",
        "In the practice, separate the rule from the fact about the case. Then ask what that fact lets you conclude. Write the reason as well as the answer. That gives you something specific to compare with the explanation if your choice goes wrong."
      ],
      "method": [
        "Read the rule in ordinary English: what does it say has to be true if the first condition is true?",
        "Check the strength. Every ready order is packed gives a guarantee; usually packed allows an exception.",
        "Find the separate fact about the case. A rule alone doesn't identify a ready order.",
        "Compare the whole fact with the condition the rule covers. Order A is marked ready meets our ready-order condition.",
        "State what follows and why. If the information leaves a question open, show how both possibilities could fit."
      ],
      "workedExample": {
        "statements": [
          "Every order marked ready has been packed.",
          "Order A is marked ready."
        ],
        "reasoning": [
          "The rule tells us that every ready order has been packed. The fact identifies A as one of those orders.",
          "So A has been packed. We haven't assumed anything about a different order or about what made A ready."
        ],
        "conclusion": "Order A has been packed."
      },
      "commonMistake": {
        "mistake": "Reading a rule as though it tells us a particular case has occurred.",
        "repair": "Every ready order is packed tells you what must be true of a ready order. It hasn't named one. Look for a separate fact before making a conclusion about a particular order."
      }
    },
    "sufficient-necessary": {
      "goal": "Explain sufficient as enough and necessary as required, then check which cases fit the same rule.",
      "teaching": [
        "Return to our rule: Every order marked ready has been packed. If you know an order is marked ready, that's enough to know it has been packed. You don't need another fact about that order. Being marked ready is the sufficient condition. Sufficient means enough, here enough to establish packing under this rule.",
        "Packed is the necessary condition. Necessary means required. A ready order has to have been packed, because an unpacked ready order would be an exception to our rule. So the same relationship has two sides: marked ready is enough to establish packed, and packed is required for marked ready.",
        "Does required mean enough? Suppose an order is packed. Must it be marked ready? We still don't know. Packing meets a requirement for ready status, but the rule hasn't said it settles that status. An order that's packed but not marked ready would fit the rule.",
        "Now suppose an order isn't marked ready. Does that settle whether it's packed? No. Our rule tells us what ready orders must have. An order without that label could be packed or unpacked. We haven't been given a fact that decides between them.",
        "Compare all four combinations under this one rule. Ready and packed fits. Not ready and packed fits too. Not ready and not packed also fits. Ready and not packed breaks the guarantee. A case fitting the rule means it is possible under that rule, not that the rule tells us it occurred.",
        "The names belong to this relationship. Packed is necessary for ready status here. In a different rule, such as every packed order has a tracking number, packed would be sufficient for that tracking number. Ask enough for what, or required for what, rather than giving an idea one permanent label.",
        "When a sentence feels unclear, try a Personalized If/Then. Read it naturally first. Then imagine you meet the condition you think is sufficient. What does the sentence force you to know? Check that thought against the whole sentence, not just against a feeling that the arrow looks right.",
        "A recovery code is required for a verified account. If my account is verified, what must it have? A recovery code. Now try the other direction: if I have a recovery code, must my account be verified? The sentence hasn't promised that. This check helps us hear why the requirement belongs on the right."
      ],
      "method": [
        "Read the whole sentence in ordinary English before deciding which condition is enough.",
        "Ask enough for what. Name both ideas completely: marked ready is enough to establish packed under our rule.",
        "Ask required for what. Packed is required for marked ready; that doesn't make packed enough to establish ready status.",
        "Check your interpretation with a Personalized If/Then. Try the proposed starting condition, then compare the reverse with the original sentence.",
        "Test a possible case against the actual guarantee. Keep a case that fits separate from a case the information establishes."
      ],
      "workedExample": {
        "statements": [
          "Every order marked ready has been packed.",
          "Order C has been packed but is not marked ready."
        ],
        "reasoning": [
          "Packing is required for ready status. The rule hasn't promised ready status for every packed order.",
          "C can therefore be packed without a ready label. That case fits the rule; it doesn't supply a reverse rule."
        ],
        "conclusion": "Packed without marked ready fits this rule."
      },
      "commonMistake": {
        "mistake": "Taking a required condition as enough to establish the other condition.",
        "repair": "Try the reverse in English: if an order is packed, it must be marked ready. Did the sentence promise that? It didn't. Keep the requirement, but don't add that guarantee."
      }
    },
    "group-1": {
      "goal": "Find the complete sufficient idea in each Group 1 expression and preserve its meaning in a diagram.",
      "teaching": [
        "We've understood enough and required. Now let's see how different words express the sufficient side. Group 1 includes if, when, where, all, the only, every and any in their conditional uses. The words help you find a relationship. You still need to read what the whole sentence says.",
        "Start with if: If an order is marked ready, it has been packed. If what? The order is marked ready. That's the sufficient idea. Now move the clause: An order has been packed if it is marked ready. The same idea still follows if, and the same guarantee runs from marked ready to packed. The first words on the page aren't always the left side of the diagram.",
        "When can introduce the event that's enough: When the alarm sounds, the staff evacuate. Ask when what. The alarm sounds. The sentence promises evacuation whenever the alarm sounds. Whenever makes the same repeated-case meaning explicit. But When I checked the desk, a notice was there reports one occasion; it doesn't promise a notice every time I check.",
        "Where can make a rule about a location or situation: Where a station is available, the service operates. Which locations does the rule cover? Locations with an available station. At one of those locations, the service has to operate. Keep the location connection when you read the rule back; a station elsewhere hasn't met this location's condition.",
        "All covers the whole group it names: All registered guests receive a wristband. All what? Registered guests, not guests generally. Being one of those registered guests is enough for a wristband. Another guest may receive one too; the sentence hasn't told us. It also hasn't told us that a registered guest exists.",
        "The only needs careful reading: The only vehicles permitted inside are electric vehicles. The only what? Vehicles permitted inside. If a vehicle is permitted inside, it must be electric. Try electric vehicle → permitted inside. That would grant permission to every electric vehicle, which the sentence never promised. The grammatical target is the whole permission description, not the word electric.",
        "Every takes the members one at a time but covers them all: Every finalist receives an invitation. Choose a finalist. The sentence promises that person an invitation. All finalists receive an invitation would express the same relationship. Neither wording says everyone receiving an invitation is a finalist.",
        "Any says that whichever member of the named group you choose, the rule applies: Any applicant who submits late pays a fee. A late-submitting applicant pays a fee. That's what the sentence guarantees. Choose an applicant who submits on time and this sentence doesn't settle the fee question. Submits late stays with applicant in your diagram.",
        "The What Test keeps you with the complete idea: if what, when what, where what, all what, the only what, every what, or any what? Don't stop at the nearest noun. In A report appears when a rover crosses the ridge, the target is the rover crossing the ridge. That event goes left, even though the sentence begins with the report.",
        "An indicator can have another job. The curator asked if the painting was insured tells us about a question the curator asked. It gives no guarantee between asking and insurance. Read for a conditional meaning before drawing an arrow.",
        "To build the diagram, name both complete ideas and give them clear condensed labels. Place the sufficient idea on the left and what it guarantees on the right. Then read the arrow as an if/then. Does that sentence say the same thing as the original? If a label lost a restriction or the arrow added a reverse, repair it before moving on.",
        "For Recall and Rephrase, put the list aside and try a fresh sentence. Write its if/then meaning, then compare with the original. The point is to keep the relationship when the wording changes, not merely to remember which side a word usually points toward."
      ],
      "method": [
        "Read the sentence for a guarantee, then identify the Group 1 expression. Use the What Test to find the whole idea it refers to.",
        "Name both complete ideas. Keep who or what they concern, as well as restrictions such as registered or submits late.",
        "Choose clear condensed labels for those ideas. A shorter label must still mean the same thing.",
        "Place the sufficient idea left and what it guarantees right. Sentence order doesn't decide the arrow's direction.",
        "Read the diagram as an if/then and compare it with the original. Check the direction and every restriction you kept in the labels."
      ],
      "workedExample": {
        "statements": [
          "Any parcel collected from the north depot receives a receipt."
        ],
        "reasoning": [
          "Any what? A parcel collected from the north depot. Collection from that depot is part of the sufficient idea, so parcel alone would be too broad.",
          "The rule promises a receipt for that same parcel. Read it back: if a parcel is collected from the north depot, it receives a receipt."
        ],
        "conclusion": "Parcel collected from north depot → receives receipt."
      },
      "commonMistake": {
        "mistake": "Putting the first idea left or dropping a restriction from the sufficient idea.",
        "repair": "Ask what the expression refers to, then read your arrow in English. A report appears when a rover crosses the ridge starts with the report, but the crossing is what guarantees it. Keep the whole crossing condition on the left."
      }
    },
    "group-2": {
      "goal": "Find what a Group 2 sentence requires, preserve its complete meaning, and distinguish a requirement from success or compliance.",
      "teaching": [
        "Group 2 helps us find the necessary side: what the sentence says is required. Its core expressions are only, only if, only when, only where, always, requires and must in their relevant uses. We'll keep the complete requirement on the right. First, let's hear why it belongs there.",
        "Compare if with only if. An order is marked ready if it has been packed makes packing enough for ready status. An order is marked ready only if it has been packed says packing is required for ready status. Those aren't the same rule. In the second sentence, an order could be packed without being marked ready. The sentence permits that possibility.",
        "Only restricts who or what can have the other condition: Only packed orders are marked ready. If an order is marked ready, it must be packed. Only what? Packed orders. Compare The only orders marked ready are packed orders. That Group 1 form reaches the same ready → packed relationship, but its target is orders marked ready. Read the phrase with its grammar rather than treating only and the only as interchangeable labels.",
        "Only if introduces a condition that has to be met: A student graduates only if the student completes the project. If the student graduates, the project must be completed. Project completion by itself doesn't promise graduation. Read the reverse aloud and you'll hear the extra guarantee it adds.",
        "Only when makes an event or state required: A review occurs only when a complaint is filed. A complaint has to be filed for this review to occur. Imagine a complaint has been filed. Does this sentence say a review now occurs? No. It says what a review requires, not that every complaint gets one.",
        "Only where makes a location condition required: The service operates only where a station is available. Wherever the service operates, a station has to be available there. A station at another location isn't enough. Nor has the sentence promised service to every place with an available station.",
        "Always describes the result that holds throughout the named cases: A finalist always receives an invitation. Start with a finalist. Under that claim, the person receives an invitation. The subject supplies the sufficient idea; receiving an invitation is the required result. Always belongs in this teaching group, but it doesn't mean the next word automatically goes on the right. Read the complete subject and result.",
        "Requires tells you what is needed: Entry requires a current pass. Requires what? A current pass. Entry goes left, having the current pass goes right. Change the wording to A current pass is required for entry. The requirement appears first now, but the relationship hasn't changed. A pass alone isn't a promise that you can enter, and an expired pass doesn't meet the full requirement.",
        "Must can state an obligation: A finalist must attend the interview. What does finalist status establish? The person is required to attend. It doesn't establish that the person actually attends; people can fail to meet an obligation. Write Finalist → Required to attend interview so the diagram preserves that difference. Keep permission words such as may in the same careful way.",
        "Use the What Test on the full expression, then check with a Personalized If/Then. If my display has activated, what does the battery rule force me to know? Its battery is charged. Now suppose I know only that the battery is charged. The rule still leaves activation open. That comparison checks the arrow against the sentence's ordinary meaning.",
        "Keep every part of a requirement. In Entry requires a current pass, pass would drop current. In Only members may use this room, actually uses the room would change permission into an action. The right direction can't repair a label that has lost part of the idea.",
        "In the fresh practice, explain what is required and what remains open. If your answer treats a requirement as enough, try saying that answer as an if/then. Compare it with the original sentence and point to the extra promise. That's the mistake we're learning to catch."
      ],
      "method": [
        "Read the whole conditional claim. Identify the Group 2 expression and ask what it requires or restricts with the What Test.",
        "Name both complete ideas. Keep restrictions, negatives, permission and obligation in their meaning.",
        "Choose clear condensed labels. Required to attend must not become actually attends.",
        "Place the restricted event or condition left and its requirement right. Check that direction with a Personalized If/Then.",
        "Read the arrow back in English. Compare the reverse too: did the original sentence really make the requirement enough?"
      ],
      "workedExample": {
        "statements": [
          "A package is released only when its clearance is recorded."
        ],
        "reasoning": [
          "Only when what? Its clearance is recorded. A released package has to meet that requirement, so release goes left and recorded clearance goes right.",
          "Read it back: if a package is released, its clearance is recorded. Recorded clearance alone doesn't promise release; the sentence hasn't given us that direction."
        ],
        "conclusion": "Package released → its clearance recorded."
      },
      "commonMistake": {
        "mistake": "Taking a requirement as a guarantee of the result, or taking an obligation as proof that someone complied.",
        "repair": "Ask exactly what was promised. Having a current pass meets the requirement for entry, but it doesn't establish that someone entered. Must attend establishes required attendance, not actual attendance. Keep that distinction in the diagram and conclusion."
      }
    }
  },
  "questionFeedback": {
    "orientation-guide": [
      "Card L is activated. Which part of the rule does that fact meet?",
      [
        "The rule covers activated cards, and L is one of them.",
        "So L's number is registered. It doesn't give a reverse rule about every registered number or exclude other registered cards."
      ]
    ],
    "orientation-b1": [
      "Which sentence promises one condition whenever the other is true?",
      [
        "If the desk is staffed, the bell is answered gives a guarantee from staffing to answering.",
        "Staffed now reports one fact. Usually answered allows an exception. Neither gives that same connection."
      ]
    ],
    "orientation-b2": [
      "What kind of crate does the rule promise a label for? Find a fact putting M in that group.",
      [
        "The rule promises a label for every numbered crate.",
        "Crate M is numbered puts M in that group. Heavy doesn't do that, and might be numbered leaves it unsettled."
      ]
    ],
    "orientation-b3": [
      "Look for a claim about one named book rather than a rule or tendency.",
      [
        "Book 4 has a new binding tells us something about that particular book.",
        "All restored books gives a general rule. Generally look newer describes a tendency. Neither reports this single binding fact."
      ]
    ],
    "orientation-m1": [
      "Could Lift 2 be an inspected lift that doesn't operate quietly without contradicting most?",
      [
        "Yes. Most inspected lifts can operate quietly while another inspected lift is noisy.",
        "We know Lift 2 was inspected, but we don't know which kind it is. Quiet operation is possible, not guaranteed."
      ]
    ],
    "orientation-m2": [
      "The fact gives you the support frame. What did the rule actually promise about framed roofs?",
      [
        "It promised a frame for a roof with a solar panel. It didn't promise a panel for every roof with a frame.",
        "This roof could have a panel or have a frame for another reason. Neither panel status follows from the information."
      ]
    ],
    "orientation-m3": [
      "Does every sealed sample is logged tell you that a sealed sample exists?",
      [
        "The rule tells us what must be true of any sealed sample: it is logged.",
        "It hasn't identified a sealed sample or any other logged sample. The relationship remains true while existence remains unknown."
      ]
    ],
    "orientation-a1": [
      "Keep may request in your conclusion. Is permission the same as making or receiving a request?",
      [
        "Imani is an authorized visitor, so the rule gives Imani permission to request a copy.",
        "It doesn't say Imani uses that permission or receives a copy. May request is the conclusion the wording supports."
      ]
    ],
    "orientation-a2": [
      "Does certified for indoor use meet certified for underwater use?",
      [
        "No. The rule promises a sealed housing for sensors certified for underwater use.",
        "Indoor certification doesn't establish that condition. K could have a sealed housing or lack one without contradicting what we've been told."
      ]
    ],
    "orientation-a3": [
      "The light flashes. What response does the instruction require, and what action has actually been reported?",
      [
        "The flashing light meets the condition for the shutdown instruction.",
        "The instruction therefore calls for shutdown. It doesn't report that anyone followed it or that the machine has already shut down."
      ]
    ],
    "sufficient-necessary-guide": [
      "If my account is verified, what does the rule require it to have? Compare the three cases with that promise.",
      [
        "The rule requires a recovery code for every verified account.",
        "Verified without a code breaks that guarantee. A verified account with one fits, and an unverified account with one doesn't break any promise the rule made."
      ]
    ],
    "sufficient-necessary-b1": [
      "If the cabinet is fire-rated, what do you know about its shell?",
      [
        "The rule makes fire-rated status enough to establish a steel shell.",
        "Having a steel shell is the promised result. The sentence hasn't identified that result or absence of fire-rating as its sufficient starting condition."
      ]
    ],
    "sufficient-necessary-b2": [
      "Imagine an accredited course. What does the rule say it has to have?",
      [
        "It has to have an assessment. An accredited course without one would break the rule.",
        "So an assessment is necessary for accreditation. The rule hasn't made every assessed course accredited."
      ]
    ],
    "sufficient-necessary-b3": [
      "Which case avoids a packaged tube without a cap?",
      [
        "A tube that isn't packaged can have a cap without breaking the rule. The sentence only promises caps for packaged tubes.",
        "Both uncapped packaged cases break that promise. Being small doesn't excuse the missing cap."
      ]
    ],
    "sufficient-necessary-m1": [
      "Read the two arrows separately. What role does reflective have in each relationship?",
      [
        "In polished → reflective, reflective is what polishing requires. It is necessary in that rule.",
        "In reflective → visible, reflective is enough to establish visible. It is sufficient there. The role changes with the relationship."
      ]
    ],
    "sufficient-necessary-m2": [
      "Could a specimen be stored without being tagged and still fit the sentence?",
      [
        "Yes. Tagged specimens must be stored, but the sentence doesn't restrict storage to tagged specimens.",
        "F could be tagged or untagged. Storage alone doesn't settle which, so tagged status is unknown."
      ]
    ],
    "sufficient-necessary-m3": [
      "What promise would an upgraded seat without extra legroom break? Does this case have an upgraded seat?",
      [
        "The guarantee applies to upgraded seats. This seat isn't upgraded, so its lack of extra legroom doesn't break that promise.",
        "The case is allowed. The rule by itself wouldn't tell us this case occurred; that is a separate claim in the question."
      ]
    ],
    "sufficient-necessary-a1": [
      "Which exact acceptance does the rule connect to having a faculty sponsor?",
      [
        "A paper accepted for the student symposium has to have a faculty sponsor.",
        "Acceptance for a different conference, or simply being a paper, doesn't meet that full sufficient idea."
      ]
    ],
    "sufficient-necessary-a2": [
      "Would a valid token without authentication break a promise about authenticated tokens?",
      [
        "No. The rule promises validity for authenticated tokens; it hasn't said every valid token is authenticated.",
        "A valid unauthenticated token therefore fits the relationship. It doesn't make authentication necessary for validity."
      ]
    ],
    "sufficient-necessary-a3": [
      "Name the requirement for a priority packet, then ask whether the sentence identifies one.",
      [
        "A priority packet has to be routed through Server C, so that routing is necessary for priority status.",
        "The rule hasn't identified a priority packet. It establishes a requirement, not the existence of a packet meeting it or the reverse direction."
      ]
    ],
    "group-1-guide": [
      "When what? A rover crosses the ridge. Does that event come first or second in the original sentence?",
      [
        "Crossing the ridge is enough for the checkpoint report, even though that event appears second in the sentence.",
        "Read the diagram: if a rover crosses the ridge, a checkpoint report appears. The sentence hasn't promised a crossing for every report or no report whenever a rover doesn't cross."
      ]
    ],
    "group-1-b1": [
      "If what? A locker is reserved. Begin the arrow with that whole idea.",
      [
        "The rule promises a nameplate for a reserved locker, so Reserved locker → displays nameplate preserves it.",
        "The sentence hasn't said a nameplate proves reservation or that every unreserved locker lacks one. Those alternatives add promises."
      ]
    ],
    "group-1-b2": [
      "Take one woven basket. What does every tell you must be true of it?",
      [
        "This basket is one of the woven baskets the rule covers, so it has a reinforced rim.",
        "Other baskets might have reinforced rims too. The rule doesn't make this the only rimmed basket or make every rimmed basket woven."
      ]
    ],
    "group-1-b3": [
      "Whenever what? Find the event after whenever, even though printing is mentioned first.",
      [
        "Whenever the schedule changes, the rule promises a printed notice.",
        "Printing is the result. A schedule that stays unchanged hasn't met the sufficient idea named by whenever."
      ]
    ],
    "group-1-b4": [
      "Where what? Keep the blue label with the shelf.",
      [
        "The rule covers a shelf with a blue label. That whole condition goes left.",
        "At such a shelf, its books are available to borrow. Any shelf would drop the restriction, and availability belongs on the result side."
      ]
    ],
    "group-1-b5": [
      "Which cups does all cover? Keep packed in the gift set in your answer.",
      [
        "A cup packed in that gift set has to have a matching saucer, so the full gift-set condition goes left.",
        "Cup → matching saucer would cover cups outside the set too. Matching saucer → gift-set cup would reverse a promise the sentence never made."
      ]
    ],
    "group-1-b6": [
      "The only what? Start with desserts on the lunch menu.",
      [
        "Every dessert on that menu has to be chilled. Being on the menu is enough for that conclusion.",
        "The sentence doesn't put every chilled dessert on the menu. It could be chilled without appearing there and still fit the rule."
      ]
    ],
    "group-1-b7": [
      "Any what? Read past ticket to the words limiting which tickets are covered.",
      [
        "The sentence covers a ticket bought online. That is the complete sufficient idea.",
        "Ticket alone would make the same promise about other purchase methods. Receipt included names the result rather than the sufficient idea."
      ]
    ],
    "group-1-m1": [
      "What does submitted through the portal add to invoice?",
      [
        "The rule promises a time stamp for an invoice submitted through the portal. Keep that full description on the left.",
        "It hasn't covered every invoice or said a time stamp proves portal submission. The broader and reversed arrows each add something."
      ]
    ],
    "group-1-m2": [
      "The only what? Which rehearsals does the sentence tell you about first?",
      [
        "Recorded rehearsals have to be rehearsals held in Studio B. Read the arrow as: if a rehearsal is recorded, it was held there.",
        "Being in Studio B alone doesn't promise recording. The sentence restricts the recorded group without promising that every Studio B rehearsal joins it."
      ]
    ],
    "group-1-m3": [
      "The flag is raised. Has the sentence said ice detection is the only way that can happen?",
      [
        "No. Ice detection guarantees the raised flag, but the sentence doesn't give the reverse guarantee.",
        "A station could have detected ice or raised its flag for another reason. The fact leaves ice detection unknown."
      ]
    ],
    "group-1-m4": [
      "If what? Its lid is sealed. Does mentioning the sticker first change that?",
      [
        "It doesn't. The sealed lid is enough for the green sticker even though the if clause comes second.",
        "Sealed lid → green sticker says the same thing. The reverse and the claim about no tray aren't supplied by the sentence."
      ]
    ],
    "group-1-m5": [
      "Could the lights be dimmed while the rehearsal continues without breaking the rule?",
      [
        "Yes. When the rehearsal ends, the lights have to be dimmed. The sentence doesn't say dim lights prove the rehearsal has ended.",
        "Dim lights leave the rehearsal's ending open. We can't conclude either that it ended or that it didn't."
      ]
    ],
    "group-1-m6": [
      "Which mugs does the rule promise handles for? Compare each case with that group.",
      [
        "A lower-shelf mug with a handle fits. The rule doesn't restrict handles to the top shelf.",
        "A top-shelf mug without a handle breaks the guarantee, whether the mug is small or not."
      ]
    ],
    "group-1-m7": [
      "Every which guest? What words disappear from the shorter arrow?",
      [
        "The rule covers guests arriving before six. The shorter arrow loses before six.",
        "That would promise a seat number to any guest, including guests whose arrival time the sentence doesn't cover. Keep the restriction with the sufficient idea."
      ]
    ],
    "group-1-a1": [
      "Compare selected for the indoor series with selected for the outdoor series. Are they the same full idea?",
      [
        "No. The captioning guarantee covers films selected for the outdoor series.",
        "Indoor selection alone doesn't meet that condition. V could be captioned or not; this rule doesn't settle it."
      ]
    ],
    "group-1-a2": [
      "Is the curator making a guarantee, or asking a question about the painting?",
      [
        "Asked if reports an inquiry about insurance. It doesn't state that asking guarantees insurance or that insurance guarantees asking.",
        "So neither arrow follows. The familiar word if has a different job in this sentence."
      ]
    ],
    "group-1-a3": [
      "Keep both limits: certified for which exposure, and stored in which place?",
      [
        "Certification for heat exposure is the sufficient idea. Storage in the outdoor cabinet is the result promised for that component.",
        "The matching arrow keeps both descriptions. Outdoors generally, certified for every use, and component alone each change or lose part of the meaning."
      ]
    ],
    "group-1-a4": [
      "Does when describe every check, or the particular check being reported?",
      [
        "It describes one visit when the shutters were closed.",
        "That observation doesn't promise closed shutters whenever I check, or a check whenever the shutters close. No conditional rule has been stated."
      ]
    ],
    "group-1-a5": [
      "Keep evening service in the reservation condition. Does a lunch reservation meet it?",
      [
        "No. The rule promises a lit lamp for a table reserved for evening service.",
        "A lunch reservation alone doesn't meet that complete condition. Its unlit lamp therefore doesn't contradict the stated evening-service guarantee."
      ]
    ],
    "group-1-a6": [
      "All which notebooks? Keep sold in the travel kit with the sufficient idea.",
      [
        "If a notebook is sold in the travel kit, it has a waterproof cover. That is the relationship the sentence gives.",
        "A waterproof cover doesn't prove the sale context, and notebook alone would cover notebooks outside the kit. Neither change is justified."
      ]
    ],
    "group-1-a7": [
      "Try the sentence from same-day feedback to online. Did it also promise feedback for every online workshop?",
      [
        "It didn't. A workshop offering same-day feedback has to be online.",
        "An online workshop without that feedback fits. The sentence requires online format for same-day feedback; it doesn't say every online workshop offers that feedback."
      ]
    ],
    "group-1-a8": [
      "If what? The order includes a collection time. Keep includes a collection time, not just order.",
      [
        "An order including a collection time is enough for the confirmation. The sufficient idea comes second in the sentence but still goes left.",
        "Order placed would lose the time restriction. A confirmation doesn't prove that time was included, because the sentence hasn't given that reverse guarantee."
      ]
    ],
    "group-1-a9": [
      "When what? Does a green marker by itself establish the nut-free reservation?",
      [
        "The rule gives a green marker to every tray set aside for nut-free orders.",
        "The sentence doesn't restrict green markers to those trays. Q could be set aside that way or have the marker without that reservation; we don't know which."
      ]
    ],
    "group-2-guide": [
      "If I can access the recording, what does only subscribers require about me?",
      [
        "Access permission is restricted to subscribers, so someone who can access the recording has to be a subscriber.",
        "The sentence doesn't say every subscriber can access the recording. Nor does permission tell us someone actually accessed it."
      ]
    ],
    "group-2-b1": [
      "Only if what? If the display has activated, what must be true of its battery?",
      [
        "Its battery must be charged. Display activates → battery charged preserves that requirement.",
        "The sentence doesn't promise activation from charging or an uncharged battery from an inactive display. Both alternatives add a direction we weren't given."
      ]
    ],
    "group-2-b2": [
      "Only what? Which people can receive a parking sticker under this restriction?",
      [
        "Recipients have to be residents. Being a resident is therefore necessary for receiving the sticker.",
        "The rule hasn't promised a sticker to every resident or made daily driving a requirement. Having a sticker is the result we're asking about."
      ]
    ],
    "group-2-b3": [
      "Start with the full subject: a registered buoy. What does always say about it?",
      [
        "A registered buoy broadcasts its identifier in every case covered by the claim.",
        "So Registered buoy → broadcasts identifier preserves the rule. The claim doesn't say every broadcasting buoy is registered or that an unregistered buoy stays silent."
      ]
    ],
    "group-2-b4": [
      "Only when what? What has to be true of the kitchen if breakfast is being served?",
      [
        "The kitchen has to be open, so that complete idea goes on the required side.",
        "The kitchen could be open without serving breakfast. Serves breakfast goes left, and café alone isn't the requirement."
      ]
    ],
    "group-2-b5": [
      "If the service runs at a location, what does only where require there?",
      [
        "Road access has to be available at that location. Service runs → road access keeps the location requirement.",
        "Road access alone doesn't tell us the service runs there. No service wouldn't prove there's no road. Keep the direction the sentence actually gives."
      ]
    ],
    "group-2-b6": [
      "Requires what? Name the form completely.",
      [
        "Someone borrowing the camera needs a signed form. That is the necessary idea.",
        "Signing the form doesn't settle whether you borrow the camera. Borrowing is the restricted activity; buying a camera isn't discussed."
      ]
    ],
    "group-2-b7": [
      "Does must report attendance, or say attendance is required?",
      [
        "Captain status gives the captain an obligation to attend the briefing.",
        "It doesn't report that the captain complied. Nor does it say only captains attend. Required to attend is what follows."
      ]
    ],
    "group-2-m1": [
      "Mira meets the score requirement. Did the sentence make that score enough for entry?",
      [
        "No. Entry requires a qualifying score, so that score is necessary.",
        "The rule doesn't say it is the only requirement or promise entry from it. Mira's entry remains open rather than established or ruled out."
      ]
    ],
    "group-2-m2": [
      "Only when what? Read the arrow as a statement about what recording requires.",
      [
        "If the camera records, motion is detected. That puts recording left and the required detection right.",
        "Motion could be detected while the camera records nothing. The sentence also says nothing about the camera being broken."
      ]
    ],
    "group-2-m3": [
      "The beacon operates at P. What does the location restriction require at P?",
      [
        "Operation there requires satellite contact there, so contact is available at P.",
        "The rule doesn't promise operation at every contact site or say P is the only site with contact. Those claims go beyond this case."
      ]
    ],
    "group-2-m4": [
      "Only what? Keep paid in advance with the orders that may be shipped today.",
      [
        "Today's shipped orders have to be orders paid in advance. Prepayment is necessary for being shipped today.",
        "The sentence doesn't discuss shipments at every time or promise today's shipment from prepayment. Order alone would lose the requirement."
      ]
    ],
    "group-2-m5": [
      "Try the reverse aloud: every guest with a day pass gets a locker. Was that promised?",
      [
        "It wasn't. The pass is required for a locker, but the rule doesn't promise a locker to every passholder.",
        "This guest could receive a locker or not. The pass meets the named requirement without deciding allocation."
      ]
    ],
    "group-2-m6": [
      "Always carries a stamp applies to which exact prints?",
      [
        "It applies to prints from this edition. That full subject goes left, and the date stamp is the promised result.",
        "Print alone would cover other editions. A stamped print could come from another edition, so the reverse arrow adds something we weren't given."
      ]
    ],
    "group-2-m7": [
      "The rule requires renters to return a key. Does it restrict all key returns to renters?",
      [
        "No. It gives renters an obligation, but doesn't say every person returning a key is a renter.",
        "Dana's return could therefore be made by a renter or someone else. The action doesn't prove renter status or tell us what every renter did."
      ]
    ],
    "group-2-a2": [
      "Rowan holds the permit. What obligation does must submit give Rowan?",
      [
        "The policy covers Rowan and requires Rowan to submit a signed safety declaration.",
        "It doesn't report actual submission. Nor does submission guarantee a permit. Preserve the obligation instead of turning it into completed compliance."
      ]
    ],
    "group-2-a3": [
      "Keep both parts of the requirement: by which deadline, through which channel?",
      [
        "An eligible claim has to be filed by the deadline through the official portal. The matching arrow preserves both limits on the right.",
        "Timely filing alone and portal submission alone each omit part of that requirement. Neither has been made enough to establish eligibility."
      ]
    ],
    "group-2-a4": [
      "Only when what? Keep the damaged item, its return, and its receipt in one complete idea.",
      [
        "A sent replacement requires a damaged item returned with its receipt. That full requirement goes right.",
        "An item returned alone or a receipt alone doesn't preserve the requirement, and neither has been made enough to guarantee a replacement."
      ]
    ],
    "group-2-a5": [
      "What does shaded add to seating? Does the fact tell us whether R meets that part?",
      [
        "A screening requires a shaded seating area. Seats alone don't establish shade.",
        "We haven't been told shade is absent either. So the facts don't settle whether the requirement is met, much less whether a screening happens."
      ]
    ],
    "group-2-a6": [
      "The item has a number. Did always restrict collection numbers to the express queue?",
      [
        "It didn't. An express-queue item has to be assigned a collection number, but another queue could use them too.",
        "This number therefore doesn't settle the item's queue. It proves neither express status nor its absence."
      ]
    ],
    "group-2-a7": [
      "What is required? Find that idea even though it appears before required.",
      [
        "The waterproof case is required for this camera's underwater use. Read the relationship: if this camera is used underwater, it has that case.",
        "Having the case doesn't tell us the camera is used underwater, and the sentence doesn't require a case for every camera use. Keep underwater in the left-hand idea."
      ]
    ],
    "group-2-a1-v2": [
      "Only which reviewers? Keep emergency-panel appointment in the required idea, and may inspect as permission.",
      [
        "Only reviewers appointed for this emergency panel have permission to inspect these records. Permission therefore goes left; that complete reviewer appointment goes right.",
        "An appointment to just any panel isn't the requirement we were given, and the sentence doesn't promise inspection permission from an appointment.",
        "It also says may inspect, not has inspected. Permission doesn't establish that anyone used it."
      ]
    ]
  }
}
```

## Checks before application is complete

1. Hash the baseline's compact practice identity projection per opening unit: level membership, ordered ID, prompt, ordered options and answer key. Compare the same current projection after normalizing only the three approved replacement IDs. This preserves the real answer contract without copying a large curriculum fixture.
2. Assert the opening has 62 practice items and the three original IDs never enter a new practice set. Verify the historical-only lookup returns each exact historical question, including its old prompt, options, key, hint and explanation.
3. Keep core indicator coverage at each level. Check must feedback for obligation, not asserted compliance.
4. Check the four unit IDs, opening order and prerequisites, no source example borrowing, and no later operations in the new teaching or methods. Existing medium practice compares sufficient/necessary roles in two separate arrows; it asks for no combined inference.
5. Leave generation to the coordinating agent once both authoring workers finish. Run the existing content, assignment, route and persistence checks, then typecheck/build and inspect the actual lesson/reference/practice surfaces.

The draft does not claim voice identity is objectively measurable. It applies the reference's definition, thought process, cadence, purposeful questions and boundaries to original course material. Claude's actual review and Joshua's response remain the calibration.

## Actual inspection 1 corrections, 2026-10-02

OR-1: My feedback rewrite used performance where the preserved prompt says rehearsal. The hint and every reasoning sentence now keep rehearsal. OR-7: The reference repair now uses the taught current-pass/entry example. OR-6: The old group-2-a1 is available only for saved work; its new -v2 question directly asks for the complete appointment requirement and permission. Other 61 prompts, option order, keys and levels remain unchanged.

OR-9: Before this voice rewrite, group-2-b3 changed Every registered buoy always broadcasts its identifier to A registered buoy always broadcasts its identifier. Always preserves the universal claim about registered buoys. Options and answer index 1 are unchanged, so this cosmetic wording needs no retired question. This is documented alongside the earlier cosmetic obligation wording in group-2-a2.

Portable practice fingerprint (62 approved current questions): 2cc25820135dd0c10ccfcd629a68758d4d924a9a3a3545df857dfbca1fc0f534. Preserved 61-question fingerprint: e4f9a1577a66ac70ca1e0fc26b6b96b6bb561e8160c00bf052517c3a4417a5f9. Four exact historical objects: 0d0ff240d9b0597515efb0b02f50f62e1af234cb1d12027d419f37ea5e76a6aa.

## Actual inspection 2 source cleanup, 2026-10-02

FI-5: All current opening ready-label waiting descriptions now describe an order that is packed but not marked ready. No later labeling or timeline is implied. FI-7: Repeated passive phrasing in the four units and their feedback now names the specific unsupported promise. Necessary qualifications remain where they clarify a supplied rule. No prompt, option, numeric key, ID, level membership or historical row changed. What Test and Personalized If/Then stay named; the renderer worker now teaches both. Current62, preserved61 and historical4 fingerprints remain exactly as recorded above.
