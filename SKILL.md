---
name: loop-engineering
description: run an adaptive, bounded, evidence-backed work system only when the user explicitly invokes it with phrases such as "loop:", "use loop", or "loop this task". derive task-specific checks, then route coding, product, ui, ux, accessibility, research, strategy, audience value, writing, and prompt-generation work through a parent orchestrator and specialist loops. preserve gitignored state, verify current observable evidence, audit marketing and seo/aeo/geo source incentives, prefer maintained open-source and portable solutions, reject generic ai-slop and polished-but-substitutable public writing, and stop or escalate cleanly. do not trigger for incidental uses such as for-loops or event loops.
---

# Loop Engineering

Perform the requested work through a bounded loop. Do not merely explain loop engineering, produce a ceremonial plan, or expose private reasoning.

Assume the receiving agent knows nothing about loop engineering. Use this skill as the operating system for the task.

## Activation

Activate only when the user deliberately invokes the skill, for example:

- `loop: fix the checkout flow`
- `use loop to research and write this article`
- `loop this task and create a reusable prompt`

Do not activate for incidental mentions of a programming loop, event loop, feedback loop, or quoted text.

When activated, perform the task now. Do not ask the user to repeat known context. Make reversible assumptions where safe. Ask only when a missing decision is consequential, irreversible, or impossible to infer responsibly.

## Read the relevant protocols

Always read:

- `references/foundations.md`
- `references/adaptive-task-design.md`
- `references/orchestration.md`
- `references/verification.md`

Then load only the specialist protocols needed for the task:

- Code, bugs, refactors, architecture: `references/engineering-loop.md`
- Product behavior, onboarding, flows, information architecture: `references/product-ux-loop.md`
- Rendered interface and visual design: `references/ui-visual-loop.md`
- Accessibility: `references/accessibility-loop.md`
- Frameworks, libraries, APIs, platform choices: `references/freshness-portability.md`
- Research and factual synthesis: `references/research-loop.md`
- Source incentives, SEO/AEO/GEO, marketing, affiliate, and PR bias: `references/source-integrity.md`
- Strategy, recommendations, prioritization: `references/strategy-loop.md`
- Conference abstracts, talks, public arguments, positioning, and other work that must earn attention: `references/audience-value-loop.md`
- Blogs, essays, manifestos, thought leadership: `references/article-loop.md`
- Final writing review and anti-slop editing: `references/editorial-loop.md`
- Prompts and reusable instructions for another model: `references/prompt-generation.md`
- Activation and routing examples: `references/examples.md`

## Adaptive, not set in stone

The protocols provide invariants, failure patterns, and candidate checks. They are not fixed forms that every task must complete.

For each invocation, derive from the actual request and current environment:

- the outcome owner, class, baseline, target state, intended context, primary measure, threshold, and guardrails
- the required evidence state and strongest feasible evidence now
- the next decision or use the result must enable
- the non-goals
- the likely failure classes
- the smallest useful specialist composition
- the evidence plan
- the commodity baseline and audience delta when attention or differentiation matters
- artifact acceptance criteria and outcome-validation scenarios
- the sequence and handoffs
- the loop depth and stop conditions

Treat default compositions and examples as starting hypotheses. Remove irrelevant checks. Add a specialist only when a material risk appears. Revise the loop design when fresh evidence changes what must be verified.

Do not confuse completing predefined boxes with proving the requested outcome.

## Parent orchestrator

Use one parent loop for the assignment. The parent owns:

- the user outcome and non-goals
- the outcome contract, target measure, guardrails, and required evidence state
- shared state and evidence
- task classification and specialist selection
- sequencing and parallelization
- handoffs and integration
- iteration, time, and scope budgets
- approval boundaries
- conflict resolution
- the final terminal state

Specialist loops own one class of failure. They may request another specialist through the parent, but they must not freely call one another or create an unbounded chain.

For multi-cycle work, initialize state with:

```bash
python <skill-directory>/scripts/init_loop_state.py --task "<concise task>" --mode deep
```

This must create project-local state under `.loop/` and ensure `.loop/` is in the repository root `.gitignore`.

Never store secrets, credentials, personal data, copied production data, or hidden chain-of-thought in `.loop/`.

Use the state file as a compact operational ledger containing:

- outcome contract and baseline
- required evidence state
- artifact-verification and outcome-validation evidence
- constraints and exclusions
- current facts and assumptions
- selected specialist loops and order
- artifacts and handoff receipts
- cycle hypotheses, predicted observations, actual observations, and measured deltas
- rejected directions
- unresolved risks
- next action
- terminal status

Use an in-memory light loop for a small task that can be completed and deterministically verified in one pass.

## Route by failure class

Do not route only by artifact type. Ask what can go wrong and which specialist can observe it.

Examples:

- A backend can pass tests while the product remains confusing: use engineering, product UX, rendered UI, and accessibility loops.
- A blog can be factual but generic: use research, article, editorial, and fact-check verification.
- A talk description can be vivid yet substitutable: use audience value before editorial polish.
- A framework can work but be stale or lock the project in: use freshness and portability before implementation.
- A prompt can sound complete but produce one-shot behavior: use prompt generation and downstream simulation.

For mixed tasks, compose specialists under the parent. Prefer the smallest set that covers the material risks.

## Handoffs

Every handoff must be an explicit artifact, not a vague chat summary. Use:

```bash
python <skill-directory>/scripts/create_handoff.py \
  --from-loop "<source>" \
  --to-loop "<target>" \
  --objective "<what the target must accomplish>" \
  --artifact "<path or artifact description>" \
  --state-dir "<.loop task directory>"
```

Complete the generated receipt with:

- the inherited parent outcome, target measure, and required evidence state
- verified facts
- evidence and commands
- known weaknesses
- constraints and non-goals
- what may change
- what must be preserved
- target acceptance criteria
- expected contribution and predicted observation
- actual observation and measured delta
- evidence state
- return state

Allowed specialist return states:

- `PASS`
- `REWORK_REQUIRED`
- `BLOCKED`
- `NEEDS_HUMAN_JUDGMENT`

The parent converts these into the assignment-level terminal state.

## Core cycle

Run this cycle without narrating hidden reasoning:

1. **Observe:** Measure the current state or establish the strongest available baseline.
2. **Hypothesize:** State the predicted observation and mechanism: `If we do X, Y should change because Z.`
3. **Choose:** Select the smallest bounded intervention that can reduce the target gap or resolve the highest-value uncertainty.
4. **Act:** Make one coherent, reversible change or collect one decisive piece of evidence.
5. **Measure:** Compare the actual observation with the prediction, baseline, target, and guardrails.
6. **Study:** Record the measured delta, contradicted or confirmed assumption, evidence state, and useful learning.
7. **Route, repeat, or stop:** Adopt, adapt, abandon, escalate, or stop. Continue only when another pass has a credible path to measurable progress or decision-relevant learning.

A failed intervention may be a successful cycle when it eliminates an important hypothesis. A new artifact with no measured delta and no useful learning is not progress.

Do not manufacture a loop when new feedback cannot change the next action. Use a one-pass workflow with verification instead.

## Self-correction and controlled improvement

Require self-correction within the assignment: observe failure, diagnose it, change the strategy, and verify again. Permit self-healing only for bounded operational recovery toward a known healthy invariant, with retry limits and escalation.

Do not let a loop redefine or weaken its own outcome, target, verifier, evidence requirement, guardrails, or authority boundaries to manufacture progress. Treat changes to the loop, prompt, rubric, or evaluation method as proposed meta-improvements. Adopt them only after representative before-and-after evaluation shows a real gain without guardrail regressions; require human approval when the change is consequential or persistent. The same model's approval is not sufficient evidence for its own rule change.

## Loop depth

Choose the smallest trustworthy depth.

### Light

Use for narrow, reversible changes with an obvious verifier.

- inspect
- change
- run the targeted check
- inspect the diff or output
- measure the target behavior or state the validation limit

### Standard

Use for normal features, bugs, UI changes, bounded research, or article revision.

- define the outcome contract and required evidence state first
- complete one coherent slice
- verify the artifact and validate the intended behavior with the strongest feasible evidence
- diagnose failures before revising
- use up to four meaningful cycles

### Deep

Use for cross-cutting product work, ambiguous architecture, migrations, major research, substantial writing, or multi-specialist tasks.

- map dependencies and risks
- define specialist sequence and handoffs
- use fresh-context or independent checking where available
- integrate, rerun the primary scenario, and remeasure the parent outcome
- use up to six meaningful parent cycles

Iteration numbers are ceilings, not goals. Stop earlier when evidence is sufficient. When the same direction fails twice, change the hypothesis instead of adding patches.

## Mandatory technology decision gate

Whenever work selects or introduces a framework, library, service, API, protocol, design system, database, build tool, or deployment pattern, read `references/freshness-portability.md` before implementation.

Default order of preference:

1. Existing repository convention that remains fit and maintained
2. Stable open standard or interoperable protocol
3. Maintained open-source library or framework
4. Thin adapter around provider-specific behavior
5. Small custom implementation only when the above options do not fit

Do not choose technology from model memory alone. Verify current official documentation, release/support status, repository or package health, license, compatibility, and migration surface. Absence of a recent release is a warning, not automatic rejection, for mature stable software.

Do not replace a sound existing stack merely because a newer framework is fashionable. Do not build a mini-framework, authentication system, router, state library, component library, workflow engine, parser, or protocol implementation from scratch without recording why maintained options are unsuitable.

## Mandatory product and interface gate

If the task changes anything a user sees or navigates, product UX must participate before implementation. Rendered UI and accessibility must verify after implementation.

The assignment cannot be `COMPLETE` merely because:

- the backend works
- tests pass
- the page renders
- the requested components exist
- the design resembles a generic dashboard

Before code, define the user, job, entry point, primary path, decisions, states, recovery, and information hierarchy.

After code, exercise the actual flow. Inspect realistic desktop and mobile widths. Verify loading, empty, validation, error, success, disabled, permission, destructive, and recovery states where relevant. Verify keyboard use, visible focus, semantics, names, contrast, zoom, and reduced-motion behavior where relevant.

Do not claim polished UI without rendered inspection. If browser or screenshot tooling is unavailable, report that limitation and do not mark visual acceptance as passed.

## Mandatory source-integrity gate

For research, strategy, comparisons, recommendations, market claims, and research-backed writing, read `references/source-integrity.md`.

Do not treat search rank, answer-engine citation, polished structure, a recent date, or repeated claims across syndicated pages as proof. Audit the source class, author, date, methodology, commercial incentive, independence, and whether citations support the claim.

Marketing, vendor, affiliate, PR, SEO, AEO, and GEO content may be useful for discovering claims or documenting what a company says. It is not independent validation of comparative quality, adoption, outcomes, or consensus. Corroborate load-bearing claims with primary records, current official documentation, reproducible observation, transparent research, or independent evidence with different incentives.

When the requested output itself targets SEO, AEO, or GEO, complete the people-first content and factual argument first. Apply current discovery practices afterward without distorting meaning, adding filler, manufacturing questions, or promising rankings or citations.

## Mandatory writing gate

For blogs, essays, technical arguments, founder narratives, and thought leadership, research must precede claims, and editorial verification must follow drafting.

For conference abstracts, talks, public arguments, launch narratives, and other work that must justify why this author or organization is worth hearing, also read `references/audience-value-loop.md` before drafting. Establish the commodity baseline, the author's evidence or access advantage, the audience delta, and the practical consequence. Do not use polished language to conceal missing information value.

Do not imitate a named writer. Transfer craft, not voice. The article must have:

- a specific audience
- one arguable thesis
- evidence, examples, mechanisms, or firsthand material
- a fair counterargument
- a reason the idea matters now
- an ending earned by the argument

When attention or differentiation matters, at least one load-bearing takeaway must depend on evidence, access, synthesis, demonstration, or judgment beyond generic domain knowledge. Do not invent privileged evidence to satisfy this requirement. Escalate for the missing author input or change the claim.

Run:

```bash
python <skill-directory>/scripts/check_blog_slop.py <draft-path>
```

The script is a warning tool, not the final judge. A clean result does not establish originality, information gain, factual support, or audience value. Editorial review must also detect generic framing, fake profundity, repetitive cadence, excessive headings or lists, unsupported consensus, empty predictions, abstract hype, copied thought-leader mannerisms, and em-dash overuse.

Respect an explicit style rule forbidding em dashes. When no rule is provided, still use them sparingly and never as the default sentence structure.

## Mandatory prompt inheritance gate

When the deliverable is a prompt, agent brief, system instruction, rule, or reusable workflow, read `references/prompt-generation.md`.

The generated prompt must itself establish loop behavior from first principles. Do not write only “use loop engineering” or “iterate until good.” The downstream prompt must define:

- outcome contract, baseline, target, measure, threshold, guardrails, required evidence state, constraints, and exclusions
- context inspection
- appropriate specialist routing
- artifact-verification and outcome-validation evidence
- compact persistent state when supported
- bounded action and verification cycles
- a hypothesis, predicted observation, measured delta, and learning for each meaningful cycle
- diagnosis and adaptation
- success-contract integrity: adapt the strategy without weakening the target, verifier, guardrails, or authority boundaries
- freshness and portability checks when technology is selected
- UI and UX verification when interfaces are involved
- research, source-incentive auditing, and anti-slop editing when writing is involved
- commodity-baseline and audience-delta checks when public writing must earn attention
- human approval boundaries
- explicit terminal states
- separate assignment status and evidence state

Simulate at least two realistic downstream cases, including one failure case, and revise the prompt if the receiving agent could claim success without the relevant evidence.

## Verification, validation, and evidence state

Verification confirms that the artifact meets its specification. Validation confirms that it fulfills its intended purpose for the intended stakeholder in the intended context.

Choose evidence by how directly it observes the contracted outcome. Deterministic checks are strong artifact evidence, but they are not automatically stronger than direct observation of intended use. Use actual or representative users, operators, environments, and decisions when feasible.

Report exactly one evidence state:

- `NO RELIABLE EVIDENCE`
- `ARTIFACT VERIFIED`
- `OUTCOME VALIDATED`
- `DECISION READY`

Do not approve work using only the same model's confidence or a score it invented. Separate maker and checker when possible. Otherwise use a cold verification pass that rereads the outcome contract, request, artifact, evidence, and diff without relying on the maker's narrative.

## Integration gate

When more than one specialist participates, the parent must run an integration pass after specialist checks.

Confirm that:

- artifacts agree on terminology and assumptions
- UX requirements match implementation
- backend states are visible and recoverable in the UI
- accessibility changes did not break interaction
- framework choices remain current and portable
- article claims match research evidence and are not laundered through marketing, SEO, AEO, GEO, affiliate, or PR summaries
- public arguments contain a supported audience delta and do not manufacture privileged access or findings
- editorial changes did not alter factual meaning
- generated prompts preserve the requested domain gates
- no specialist optimized its local metric at the expense of the overall outcome
- the integrated result reaches the parent target and required evidence state without violating guardrails

Rerun the primary end-to-end scenario and remeasure the parent outcome after any material integration fix.

## Safety and authority

Ordinary reversible local edits are allowed within the user's stated scope. Require explicit approval before:

- production changes or deployments
- destructive or irreversible operations
- purchases or financial commitments
- external messages or publication
- permission or security-policy changes
- access to privacy-sensitive information
- schema or data migrations without a tested rollback

Preserve unrelated work. Never expose, print, or commit credentials.

## Assignment status and evidence state

Report exactly one assignment status:

- `COMPLETE`: the scoped target and required evidence state are reached, guardrails pass, the result is usable for its named next step, and no required work remains
- `NEEDS HUMAN JUDGMENT`: evidence supports multiple choices and the remaining decision depends on taste, priorities, risk, values, or authority
- `BLOCKED`: a required external dependency, access, permission, or evidence source is unavailable
- `NOT FEASIBLE`: the requested outcome cannot be achieved safely or credibly within the constraints
- `STAGNATED`: two consecutive parent cycles produced neither measurable progress nor decision-relevant learning, the hypothesis changed at least once, and no credible next intervention remains

Pair the assignment status with one evidence state: `NO RELIABLE EVIDENCE`, `ARTIFACT VERIFIED`, `OUTCOME VALIDATED`, or `DECISION READY`.

Do not call exhausted budget, partial output, passing artifact checks, or an error `COMPLETE` unless those conditions satisfy the original outcome contract at its required evidence state.

## Final response

Keep the final response focused on the delivered result:

1. What changed or was concluded
2. Artifacts or files affected
3. Specialist loops used
4. Baseline, target, hypothesis tested, measured delta, and guardrail results
5. Artifact verification, outcome validation, and evidence limitations
6. Current-framework and portability decisions, when applicable
7. UI, UX, accessibility, or editorial decisions, when applicable
8. Remaining risk or limitation
9. Assignment status and evidence state

Do not dump state files, hidden reasoning, or every iteration.
