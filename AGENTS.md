# Working on this student game

- Read SPEC.md and existing code before editing. Treat the agreed spec as current context; flag conflicts and unclear behavior before coding.
- The starter deliberately leaves RPS-001 unimplemented in game.py. Supplied shell tests do not prove the game rules.
- Keep RPS-001 to one independent round. No score, accounts, storage, new frontend framework, AI API, or OOP patterns unless separately agreed.
- The primary path is one local Codex chat inside ChatGPT desktop for discussion, saving the agreed SPEC.md, implementation, tests and review. Students use terminal Git over SSH and a browser. VS Code is optional. Do not require an IDE extension, Codex CLI install, app-to-app plan transfer, or a Command Palette/Git GUI workflow.
- This is self-paced. Explain one next action and what success looks like. Do not assume an instructor demonstration. Keep planning and building in the same chat; preserve durable decisions in SPEC.md rather than requiring transcript copying.
- Run .venv/bin/python check.py for Black, Pylint, fast pytest tests and Chromium E2E; CI uses the same command. --fast is for intermediate feedback only and must be reported as skipping browser checks. Do not weaken configuration, disable checks, or remove meaningful assertions just to pass; discuss legitimate changes first.
- Plan positive and negative cases at appropriate unit/integration/E2E levels. A valid loss or tie is a positive case. Reuse supplied invalid/missing-input integration checks; do not duplicate all nine cases in the browser.
- Add nine explicit unit outcomes from SPEC.md and a real request/result integration check to tests/test_game.py. Add tests/e2e/test_round.py for a real browser round and replay using supplied live_server/page fixtures. Mark tests unit, integration, or e2e. Fix only randomness, not the rule function being verified; use literal expected answers. Use Playwright waiting assertions, no arbitrary sleeps or retries until passing.
- Before asking the student to play, run checks, inspect the diff against the spec, fix identified problems, and report actual results and limitations. Never invent browser checks or claim a second AI review is independent proof.
- Preserve the student's agreed plan and issue link. Record concise actual checks and relative code/test links in SPEC.md. Keep detailed evidence in the PR; avoid temporary status such as 'not pushed'.
- No commits, pushes, or merges unless the student asks. Explain unexpected changed files. Keep .venv, caches, credentials, and local data out of Git.
