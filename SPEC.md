# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

1. Keep the supplied interface/server and implement only `determine_winner`: equal moves tie; rock beats scissors, paper beats rock, and scissors beats paper; other valid pairs lose.
2. Add all nine literal unit outcomes from the table and one real Flask request/result check with the computer choice fixed. Reuse the supplied missing/unsupported-input checks.
3. Add one Chromium journey using real rules: play Rock against fixed Scissors, then replay with Paper and verify the new loss. Do not stub the rules or repeat every matchup through the browser.
4. Run the full shared checks and review the diff before browser play. Then inspect actual choices/results, replay and keyboard behavior, and record only performed checks. Keep scoring for a later feature.

Prediction before implementation: Rock against Paper returns `lose`, because Paper beats Rock. This guided walkthrough uses the current coding chat; ChatGPT desktop UI control is unavailable.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round](https://github.com/kaw393939/rps-self-paced-trial-1025/issues/1).
- Implementation: [rule function](game.py), [nine outcomes and real request](tests/test_game.py), and [real-browser round/replay](tests/e2e/test_round.py). The supplied app, interface, fixtures, and shared check configuration are unchanged.
- Checks: `.venv/bin/python check.py` passed Black, Pylint, 22 non-browser cases, and two actual Chromium cases. The ten new rule/request cases first failed against the unfinished rules. Reviewed the four changed files against this spec, including the untracked tests. Rock/Paper's literal `lose` expectation matches the prediction above.
- Browser observations through Computer Use in Safari: Rock/Scissors won; Paper/Paper tied; Scissors/Rock lost; replay updated both choices and the result. Option+Tab visibly focused Rock and Enter submitted Rock/Paper, which lost correctly. Plain Tab skipped buttons with this browser's settings. Reopening the printed address avoided Safari's form-resubmission prompt.
- Trial limit: implementation and commands used the current coding chat and command tool. ChatGPT desktop and Terminal UI control were blocked; no independent student or human review is claimed. Detailed evidence belongs in the linked PR.
