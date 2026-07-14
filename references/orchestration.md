# Orchestration and Handoffs

## Contents

- [Parent and check owners](#parent-and-check-owners)
- [Execution modes](#execution-modes)
- [Routing](#routing)
- [Handoff lifecycle](#handoff-lifecycle)
- [Return and integration](#return-and-integration)
- [Conflicts and stopping](#conflicts-and-stopping)

## Parent and check owners

Use one parent for the assignment. The parent owns the user outcome, success card, shared evidence, routing, budget, integration, approval boundaries, and terminal state.

A specialist is the owner of one material failure check. It is not automatically a separate agent. The parent must know what can actually receive and execute the check before creating a handoff.

Specialists inherit the parent target, measure, guardrails, and proof requirement. They may define local acceptance checks but must not weaken the assignment contract. They return to the parent rather than calling one another freely.

## Execution modes

Select the strongest available mode and record it when independence matters.

### Real specialist

Use when a subagent, human reviewer, independent context, or purpose-built checker can actually receive a bounded task.

1. Create and validate the handoff request.
2. Deliver it to the named recipient.
3. Require a completed return with evidence.
4. Validate the return.
5. Let the parent integrate and remeasure the overall target.

### Cold same-session pass

Use when no independent recipient is available but files can preserve a clean request.

1. Write the handoff.
2. Reopen the original request, success card, handoff request, and target artifact.
3. Ignore the maker's narrative and inspect from the named failure class.
4. Complete the return and disclose that maker/checker independence was limited.
5. Let the parent integrate and remeasure.

### In-memory pass

Use when neither an independent recipient nor useful file state exists. Keep a short request/return receipt in context. Do not claim independent review.

An undelivered template, a role label, or a statement that a specialist “participated” is not a handoff.

## Routing

Start with the failure that could let the artifact pass while the intended outcome fails. Add only check owners able to observe a material risk.

Common compositions are hypotheses, not mandatory pipelines:

- **Visible product feature:** product UX before implementation; engineering; rendered UI and accessibility after implementation; parent rerun.
- **Backend-only change:** engineering; security, concurrency, or migration review only when relevant; parent integration.
- **Research-backed article:** research and source incentives; audience value when attention matters; article; editorial and factual verification; parent integration.
- **Public abstract:** evidence/access inventory; audience value; argument; editorial; promise verification; parent integration.
- **Strategy:** current research when needed; strategy; feasibility and counterargument; parent integration.
- **Downstream prompt:** task analysis; prompt generation; normal, failure, and false-success simulation; relevant domain review; parent integration.

Parallelize only genuinely independent checks with a clear integration contract. Do not parallelize work that depends on a shared experience contract or a single coherent argument.

## Handoff lifecycle

Use `scripts/create_handoff.py` when persistent files are available. It reads the parent state and refuses to create a handoff until the baseline, target, measure, guardrails, proof requirement, and constraints are populated.

The artifact has three phases.

### Request

The parent supplies:

- goal and artifact
- inherited parent success criteria
- current state and already verified facts
- remaining uncertainty
- constraints and preserve/change boundaries
- the bounded specialist task
- observable acceptance checks
- predicted contribution

Validate this phase with:

```bash
python3 scripts/validate_handoff.py <handoff> --stage request
```

### Return

The recipient supplies the fields below. Record them with `scripts/complete_handoff.py return`; run `--help` for the full command:

- one status: `PASS`, `REWORK_REQUIRED`, `BLOCKED`, or `NEEDS_HUMAN_JUDGMENT`
- findings and changes
- reproducible evidence
- actual observation or decision-relevant learning
- one evidence state
- unresolved uncertainty
- recommended next step

Validate this phase with:

```bash
python3 scripts/validate_handoff.py <handoff> --stage return
```

### Parent closure

After integration, the parent records exactly one disposition: `ACCEPTED`, `REWORK`, or `ESCALATED`, plus evidence from rechecking the integrated result. Use `scripts/complete_handoff.py close`, then validate with `--stage closed`.

The lifecycle status should move from `REQUESTED` to `RETURNED` to `CLOSED`. A valid return is not closed until the parent records its disposition.

## Return and integration

Specialist status and assignment status are different. A local `PASS` does not imply assignment `COMPLETE`.

Before accepting a return, confirm that:

- the recipient answered the bounded task
- evidence supports the selected status and evidence state
- remaining uncertainty is explicit
- protected constraints remain intact
- the return does not silently redefine success

After accepting or applying changes, the parent reruns the primary scenario and remeasures the parent target. For multi-specialist work, also check that terminology, assumptions, UX requirements, implementation states, accessibility, factual meaning, and technology constraints still agree.

If only artifact checks are possible, report `ARTIFACT VERIFIED` and preserve the validation gap.

## Conflicts and stopping

When checks conflict:

1. Identify the parent acceptance criterion affected.
2. Prefer evidence closest to the user's intended outcome.
3. Preserve non-negotiable safety and accessibility requirements.
4. Run a representative scenario when possible.
5. Escalate taste, cost, risk, values, or authority decisions.

Do not average incompatible recommendations. Route rework through the parent:

```text
specialist -> parent -> prioritized rework -> targeted verification -> parent
```

Stop rather than creating a circular chain. If two parent cycles yield neither measurable progress nor decision-relevant learning and no credible alternative remains, return `STAGNATED`.
