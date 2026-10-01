# liftlog — agent notes

Personal project of the repo owner. Goal: the fastest possible set logging in the gym on an
iPhone, plus a per-set hardness rating (RIR) that drives the next session's weights. The
training goal is hypertrophy and looks; the program and its reasoning are in `docs/program.md`.
`README.md` explains the files, data model, test and deploy steps. Read both first.

## Rules

- One `index.html`, vanilla JS and CSS, no build, no npm, no frameworks, no CDN scripts.
  Tooling scripts use the Python standard library only. Keep it that way unless the owner asks.
- Every change to `index.html`, the manifest or the icons: bump `V` in `sw.js`, or phones keep
  the old copy. Then open `/#test` and make sure every line says PASS. New logic gets a test
  line in `runTests()`. Tests must never touch saved data (`noSave` is already there for this).
- Verify layout at 390 CSS px before calling UI work done. Headless Chromium lays pages out at
  about 480 px minimum; screenshot `tools/phone.html` as the README shows. Use a fresh profile
  directory or the service worker will serve the stale copy and hide your edit.
- Look (owner's decision, 2026-10-01): black and white only, no colour, Liquid Glass per Apple's guidance. Glass goes
  only on floating controls (header buttons, primary actions, the chosen RIR); content stays on
  plain cards. Do not spread glass onto content, add colour or bring back light mode without asking.
- The owner decides anything a user sees: wording, thresholds, program changes, new features.
  Propose in plain words, get a yes, then build. Do not add features "while at it".
- UI text: plain words a lifter understands. No statistics jargon. One idea per line.
- Prefer deletion over addition. The current feature set was chosen on purpose; the README
  lists what was skipped and why.

## Git and deploy

- Remote: `https://krankrider@github.com/krankrider/liftlog.git` (private, personal account).
  The username in the URL keeps credential managers from mixing this login with any other
  GitHub account on the machine. Commit identity is set repo-locally (krankrider / gmail).
- If pushing from inside VS Code's terminal picks the wrong GitHub account, run the push with
  the VS Code credential variables unset:
  `env -u GIT_ASKPASS -u VSCODE_GIT_ASKPASS_MAIN git push`.
- Pushing `main` deploys to Vercel. There is no staging; test locally first.
- Never commit exported training data (`liftlog-*.json` is ignored).

## Program data

The PROGRAM table at the top of `index.html` is the single source of truth for sessions,
sets, rep ranges, target RIR and superset tags. `docs/program.md` must be updated in the same
commit when it changes. Exercise names are the history keys; renaming one needs a migration.
