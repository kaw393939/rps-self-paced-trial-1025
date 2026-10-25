# Next: RPS-002 — First to two wins

**Your turn with less guidance.** Reuse the process from RPS-001; write your own short request and test plan rather than copying the first lab's full prompts.

Finish and merge RPS-001 first. Start this change from your updated `main`:

```sh
git switch main
git pull --ff-only
git switch -c rps-002
```

Repeat: discuss → update the spec and open an issue → build → AI checks → your review → PR.

Agree these decisions **before** coding:

- A win adds one point to the winner. Ties add no points.
- Show both scores. The first side to two wins the match.
- After the match, keep the final result visible and stop further scoring.
- A **New match** control resets both scores and clears the previous result.
- Decide what refreshing the page does. Keep storage/accounts outside this change.

Add RPS-002 to `SPEC.md`, with examples for a tie, a match win, another click after the match, and reset. Ask AI how it will test the sequence deterministically and preserve RPS-001’s nine rules. Choose the simplest design together; do not add a database or architecture pattern just for this exercise.

Plan valid play and rejected post-match actions at the appropriate test level. Keep most scoring/reset combinations in fast tests and one complete match/reset journey in the browser. Run `.venv/bin/python check.py` before review; passing the old round tests alone does not verify the new match behavior.

Keep this feature in its own issue and PR. A game name/color change is optional after behavior works; keep text labels and readable contrast.
