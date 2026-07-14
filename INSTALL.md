# Install in Cursor

Unzip the package into the project-level Cursor skills directory:

```bash
mkdir -p .cursor/skills
unzip skill.zip -d .cursor/skills
```

Expected structure:

```text
.cursor/
  skills/
    loop-engineering/
      SKILL.md
      references/
      scripts/
```

Restart or reload Cursor after installation.

Invoke explicitly:

```text
loop: fix this bug and verify the result
```

```text
loop: build this feature with a clear user flow and polished responsive UI
```

```text
loop: research and write this article. No AI slop and no em dashes.
```

```text
loop: generate a prompt for another coding agent. The resulting prompt must also use bounded loop engineering.
```

The skill creates local task state under `.loop/` and adds `.loop/` to the project root `.gitignore`.

The `.cursor/skills/loop-engineering/` directory may be committed when the team should share the skill. Keep `.loop/` uncommitted.

Research example:

```text
loop: research whether this framework is a current fit, then write a comparison. Derive the evidence plan for this question and distinguish official documentation from vendor marketing, affiliate pages, SEO/AEO/GEO content, and independent evidence.
```

The protocols are adaptive. They provide fixed reliability boundaries, but the agent derives the task-specific outcome contract, evidence plan, specialist order, and checks from the current request and repository.

Every substantive invocation should establish an observed baseline, a target state, a measure and threshold, guardrails, and a required evidence state. Each meaningful cycle records its prediction, actual observation, measured delta, and learning. Final reports keep assignment status separate from evidence maturity so passing checks cannot masquerade as a validated outcome.

Loops correct their strategy when evidence contradicts it. They do not autonomously weaken the target, verifier, guardrails, or authority boundaries. Persistent changes to a loop or evaluator require representative before-and-after evidence and appropriate approval.
