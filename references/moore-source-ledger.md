# Source ledger and interpretation protocol

## Status of the supplied corpus

This skill is based exclusively on **seven user-supplied Markdown files**. Six are first-person, Moore-attributed transcript texts. One is a LitReactor article by another writer discussing *Writing for Comics* and quoting excerpts attributed to Alan Moore. None of these documents has been independently checked against original audio, video, books, or verified publication metadata. The metadata field `created: 2026-11-07` for S02 is a clipping date and **not** evidence of the article's publication date.

Use these provenance labels:

- **[T] Transcript-based:** Supported by first-person advice in the supplied Moore-attributed transcript. This is an attribution within the provided material, not independently authenticated.
- **[Q] Quoted-in-secondary:** Words quoted as Moore's by the S02 article. The quote is available only through the secondary source in this corpus.
- **[C] Commentary:** The S02 article author's framing, examples, or recommendation; do not say Moore teaches it unless supported elsewhere.
- **[A] Adaptation:** An agent workflow, diagnostic heuristic, exercise, template, or reasonable novel-specific implementation built from the preceding evidence. It is not presented as Moore's direct prescription.

Each `S##:L##` refers to the supplied Markdown copy's **physical line number**, not to a line number in the original videos or publications. Most transcripts put an entire paragraph on one line. Read linked paragraphs in full rather than cherry-picking fragments.

## Register

| ID | Retained copy | Type | Distinctive content |
|---|---|---|---|
| S01 | [`../sources/S01-language-experiments.md`](../sources/S01-language-experiments.md) | [T] | Surprise in diction, juxtaposition, Lovecraftian dissonance, Shakespearean wordplay, Oulipo constraints. Lines 2, 4, 6, 8, 10. |
| S02 | [`../sources/S02-litreactor-writing-guide.md`](../sources/S02-litreactor-writing-guide.md) | [Q] + [C] | Quoted distinctions of idea/plot, immersive transitions, exposition, physical character enactment, risk, reputation, human ethics; journalist's own interpretations and naming suggestion. Lines 23-87. |
| S03 | [`../sources/S03-place-and-time.md`](../sources/S03-place-and-time.md) | [T] | Place as psychology, location research, psychogeography, invented-world texture and consistency, historical specificity, in medias res. Lines 1, 3, 5, 7, 9, 11. |
| S04 | [`../sources/S04-character.md`](../sources/S04-character.md) | [T] | Entering characters' embodied experience, research, empathic villains, independent agency, everyone seeing themselves as protagonist. Lines 2, 4, 6, 8. |
| S05 | [`../sources/S05-genre-mode-voice.md`](../sources/S05-genre-mode-voice.md) | [T] | Genre literacy/subversion, comic and horrifying expectation reversals, tense, first/third/close third narration, unreliability, free indirect discourse. Lines 2, 4, 6, 8, 10. |
| S06 | [`../sources/S06-four-weapons.md`](../sources/S06-four-weapons.md) | [T] | Earth/material understanding; sword/discrimination; cup/compassion; wand/will; taking responsibility and completing work. Lines 1, 3, 5, 7, 9, 11, 13. |
| S07 | [`../sources/S07-language-reader.md`](../sources/S07-language-reader.md) | [T] | Word order, reader embodiment, provocative neuroscience claims, inventive language, Joyce/Lovecraft examples, constraints, language and consciousness. Lines 2-14. |

## Important interpretive boundaries

1. **S01 and S07 overlap substantially.** Their shared Lovecraft, Shakespeare, Joyce, and unusual-diction material should be **deduplicated**, not counted as separate independent confirmation.
2. **S02 is not a direct source transcript.** The article's use of *Prey* to distinguish idea and plot (L33), the recommendation to use Find a Grave for names (L55-L57), and its informal discussion of exposition are **commentary [C]**. Moore quotes at L25, L39, L47, L53, L67, L75, L81, and L87 are **[Q]**.
3. **Narratological precision matters.** S05:L8 calls third-person broadly omniscient; novelistic third person can be **limited, close, or omniscient**. Use the source to justify choosing narratorial distance, not to perpetuate that generalization as a rule. S05:L10 presents close third and free indirect discourse favorably; free indirect discourse is a technique, not unrestricted hopping among minds.
4. **Neuroscience is not established here.** S07:L2-L6 and S01:L6 include claims about mirror neurons, brain-imaging and wordplay. The corpus does not provide scientific studies or verification. Their usable literary insight is attention to sequencing, embodied perception, and surprise, **not** a proven neural mechanism.
5. **Psychological labels are historical source phrasing, not characterization requirements.** S04 refers to extreme states, villains, and hypothetical nonhuman perspectives. Adapt empathetically and research represented conditions rather than defaulting to stereotypes.
6. **Some original context is comics.** Transitions, captions, and dialogue exposition quoted in S02 are translated into prose-specific equivalents as **[A]**: scene joins, time/location changes, internal exposition, and conversational information exchange.
7. **The magic/tarot framework is metaphorical in the supplied text.** S06 explains four symbolic abilities. Do not require supernatural beliefs or occult framing from the writer.
8. **Preserve positive creative control.** Moore's encouragement toward risky work does not license overriding the author's boundaries or changing the requested genre, tone, or audience.

## What this corpus does **not** prescribe

There is no canonical Moore-authored three-act outline, scene-beat algorithm, mandatory chapter length, commercial pacing formula, word-count goal, objective numerical scoring system, AI prompting architecture, or standardized manuscript-tracking schema in these seven files. Such procedures in this skill are explicitly labeled **[A]**.

The corpus also does not provide independently verified cognitive-science citations or a complete account of *Writing for Comics*. Do not infer the missing chapters or invent advice from the book.

## Attribution examples

- Correct: “The transcript on character agency argues that every person experiences themselves as the center of their own narrative (P04; S04:L8) [T].”
- Correct: “Use a brief scene objective and change log as an implementation aid [A], informed by independent character motives (P03-P04).”
- Correct: “A passage quoted in the LitReactor article distinguishes a story's idea from its plot (P01; S02:L25) [Q].”
- Incorrect: “Alan Moore scientifically proved invented words activate the brain in a specific way.”
- Incorrect: “Alan Moore recommends a three-act plot and a scene checklist.”
- Incorrect: “Moore tells writers to search Find a Grave for character names.” (That recommendation is the journalist's.)
