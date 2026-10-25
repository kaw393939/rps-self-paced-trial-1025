# Build a game you can trust—with AI

This is a **self-paced, guided first lab**. Make one round of Rock, Paper, Scissors work, then show why you trust the result. You will agree on a short spec, guide an AI coding agent, use automatic checks, and review its work.

Use **ChatGPT desktop in Codex mode**, your **class terminal**, and a **browser**. Codex is the coding agent inside the app: it can read your project, edit files, and run checks. **VS Code is optional.** No API key, separate Codex CLI, or classroom demonstration is required.

**Try → Decide → Build → Check → Keep.** If you stop, return to this README at the last checkpoint you completed. [Visual overview](https://kaw393939.github.io/218_spec/).

## 1. Try the starter

Use your existing GitHub SSH and Python setup. Mac students use Terminal; Windows students use the class Ubuntu/WSL terminal. Check `python3 --version`: expect **Python 3.12.x**. If different, use [Python help](https://kaw393939.github.io/218_spec/setup.html#python-version) before creating the environment.

On [the starter](https://github.com/kaw393939/is218-rps-starter), choose **Use this template → Create a new repository**. Use your account, name it `my-rps`, choose **Public**, leave **Include all branches** off, and leave the optional Copilot prompt blank.

In your projects folder, replace `YOUR-USERNAME` below. If you chose another repository name, replace `my-rps` too.

```sh
git clone git@github.com:YOUR-USERNAME/my-rps.git
cd my-rps
git remote -v
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python run.py
```

The remote should name **your copy** using `git@github.com:` for fetch and push. Open **http://127.0.0.1:5050**. Click a move: expect both choices and **“Starter: game rules not built yet.”** A missing winner is the task, not a failed setup. Leave this terminal running; code edits reload automatically.

**Checkpoint:** you can see the game and its unfinished notice. Stuck? [Setup help](https://kaw393939.github.io/218_spec/setup.html). Already have your copy? Keep it; do not create another.

## 2. Decide with your coding agent

In **ChatGPT desktop**, select **Codex** from the ChatGPT dropdown. Open your cloned folder with **⌘O on Mac / Ctrl+O on Windows**. Start a chat in that project, choose **Work in → This computer**, and leave **Worktree** off. On Windows, first follow the [one-time WSL app setup](https://kaw393939.github.io/218_spec/setup.html#windows-wsl).

Keep this one local chat for the exercise. Before asking AI, predict player **Rock** against computer **Paper** and say why. Then ask:

> Read AGENTS.md and SPEC.md. Explain RPS-001 and propose a short plan. Include valid and invalid cases, what to test as a unit, through a request, and in a real browser. Do not edit yet. Keep scoring for later.

Compare its answer with the nine-matchup table. A valid loss is a **positive** case; a missing or unsupported move is a **negative** case. Ask about anything you cannot explain. [Short introduction to the checks](https://kaw393939.github.io/218_spec/checks.html).

When you agree, ask:

> Save our agreed plan under “Agreed plan” in SPEC.md. Preserve the expected results. Do not edit the app yet.

Open **New tab → Terminal** in ChatGPT desktop. This terminal should be in your cloned folder. Keep using it for checks and Git:

```sh
pwd
cat SPEC.md
.venv/bin/python -m playwright install chromium
.venv/bin/python check.py
```

Confirm the path and saved plan. Chromium is a one-time test-browser download. Look for **PASS** at each check and **STARTER BASELINE ONLY**: these tests check the shell, not the missing rules. Resolve failures with [help](https://kaw393939.github.io/218_spec/setup.html) before continuing.

In **your GitHub repository → Issues → New issue**, create **“RPS-001: Play a round”**. Describe the scope and checks you agreed on; you can ask the agent for a short draft. Review before posting. Give its URL to the agent and ask it to put that link in **SPEC.md → Work record**.

**Checkpoint:** `SPEC.md` contains your agreed plan and issue link. No transfer between AI apps or manual code copying is needed.

## 3. Build and let AI check first

In the app's terminal:

```sh
git status --short --branch
git switch -c rps-001
```

Expect `## main...origin/main` and your intended `SPEC.md` edit. If the branch exists, use `git switch rps-001`.

In the **same AI chat**, ask:

> Compare our saved plan with the code and supplied fixtures. Explain conflicts or needed changes before editing; do not restart the whole plan. If it fits, implement RPS-001 and its agreed tests. Run .venv/bin/python check.py, review the diff against SPEC.md, and fix problems without weakening checks. Report actual results and remaining human checks. Do not commit or push.

Review file/command approval requests. The prepared checks use **Black** for formatting, **Pylint** for Python analysis, and **pytest** for behavior, including a small real-browser journey. The agent should add nine rule cases, a real request/result check, and a browser round with replay—not repeat every case through the browser.

**Checkpoint:** AI reports actual commands/results and what remains for you. Passing unchanged starter tests alone is not enough.

## 4. Check and give feedback

Refresh the local game, then choose a new move. Play several rounds. Do both choices and the result make sense? Can you play again? Try Tab and Enter too.

In the app's terminal:

```sh
.venv/bin/python check.py
git diff
cat tests/test_game.py
```

Press `q` if Git opens a scrolling view. Find the assertion for your predicted matchup and compare it with the spec. You can open files in the app with **⌘P / Ctrl+P**, or optionally inspect them in VS Code.

Tell the agent what you actually did and saw. For a mismatch, describe the action, expected result, and observed result; ask for a focused fix and retest. [Worked failure example](https://kaw393939.github.io/218_spec/checks.html#when-a-check-fails) shows how.

During fixes, `.venv/bin/python check.py --fast` skips the browser. Use the full command before review and the PR. For formatting, `.venv/bin/python -m black *.py tests` applies the shared style; inspect its edits. Do not remove meaningful assertions or disable checks just to pass.

Ask the agent to replace starter status in **SPEC.md → Work record** with actual checks, your browser observations, and real code/test links. Preserve the plan and issue. Do not record checks nobody performed.

**Checkpoint:** you can connect one requirement to its code and a meaningful test. You have tried the result yourself.

## 5. Keep the reviewed change

Expect `game.py`, `tests/test_game.py`, `tests/e2e/test_round.py`, and `SPEC.md`. Ask about other changed files before keeping them.

```sh
git add game.py tests/test_game.py tests/e2e/test_round.py SPEC.md
git diff --cached
git commit -m "RPS-001: play a round"
git push -u origin rps-001
```

In **your GitHub repository → Pull requests → New pull request**, use base `main` and compare `rps-001`. Describe the result and actual checks; add **`Closes #N`** with your issue number. In **Files changed**, verify the added tests use real rules rather than just the supplied stubs. Wait for **Python checks** to pass, then merge when it matches the spec.

**Done:** the game works locally, the PR is merged, its issue is closed, and the spec links to code and actual checks. Stop your server with Ctrl+C. No website deployment or extra reflection document is required.

**Next, with less guidance:** [RPS-002: first to two wins](NEXT.md). Write your own short request and test plan. Keep it in a separate issue/PR. Optional: personalize your game after the rules work.
