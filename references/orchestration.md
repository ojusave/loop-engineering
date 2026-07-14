# Orchestration and Handoffs

## Contents

- [Parent and specialists](#parent-and-specialists)
- [Routing questions](#routing-questions)
- [Default compositions](#default-compositions)
- [Parallelization](#parallelization)
- [Handoff contract](#handoff-contract)
- [Return states](#return-states)
- [Conflict resolution](#conflict-resolution)
- [Integration review](#integration-review)
- [Avoid circular handoffs](#avoid-circular-handoffs)


## Parent and specialists

Use one parent orchestrator per user assignment.

The parent owns:

- the final outcome
- the outcome contract, required evidence state, and target measure
- shared assumptions
- routing
- sequencing
- budget
- integration
- escalation
- terminal state

A specialist owns one class of failure and returns a receipt.

Specialists inherit the parent outcome contract. They may define local checks, but they must not silently redefine the assignment's target, threshold, intended context, or required evidence state.

Do not create a peer-to-peer swarm. A specialist may identify the need for another specialist, but it must return that request to the parent.

## Routing questions

Default compositions below are examples, not compulsory checklists. Derive the smallest composition from the current failure modes, then revise it if fresh evidence reveals a new risk or proves a specialist unnecessary.


Route by asking:

1. What baseline-to-target change, decision, or capability is required?
2. What evidence state must the assignment reach?
3. What artifact or intervention may produce that result?
4. What failure would be easy to miss if only the artifact were checked?
5. What evidence can verify the artifact and validate the outcome?
6. Which specialist can collect that evidence?
7. Which checks must happen before implementation, after implementation, or both?
8. Does success depend on an audience delta that must be established before wording or visual polish?

## Default compositions

### Product feature with UI

1. Freshness and portability, when new technology is considered
2. Product UX before implementation
3. Engineering implementation
4. Engineering verification
5. Rendered UI review
6. Accessibility review
7. Portability review, when architecture changed
8. Parent integration and primary-flow rerun

### Backend-only change

1. Engineering
2. Security or migration review when relevant
3. Parent integration

Do not invoke UI loops for truly non-user-facing work.

### Research-backed article

1. Adaptive evidence plan
2. Research and source-incentive audit
3. Audience-value and knowledge-advantage check when the article must earn attention
4. Article argument and drafting
5. Editorial anti-slop review
6. Fact, citation, and source-independence verification
7. Parent integration

### Conference talk or public abstract

1. Inventory the speaker's evidence, access, demonstration, findings, and disclosure limits
2. Establish the commodity baseline and audience delta
3. Shape the argument or talk contract
4. Draft the title and description
5. Editorial anti-slop review
6. Verify that every promised advantage is supported and will appear in the talk
7. Parent integration

### Strategy recommendation

1. Research when external facts matter
2. Strategy
3. Feasibility and counterargument review
4. Parent integration

### Downstream prompt

1. Task analysis
2. Prompt generation
3. Downstream simulation
4. Domain specialist review for any code, UI, research, or writing behavior carried by the prompt
5. Parent integration

## Parallelization

Parallelize only when subtasks are genuinely independent and their outputs have a clear integration contract.

Good candidates:

- research into separate factual questions
- independent security and accessibility review
- evaluation of two genuinely different architecture options

Poor candidates:

- two agents editing the same component without coordination
- UX and implementation proceeding before a shared experience contract
- several writers producing sections that require one consistent argument

## Handoff contract

Every handoff must contain:

```text
FROM:
TO:
OBJECTIVE:
ARTIFACT:
CURRENT VERSION OR PATH:
PARENT OUTCOME AND TARGET MEASURE:
BASELINE AND REQUIRED EVIDENCE STATE:
VERIFIED FACTS:
EVIDENCE OR COMMANDS:
KNOWN WEAKNESSES:
CONSTRAINTS AND NON-GOALS:
MAY CHANGE:
MUST PRESERVE:
TARGET ACCEPTANCE CRITERIA:
EXPECTED CONTRIBUTION AND PREDICTED OBSERVATION:
ACTUAL OBSERVATION AND MEASURED DELTA:
EVIDENCE STATE:
RETURN STATE:
```

Use `scripts/create_handoff.py` when project files are available.

## Return states

Specialists return one of:

- `PASS`: specialist acceptance passed
- `REWORK_REQUIRED`: concrete failures remain and another pass is justified
- `BLOCKED`: required evidence or environment is unavailable
- `NEEDS_HUMAN_JUDGMENT`: the remaining decision is subjective or consequential

They also report one evidence state: `NO RELIABLE EVIDENCE`, `ARTIFACT VERIFIED`, `OUTCOME VALIDATED`, or `DECISION READY`. The parent decides whether that local evidence advances the assignment's contracted target.

Specialist `PASS` does not imply assignment `COMPLETE`.

## Conflict resolution

When specialists conflict:

1. Identify which overall acceptance criterion is affected.
2. Prefer evidence tied to the user's primary outcome.
3. Preserve non-negotiable safety and accessibility requirements.
4. Test the disputed behavior with a real scenario when possible.
5. Escalate when the tradeoff is product taste, cost, risk, or authority.

Do not average incompatible recommendations.

## Integration review

The parent must verify the assembled result, not merely collect specialist passes.

Check:

- terminology and assumptions align
- implementation matches the experience contract
- backend failures are visible and recoverable in the interface
- accessibility changes preserve intended interaction
- framework choices match repository constraints
- article claims match research and source incentives are disclosed or appropriately discounted
- public arguments preserve the supported audience delta and do not replace it with biography, hype, or generic takeaways
- editorial changes preserve factual meaning
- generated prompts carry all required domain checks
- the integrated artifact is remeasured against the parent baseline, target, threshold, guardrails, and required evidence state

After integration changes, rerun the primary end-to-end scenario and remeasure the parent outcome. If only artifact checks are possible, report `ARTIFACT VERIFIED` and preserve the validation gap.

## Avoid circular handoffs

Never allow:

```text
engineering -> ux -> engineering -> accessibility -> ux -> engineering -> ...
```

Instead:

```text
specialist -> parent -> prioritized rework -> specialist verification -> parent
```

The parent records each cycle, measures improvement, and stops on stagnation.
