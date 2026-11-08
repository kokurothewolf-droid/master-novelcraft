# Revision, diagnostics, and editorial restraint

Sources: `manuscript-reviser(1).md`, `fiction-writing-prose(2).md`, `fiction-writing-story-development(1).md`, dialogue diagnostics, story-zoom, Moore revision rubric.

## Scope before edits

Identify requested level: **concept/structure**, **character/arc**, **scene/chapter**, **line/prose**, **copyediting**, **continuity**, or **comedy punch-up**. Reading the full available target before changing it is preferable. When only excerpts are available, explicitly limit conclusions to that scope. Verify POV, tense, author voice, language variety, character facts, timeline, and intended reader effect before touching text. If asked to critique, don't silently deliver a rewritten draft.

## Coarse-to-fine passes

1. **Canon and continuity:** names, bodies, species features, role, status, place, time, travel, objects, injuries, relationships, knowledge-at-time, character-driven acts, and prior promises. Distinguish confirmed contradiction, unreliable perception, planned revelation, and missing context. Flag the last rather than fabricating a repair.
2. **Architecture:** core idea/reader promise, causal chain, protagonist agency, opposing agendas, arc progression, pacing across chapters, subplot payoff, whether a scene is needed at all.
3. **Scene function:** desire, pressure, choice, consequence or deliberate stillness; transitions; setup/payoff; necessity of introspection and exposition; chapter opening/endings.
4. **POV and psychic distance:** accessible thoughts/senses, consistent tense, controlled narrative voice, deliberate distance changes, free indirect discourse. Omniscient is valid when established.
5. **Dialogue:** motive, subtext, relationship temperature, distinct voices, natural rhythm, information distribution, tags and beats, and comic timing.
6. **Prose and line craft:** clarity, exactness, rhythm, image quality, cliché, repetitive beats, weak verbs, redundant labels, overwriting or needless thinning, accessibility of invented terminology.
7. **Proofread:** grammar, punctuation, spelling, typography, house style. Do not silently convert the author's dialect or preferred punctuation conventions.

## Priority classification

- **Defect:** provable contradiction, incomprehensible movement, unintended POV violation, repeated incoherence, or clear breach of declared story contract.
- **Tradeoff:** two valid approaches with different reader effects, such as intimate vs distant POV, slow vs swift opening, explaining vs withholding world rules, ornament vs sparseness.
- **Preference:** an editor's favored style without demonstrable problem. Do not impose it as a correction.

Report major issues as **location → observation → likely reader effect → targeted fix → confidence/source**. Show examples or before/after where substantial. Keep other parts unchanged. Author approval controls all creative and canonical changes.

## Numerical heuristics are not targets

The Manuscript Reviser suggests 5–10% trims, 150–200-word opening checks, and 2–3 filter words per manuscript page; the prose guide suggests close attention to psychic distance and sentence patterns. These are **warning signs to examine, not automated thresholds**. Excellent lush, reflective, nonlinear or deliberately repetitive fiction may violate them with purpose. Avoid reporting an “improvement” simply because fewer words remain.

## Change propagation

For a canon or major-arc change, inspect consequences at **pitch → plot → scene → entity → manuscript** levels. Record affected chapters and classify blocking/high/deferrable. Do not run source watcher/CLI scripts unless actually installed and verified. When a revised scene changes a promise or knowledge state, include a proposed `continuity/change-log.md` entry.

## Revision deliverables

Provide (1) revised passage at requested scope when authorized, (2) concise categorized change log, (3) unresolved continuity questions and assumptions, (4) optional alternatives where the author must choose a tradeoff. For large manuscripts, prioritize substantive defects and provide a pass-by-pass plan rather than claiming exhaustive unseen review.

## Typical failure patterns

- **Generic polish:** erases lively eccentricity. Fix: compare against approved voice sample.
- **Overrepair:** fixes deliberate untrustworthy narration, contradictions between opinions, or controlled anachronism. Fix: trace narrator/research/canon status first.
- **Microediting too early:** sentence polish before plot redesign. Fix: top-down ordering.
- **Stale lore:** character profile describes end-of-book state at chapter 1. Fix: effective-from states.
- **Unfounded critique:** claims weak humor or motivation without locating text. Fix: support diagnosis with scene evidence.
- **Over-joking:** trades emotional sincerity for a punchline. Fix: preserve intended dramatic contract.

## Portable project state and file authority

If a user wants a persistent story project, the minimal plain-Markdown version consists of `story.md`, `characters/`, `world/`, `plot/`, `manuscript/`, and `continuity/`. Use `templates/story.md`, `templates/character.md`, `templates/scene.md`, `templates/volume-plan.md` and `templates/canon-change.md`. Preserve any existing author's folder scheme instead of migrating unasked. Do not require commands from the original Story CLI skill, which may not be available.

For every proposed new canon fact distinguish: **confirmed by author**, **confirmed by excerpt**, **inferred**, **planned**, **unresolved**. Date the effective chapter if the fact changes during a novel. A character's belief, rumor, dream, flashback and deliberate lie must not overwrite the objective source-of-truth registry. A proposed patch is not a completed modification.

## Collaborative editing and writers-room adaptation

`sw-writers-room` contributes the practice of separating brainstorming from decision: generate alternatives, articulate each version's effects, record what the author accepts, and critique the work rather than the person. If several AI agents are used, appoint one canonical record and report conflicting proposals rather than merging incompatible drafts automatically. Do not import film-industry hierarchies or writer-room labor practices as literary requirements.
