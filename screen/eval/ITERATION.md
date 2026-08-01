# Prompt iteration log — merchant policy screening

Referee: the 16-merchant fixture manifest (`fixtures/manifest.yaml`) carries the
expected decision + reason codes for every merchant; `score.decisions` reports exact-
decision accuracy and decline recall after every change. Screening responses are cached
(`screen/eval/cache/`, committed), so the pipeline replays offline.

## screen_v1 — baseline

Design: full AUP-1 text in prompt; verdicts {pass/restricted/prohibited/insufficient-
info} with verbatim quotes; unverifiable quotes voided to insufficient-info (AUP-05.1);
scorecard hard override: ANY insufficient-info verdict → manual review.

Result: **6/16 exact decisions (37.5%)**, decline recall 4/5.

Failure taxonomy (from reading the 10 misses):

1. **Systematic over-routing to manual review (9 of 10 misses).** The model
   conscientiously emitted `insufficient-info` for policy areas that site text *cannot*
   evidence (portfolio monitoring, review reputation — the latter handled by a separate
   call), and the scorecard's fail-safe override treated any such verdict as "send a
   human." Every clean merchant landed in manual review. The bug was the interface
   between a cautious model and a blunt override — neither alone.
2. **One fixture overshot its own brief.** `titan-supps` was specified as "borderline
   health claims → manual review," but the authored copy said "reverses diabetes
   naturally" — which AUP-01.9 grades as prohibited. The model declined it, and the
   model was right; the fixture, not the model, was mislabeled. Fixed by softening the
   copy to genuinely borderline structure/function language.

## screen_v2 — scoped sections + graded claims

Changes: (1) explicit SCOPE block — assess only what site text can evidence (AUP-01/02/
03 + health-claim language); out-of-scope areas are simply not assessed, never
insufficient-info; insufficient-info reserved for category-level unassessability.
(2) explicit AUP-01.9 grading: disease-cure/reversal claims prohibited, structure/
function puffery restricted at most. Scorecard override narrowed to core-section
(AUP-01/02) insufficient-info only (with a regression test for the non-core case).

Result: ⟨V2-RESULT⟩

## Verification discipline (unchanged across versions)

Every restricted/prohibited verdict must quote the site verbatim (whitespace/case-
normalized string check); a failed quote voids the verdict toward the fail-safe
direction. Review-theme quotes verified against the review corpus the same way.
