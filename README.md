# Master Novelcraft

**A portable AI writing skill for developing, drafting, revising, and learning to write novels and light novels.**

Master Novelcraft is built primarily from Alan Moore’s writing advice, as represented in the supplied transcripts and commentary, and expanded with complementary prose, story-development, and screenwriting craft methods. It turns those principles into practical workflows, focused references, and reusable templates for an AI creative collaborator, writing tutor, developmental editor, line editor, or continuity assistant.

Its guiding principle is simple: **the author leads; craft frameworks serve the story.**

## What it helps with

- **Story development:** Explore premises, themes, genre expectations, plot structures, and alternative directions.
- **Characters:** Develop desires, contradictions, relationships, motivations, and choices under pressure.
- **Scenes and chapters:** Shape openings, progression, revelations, emotional turns, and endings.
- **Prose and dialogue:** Work on point of view, voice, interiority, imagery, rhythm, subtext, and exposition.
- **Revision:** Diagnose structural problems, revise within a defined scope, and preserve established facts.
- **Comedy:** Build humor from character, situation, escalation, physicality, and relationships.
- **Series planning:** Track subplots, recurring story engines, relationship development, and promises across volumes.
- **Writing practice:** Learn a technique through explanation, original examples, exercises, and feedback.

Optional modules support light novel conventions and romantic or ecchi comedy when the author explicitly requests them. These modes do not automatically apply to every project.

## How it works

The main `SKILL.md` routes each task to the relevant craft references. The assistant loads the material needed for the request rather than treating every technique as a rule to apply simultaneously.

Master Novelcraft supports structure-first, discovery-first, and hybrid writing. It does not require every novel to follow the same outline, every scene to contain a dramatic reversal, or every protagonist to undergo a transformation.

When methods disagree, the author's intent, the existing manuscript, and the desired reader experience guide the choice.

## Getting started

To upload this package to GitHub, follow [UPLOAD_TO_GITHUB.md](UPLOAD_TO_GITHUB.md).

1. Download the skill folder from this repository.
2. For an assistant that supports folder-based skills, copy the complete folder into its skills directory. Keep `SKILL.md`, `references/`, and the other bundled resources together. Follow your assistant's instructions to enable it.
3. Provide your writing brief. For existing fiction, include the relevant manuscript and current character or world notes.
4. Specify whether you want ideas, planning, drafting, critique, revision, continuity work, or a lesson.

For an assistant without a skill installer, provide `SKILL.md` as instructions and make the referenced files available as project documents. Reference loading depends on the host application's capabilities.

**Requirements:** An AI assistant that can follow Markdown instructions and access the supplied files. The core writing workflow needs no separate runtime, Story CLI, or dedicated paid API. Your chosen AI service may have its own costs and limits.

## Example requests

### Develop a story

> Use Master Novelcraft to develop three directions for a cozy mystery set in a floating market. Compare the protagonist, recurring conflicts, and reader promise before outlining.

### Draft a scene

> Write a close-third scene in past tense. A retired cartographer discovers that her latest map includes a room she has never entered. Keep the voice restrained and end on a consequential choice.

### Critique without rewriting

> Review this chapter for character motivation, pacing, and point of view. Rank the three most consequential issues, cite evidence from the text, and suggest repairs. Do not rewrite it yet.

### Revise comedy

> Revise this scene as an adult romantic comedy. Increase character-driven humor, flirtation, and escalating embarrassment while preserving the plot, character agency, and established boundaries.

### Learn a technique

> Teach me subtext through two short original examples, then give me an exercise and feedback on my attempt.

### Check continuity

> Compare this chapter with the supplied canon notes. Separate factual contradictions, unanswered questions, and optional craft suggestions. Do not invent missing history.

## Give it a useful brief

Include whatever you already know:

| Detail | Examples |
| --- | --- |
| Task | Draft, critique, revise, outline, teach, or check continuity |
| Form and audience | Standalone novel, light novel, series; intended readership |
| Genre and tone | Cozy fantasy, thriller, literary fiction, romantic comedy |
| Narrative voice | Point of view, tense, distance, and stylistic preferences |
| Source material | Manuscript, outline, character notes, world rules |
| Scope | Scene, chapter, selected passages, or whole-book diagnosis |
| Boundaries | Required events, content limits, facts that must remain intact |

You do not need to settle every detail before starting. The skill is designed to work with exploratory drafts and provisional plans.

## Package structure

| Location | Purpose |
| --- | --- |
| `SKILL.md` | Main instructions, working modes, and reference routing |
| `agents/` | Host-specific skill metadata |
| `references/` | Focused craft guides, method choices, and source ledgers |
| `templates/` | Markdown structures for story, character, scene, volume, and canon records |
| `examples/` | Original examples illustrating different development approaches |
| `tests/` | Package checks and behavioral acceptance scenarios |
| `sources/` | Imported source guides, literary-craft documents, and comparative material |

The public edition is intended for general use. Private manuscripts, personal character notes, and project-specific canon are outside its scope.

## Sources and attribution

Alan Moore’s writing advice provides the skill’s primary foundation: language and voice, character agency, the influence of place, genre expectations, experimentation, and the writer’s responsibility to the reader. The seven supplied Moore-related documents include attributed transcripts and secondary commentary. Their provenance and interpretation limits are documented in [`references/moore-source-ledger.md`](references/moore-source-ledger.md).

The practical AI workflows and novel-specific adaptations are this project’s synthesis. This is an independent project, with no affiliation with or endorsement by Alan Moore.

The skill synthesizes literary craft principles, contributed writing guides, and selected screenwriting techniques adapted for prose fiction. These are tools for original writing, not instructions to imitate a named author's distinctive prose.

Source ledgers distinguish supplied-source claims, secondary interpretations, novel adaptations, and new synthesis. Attribution in a supplied document is not independent verification of every claim about an author, book, or research finding.

Source documents are included under `sources/` for attribution and comparison, separately from the operational guides. One comparative document is a public extract with private applications removed. See [public edition notes](PUBLIC_EDITION_NOTES.md) and [third-party notices](THIRD_PARTY_NOTICES.md). Source inclusion does not change the original material's applicable terms.

## Status and limitations

**Current basis: v2.1 release candidate.**

The skill cannot guarantee publication-ready prose, originality, factual accuracy, or perfect continuity. It can only check the manuscript and canon made available to it. Structural validation checks packaging and references; it does not establish writing quality or reliability across all AI models.

Author preferences about theme, outlining, and character development remain selectable per project rather than mandatory global defaults.

## Contributing

Useful contributions include clearer instructions, stronger original examples, broken-reference fixes, and reproducible reports of unwanted behavior.

For a behavior report, include the request, relevant context, expected behavior, and actual output. Remove private manuscript content and personal information before posting.

Prefer adaptable craft guidance over universal prescriptions. Clearly identify the origin and redistribution terms of contributed material.

## License

Master Novelcraft's original contributions are licensed under the [MIT License](LICENSE).

You may use, copy, modify, distribute, sublicense, and sell copies of the covered material, provided you retain the copyright and permission notices. The material is provided without warranty.

This license covers only original contributions by the project author. Third-party source documents, imported skills, quotations, and other separately attributed material retain their own applicable terms. Their presence in a working package does not grant redistribution rights or place them under MIT.
