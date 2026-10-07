"""Classify an LR question stem into the app's 18 canonical types.

Order matters: narrower and structural types first. Returns None when no rule
fires, which sends the row to manual review instead of guessing.

Taxonomy calls (follow the app's TYPE_SYNONYMS where it has an opinion):
- "best illustrates / conforms to which proposition/generalization",
  "principle violated", "principle above supports which judgment"
  -> Principle-Conform (synonyms: Principle Illustrated, Principle-Identify,
  Inconsistent with Principle, Principle Application).
- answer choices are principles that justify the passage, or "justifies the
  application of the principle/policy" -> Principle-Strengthen.
- misinterpretation / ambiguity stems -> Flaw.
- "X is (most strongly) supported if which is assumed" -> Strengthen;
  "follows logically / properly drawn / properly inferred if assumed" and
  "if assumed, (most helps to) justify" -> Sufficient Assumption.
- fill-in ("completes the passage") -> Most Strongly Supported unless the
  stem names another task.
"""
import re


def norm(s):
    s = (s or "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("�", "'").replace("­", "")
    return re.sub(r"\s+", " ", s.lower()).strip()


FLAWWORD = r"flaw|questionable|error|erroneous|vulnerable|faulty|dubious|fallac|mistake|susceptible to criticism|subject to criticism"


def stem_type(stem):
    s = norm(stem)
    if not s:
        return None

    # --- Misinterpretation / ambiguity: Flaw ---
    if re.search(r"misinterpret|misunderstood|misunderstand|interpreted [^?]* (to mean|to be|to imply|as)|interpreting [^?]* to be|trades on an ambiguity|ambiguity in", s):
        return "Flaw"

    # --- Parallel family ---
    if re.search(r"principle", s) and re.search(r"parallel|most similar|same principle|illustrates? the same|also illustrat|similar principle|(conforms?|conform) (most closely )?to the (same )?principle (illustrated|underlying|exemplified)", s):
        return "Principle-Conform"
    if re.search(r"parallel|most similar|similar (in|to)|most closely resembles|most like|pattern of reasoning|logical features|both of the (logical )?flaws|exhibits both", s) and not re.search(r"counterexample", s):
        if re.search(FLAWWORD, s):
            return "Parallel Flaw"
        return "Parallel Reasoning"

    # --- Role (structural, before everything that keys on content words) ---
    if re.search(r"\brole\b|figures in the|plays which one|function(s|ed)? (primarily )?(in|as)|the function of|serves? (which one of the following|to|as|in)|is offered (in|as)|is used (in|to)|relationship (between|of)|the point of [^?]* is to", s) and not re.search(r"proceeds by|technique|strategy", s):
        return "Role"

    # --- Agree/Disagree ---
    if re.search(r"disagree|point at issue|at issue between|in dispute|committed to (agreeing|accepting|disagreeing)|(both|each) of them would (agree|accept)|agree (with each other|about|that|on)|at odds|views differ|differ (over|about|on)|accepted by [^?]* but not by", s):
        return "Agree/Disagree"

    # --- Flaw via criticism of an application or the reasoning ---
    if re.search(r"vulnerable to|subject to criticism|susceptible to criticism|criticism of [^?]*reasoning|grounds for criticizing|basis for criticizing|objection to the reasoning|objections?\?|criticisms?\?|is flawed|fallacious|unwarranted because|error|mistake in|\bflaw|questionable reasoning|does not follow logically from its premises|exhibits which one of the following", s) and not re.search(r"assum", s):
        return "Flaw"

    # --- Method (stems that describe how an argument proceeds) ---
    if re.search(r"proceeds by|method|technique|strateg|argues by|by (doing )?which|does which one of the following|in which one of the following ways|derives its conclusion by|(responds|replies|counters?|challenges|criticizes|undermines|questions|attacks|calls into question)[^?]* by$|attempts? to [^?]* by$|by$|seeks to do|most accurately describes [^?]*(argument|response|reply|reasoning|study|comparison)\??$|is (most accurately|best) described as|descriptions best fits|comparisons is utilized|on the grounds that$|could have remained unchanged", s):
        return "Method of Reasoning"
    if re.search(r"analog(y|ous)|corresponds to", s):
        return "Method of Reasoning"

    # --- Principle family ---
    if re.search(r"(justif|support)\w* [^?]*(the )?(above |stated |given )?application of the (principle|policy|polic)", s):
        return "Principle-Strengthen"
    if re.search(r"which one of the following (university |company )?(principles|polic(y|ies))|principles? (that|which),? if|each of the following principles|is a principle that|principles?,? (if|would,? if) (valid|established|accepted)", s):
        if re.search(r"must be assumed|assumption", s):
            return "Necessary Assumption"
        if re.search(r"conform|illustrat|exemplif|violat|properly (be )?inferred", s):
            return "Principle-Conform" if not re.search(r"properly (be )?inferred", s) else "Must Be True"
        if re.search(r"disagree|committed", s):
            return "Agree/Disagree"
        return "Principle-Strengthen"
    if re.search(r"principle", s):
        if re.search(r"must be assumed|assumption", s):
            return "Necessary Assumption"
        if re.search(r"properly drawn using the principle", s):
            return "Principle-Strengthen"
        return "Principle-Conform"
    if re.search(r"conforms? (most closely )?to|most closely conforms|illustrat|exemplif|violates?|is an example of|appropriate for (which|each)|exhibit the most", s):
        return "Principle-Conform"

    # --- Weaken (before Paradox: "calls into question the explanation") ---
    if re.search(r"weaken|undermine|cast(s)? (the most |most )?(serious )?doubt|call(s)? into question|called into question|calls? (the )?\w+ into question|counters? the|counter to|most seriously (challenge|jeopardi|limits)|strongest (objection|challenge)|argues? (most strongly )?against|evidence against the|count as evidence against|reduce the support|alternative explanation|only a partial|at best incomplete|is misleading if|might not have the result|might be ineffective", s) and not re.search(r"strengthens the [^?]*counter|supports [^?]*counter", s):
        return "Weaken"

    # --- Assumptions ---
    if re.search(r"if (which one of the following|the following) is assumed|is assumed\?|if assumed|assumptions? enables|enables? the (argument'?s? )?conclusion|allows? the [^?]*conclusion to be properly|would (allow|enable)", s):
        if re.search(r"(is|are) (most )?(strongly )?supported if", s):
            return "Strengthen"
        return "Sufficient Assumption"
    if re.search(r"follows logically if|properly (drawn|inferred) if|logically follow if|would provide the proof", s):
        return "Sufficient Assumption"
    if re.search(r"assum|depends on|relies on|presuppos|is required by|would not follow if", s):
        return "Necessary Assumption"

    # --- Paradox ---
    if re.search(r"discrepancy|paradox|apparent (conflict|inconsistency)|seemingly (contradictory|conflicting)|apparently contradictory|reconcile|resolv|account for|accounts for|explain|explanation of|reason in favor of", s) and not \
       re.search(r"support[s]? the [^?]*explanation|support for the [^?]*explanation", s):
        return "Paradox"

    # --- Evaluate ---
    if re.search(r"evaluat|useful to (know|determine|establish)|helpful to (know|determine)|relevant to (assessing|determining|evaluating)|most important to know|least helpful in establishing|accurate assessment", s):
        return "Evaluate"

    # --- Main Conclusion ---
    if re.search(r"main (conclusion|point)|overall conclusion|expresses the (argument'?s )?conclusion|states the conclusion|conclusion (drawn in|of) the argument|structured to lead to|leads? to the conclusion|is arguing that|argues that$", s):
        return "Main Conclusion"

    # --- Must Be False ---
    if re.search(r"could (also )?be true,? except|cannot be true|must be false|inconsistent with|incompatible|conflicts? with|could not be true|least compatible|compatible with each of the following except|justifiably be rejected|basis for rejecting|reason for rejecting|strongest evidence against", s):
        return "Must Be False"

    # --- Strengthen ---
    pass_supports_answer = re.search(r"(statements?|information|passage|claims?|remarks?|facts?|considerations?|views?|reasoning|dialogue|conversation|exchange|above|results?|findings?)[^?]*(most strongly|best|most|strongly|reasonably|some)? ?support (for )?(which|each)|most strongly support (which|the statement|the claim that)|lend the strongest support to which|support (for )?(which one|each of the following)|supported by|evidence for which|grounds for accepting|used as part of an argument for", s)
    if not pass_supports_answer and re.search(r"strengthen|support|justif|bolster|defense of|argues most strongly for|additional evidence", s):
        return "Strengthen"

    # --- Must Be True vs Most Strongly Supported ---
    if re.search(r"must (also )?be true|would also have to be true|must also hold|can (properly |logically |validly )?be (properly |logically )?(inferred|concluded|deduced|drawn)|properly (be )?inferred|strictly implied|logically follows|follows logically from|must be the case|commit (him|her|them) to|can be concluded|must violate", s):
        return "Must Be True"
    if pass_supports_answer or re.search(r"most (strongly|reasonably|clearly|logically)? ?support|best support|complet(es|ion)|logically concludes|most reasonably (be )?(inferred|concluded)|most likely (to )?(also )?be true|serve least well as evidence", s):
        return "Most Strongly Supported"
    return None
