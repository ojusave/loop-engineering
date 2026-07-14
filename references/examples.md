# Routing Examples

## Contents

- [Activation](#activation)
- [Small code fix](#small-code-fix)
- [Product feature](#product-feature)
- [Backend feature with no UI](#backend-feature-with-no-ui)
- [Framework choice](#framework-choice)
- [Research-backed article](#research-backed-article)
- [Conference abstract](#conference-abstract)
- [Strategy](#strategy)
- [Prompt generation](#prompt-generation)
- [Outcome-contract examples](#outcome-contract-examples)
- [Handoff example](#handoff-example)


## Activation

Activate:

```text
loop: fix the login bug and verify it
```

```text
use loop to build a polished responsive settings flow
```

```text
loop this task: research and write the article without AI slop
```

Do not activate:

```text
Why is this for loop slow?
```

```text
Explain the JavaScript event loop.
```

## Small code fix

Prompt:

```text
loop: fix the incorrect timezone conversion
```

Route:

```text
parent -> engineering -> parent integration
```

Evidence:

- reproduction
- targeted test
- relevant broader tests
- diff inspection

## Product feature

Prompt:

```text
loop: add an onboarding flow for creating a service
```

Route:

```text
parent
  -> freshness/portability if dependencies are considered
  -> product UX experience contract
  -> engineering
  -> rendered UI
  -> accessibility
  -> parent integration
```

False success to reject:

- API works
- page renders
- component tests pass
- no mobile or error state checked

## Backend feature with no UI

Prompt:

```text
loop: add idempotency to webhook processing
```

Route:

```text
parent -> engineering -> concurrency/data review -> parent integration
```

Do not invoke UI specialists unless an operator interface changes.

## Framework choice

Prompt:

```text
loop: choose and integrate a workflow library
```

Route:

```text
parent -> freshness/portability -> engineering -> integration
```

Required evidence:

- project fit
- current official docs and release/support state
- license
- alternatives
- adapter boundary
- migration path

## Research-backed article

Prompt:

```text
loop: research and write a strong article about developers delegating setup to agents. No AI slop and no em dashes.
```

Route:

```text
parent -> research -> article -> editorial -> fact check -> parent integration
```

False success to reject:

- polished generic prose
- factual claims with no thesis
- a thesis or talk promise a competent generalist could produce without the author's evidence, access, demonstration, synthesis, or judgment
- copied Theo, swyx, or Garry Tan cadence
- inspiring ending unsupported by the article
- any em dash in the final draft

## Conference abstract

Prompt:

```text
loop: make this engineering conference title and description impossible to ignore
```

Route:

```text
parent -> speaker evidence/access inventory -> audience value -> argument contract -> editorial -> promise verification -> parent
```

False success to reject:

- a vivid title attached to generic best practices
- biography or employer scale used instead of a finding
- an empty teaser that withholds the talk's actual contribution
- invented proprietary data, experience, framework names, or organizational bets
- takeaways obtainable from common knowledge and the supplied public context

## Strategy

Prompt:

```text
loop: decide whether we should build or partner for this feature
```

Route:

```text
parent -> research as needed -> strategy -> feasibility review -> parent
```

Output should contain one recommendation, assumptions, tradeoffs, and a reversible first test.

## Prompt generation

Prompt:

```text
loop: create a prompt for Cursor to build a polished open-source admin tool
```

Route:

```text
parent -> prompt generation -> downstream simulation -> product/UI prompt review -> parent
```

The output prompt must itself route product UX before implementation and rendered UI after implementation.

## Outcome-contract examples

### Code bug

```text
Outcome owner or beneficiary: API callers
Outcome class: state change
Baseline: duplicate webhook delivery creates two orders
Target state: repeated delivery with the same event ID creates exactly one order
Intended context of use: integration test and production-like worker runtime
Primary measure and threshold: one persisted order after two identical deliveries
Guardrails: distinct event IDs still create distinct orders; no lost notification
Required evidence state: OUTCOME VALIDATED
Next decision or use: merge the fix
```

Passing unit tests without exercising repeated delivery is only `ARTIFACT VERIFIED` and does not satisfy this contract.

### Research decision

```text
Outcome owner or beneficiary: engineering lead choosing a workflow library
Outcome class: decision
Baseline: alternatives and compatibility are unresolved
Target state: one option can be selected with bounded migration and maintenance risk
Primary measure and threshold: required capabilities, license, support status, and migration path are resolved for the top options
Guardrails: do not introduce avoidable lock-in or unsupported software
Required evidence state: DECISION READY
Next decision or use: approve adoption or decline all options
```

A long source list without a decision threshold is not `DECISION READY`.

### Conference abstract with missing evidence

```text
Outcome owner or beneficiary: target conference attendee and speaker
Outcome class: artifact
Baseline: the description promises generic reliability advice
Target state: target readers can identify the talk's unique, deliverable learning promise
Primary measure and threshold: representative readers distinguish the promise from a generic overview; the speaker confirms every claim is supportable
Guardrails: do not invent telemetry, experience, findings, or organizational bets
Required evidence state: OUTCOME VALIDATED
Next decision or use: submit or publish the abstract
```

If the speaker's distinctive evidence is unavailable, stop `BLOCKED / NO RELIABLE EVIDENCE`. Do not invent a framework and call the copy complete.

## Handoff example

```text
FROM: engineering
TO: rendered-ui
OBJECTIVE: Verify the first-time service creation path.
ARTIFACT: Running application at http://localhost:3000
CURRENT VERSION OR PATH: working tree after feature implementation
PARENT OUTCOME AND TARGET MEASURE: first-time user creates a service successfully
BASELINE AND REQUIRED EVIDENCE STATE: current flow unverified; OUTCOME VALIDATED
VERIFIED FACTS: build and API integration tests pass
EVIDENCE OR COMMANDS: npm test; npm run build
KNOWN WEAKNESSES: mobile layout and permission error not inspected
CONSTRAINTS AND NON-GOALS: preserve existing design tokens and API contract
MAY CHANGE: layout, labels, local component structure
MUST PRESERVE: service payload and route behavior
TARGET ACCEPTANCE CRITERIA: primary path is clear at desktop and mobile; error is recoverable
EXPECTED CONTRIBUTION AND PREDICTED OBSERVATION: clearer hierarchy should let representative users identify and complete the primary action
ACTUAL OBSERVATION AND MEASURED DELTA: pending specialist test
EVIDENCE STATE: ARTIFACT VERIFIED
RETURN STATE: PASS | REWORK_REQUIRED | BLOCKED | NEEDS_HUMAN_JUDGMENT
```
