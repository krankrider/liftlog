# Lift log

A personal workout-logging PWA for iPhone. One HTML file, no build step, no dependencies.
It replaces the paper training-log pages of the "Max-Efficiency Hypertrophy Program"
(original v3 PDF in `docs/`, current v5 revision with reasoning in `docs/program.md`).

Owner: Rokas (GitHub `krankrider`). Started 2026-10-01 with Claude Code; continued from a
personal account. Read `CLAUDE.md` before changing anything.

## What it does

- Home shows "Start <next session>" based on the last logged session (Upper A → Lower A →
  Upper B → Lower B), the other three sessions, number tiles, a month calendar, trophies and
  the history list. History shows the last 6 sessions, with "Show all" for the rest. Dates
  read "Wed 7 Oct", with the year only when it is not this year.
- A session started today stays open until Done: the big button says "Continue Upper A" instead
  of "Start <next>". If a set was rated in the last 30 minutes, the app opens straight on that
  session, because iOS often closes a home-screen app in the background mid-workout.
- A session left with nothing rated, no bodyweight and no note is deleted when home shows, so a
  mistapped Start or a look at the weights leaves no trace on the calendar or the rotation.
- The calendar starts on Monday. A trained day is a white circle with the session's letters
  under it (UA = Upper A); tapping it opens that session. Today has a ring. ‹ › change month.
- A session is the program's exercise list with one row per set: weight stepper (±2.5 kg),
  reps stepper (±1), both open the numeric keypad when tapped, and a row of RIR chips 0–4+.
  Tapping a chip marks the set done and fills its number white. An unrated set is not counted
  anywhere. Date and bodyweight sit at the bottom with the notes, so a session opens on the
  first lift. The line under each exercise reads "Last time, Thu 1 Oct: 70 kg × 8, 8, 8 · RIR 1, 1, 1".
- Weight and reps are prefilled from the last time that exercise was done, so a repeat set is
  one tap. If every set hit the top of the rep range last time, the weight prefills 2.5 kg
  heavier, reps at the bottom of the range, and the badge says "+2.5 kg". The same happens
  when every set was rated RIR 3 or 4+ ("every set felt easy"). This is the program's
  double-progression rule. If a set fell under the range, it shows a "below range" badge and
  keeps the weight; if that happens two sessions in a row at the same weight, the weight
  prefills about 10% lighter (rounded to 2.5 kg, at least 2.5 off), reps at the bottom, and
  the badge says how much. Deload sessions keep the weight and show the old "add weight" text.
- A rated set that beats the exercise's record (more reps than ever at that weight or heavier,
  counting earlier sets today) gets the trophy ring on its number and "Best" in place of the
  RIR label, so the row keeps its height. Never on the first time an exercise is logged, or
  every set would be one.
- Done shows a summary of today's session: minutes, new bests, which exercises get +2.5 kg next
  time, how the week stands, and any trophy this session earned. Earlier sessions and empty
  ones go straight home.
- Home tiles: this week's sessions out of 4, full weeks in a row (Monday to Sunday, all 4
  sessions; deload weeks count when trained; this week counts once it is full), bodyweight
  and total lifted.
- Trophies on home, black-and-white medals, solid when earned with the date, outlined with
  what is left when not. Home shows the earned ones and the 4 closest to earn; "Show all"
  lists the rest. The trophies: 1/10/25/50/100 sessions; 4/12/26 full weeks in a row; 1/10/25
  weight jumps earned (an exercise that hit the add-weight rule); plate clubs for 5+ reps
  (bench 60/100, squat 100/140, trap bar 140/180, overhead press 60); a deload week taken
  after at least 4 weeks of training. All worked out from history, nothing extra saved.
- The first lift of each session shows its warm-up under the "last ..." line, worked out from
  set 1's weight: bar ×10, 50% ×5, 70% ×3, 85% ×1, rounded to 2.5 kg.
- In a session the header shows the minutes since the first rated set (today only). It stops
  at the last rated set once nothing has been rated for 30 minutes.
- Rating a set starts a rest timer at the bottom of the screen: first heavy compound 3 min,
  other compounds 2 min, isolation 90 s (from the v3 PDF; per exercise in
  PROGRAM). A1 of a superset goes straight to A2: the card says "No rest" and "Superset: straight
  to ..." instead of counting down. That only happens while A2 is behind A1, so logging A2 first
  still gives a normal rest. While it runs it shows the next exercise (with its superset tag) and
  set, with that exercise's cues from the PDF's exercise guide (the TIPS table). It slides up
  from the bottom and leaves the same way (a fade with Reduce Motion on). At zero it eases to
  white and says Go. Skip closes it. Re-rating a set does not restart it.
- The set to log next has a white outline: right after a rating, the set the rest card names;
  on opening today's session, the set after the first exercise with an open set (so a superset
  resumes on the half that is behind). If it is off screen the page scrolls it into view between
  the header and the rest card; otherwise nothing moves. Re-rating a set moves nothing.
- Tapping the "last ..." line under an exercise opens its last 8 sessions.
- Bodyweight and a notes field per session. Everything autosaves on each tap.
- The bodyweight tile is the average of the last 7 days and the change on the 7 days before.
- Deload: home counts the weeks since you started or since the last deload, and says
  "Deload week due" from week 6. "Start deload" on that line (two taps) makes the next 7 days a deload:
  new sessions get about 60% of the sets (3 → 2, 4 → 2, 2 → 1) at the same weights, the header
  says Deload, and those sessions are left out of the badges and prefill.
- Delete a session by swiping its history row left and tapping Delete (no confirm, no undo,
  like iOS Mail). Inside a session, "Delete session" at the bottom does the same with two taps.
- Black-and-white Liquid Glass look, following Apple's guidance: glass only on the floating
  controls (back button, Export, Start, Done, the chosen RIR), content on plain dark cards.
  No colour anywhere; the add-weight badge is solid white, the below-range one outlined. Safari cannot
  bend light on a web page, so the glass is blur, tint and highlights. Presses show at once
  (Safari on iPhone needs a touchstart listener for that), and the steppers and RIR chips
  carry VoiceOver labels.
- Export sends a JSON backup to the iOS share sheet. Import merges a backup by session id.
- Installs to the home screen, runs full screen, works offline after the first load, and
  updates itself on the home screen after a push.

## Files

| File | Purpose |
|---|---|
| `index.html` | Everything: CSS, the PROGRAM and TIPS tables, logic, self-tests (`#test`) |
| `sw.js` | Offline cache, stale-while-revalidate. **Bump `V` on every change** |
| `manifest.webmanifest` | PWA manifest |
| `icon-180.png`, `icon-512.png` | App icons, generated by `tools/make_icons.py` (stdlib only) |
| `tools/phone.html` | Frames the app at a true 390 px iPhone width for headless screenshots |
| `docs/program.md` | The v5 program, principles, and why it differs from v3 and v4 |
| `docs/hypertrophy-program-v3.pdf` | The original program with the exercise guide |
| `CLAUDE.md` | Working rules for an AI agent on this repo |

## Run locally

```sh
python3 -m http.server 8123
# app:        http://localhost:8123/
# self-check: http://localhost:8123/#test
```

`#test` renders PASS/FAIL lines for the progression, prefill and rest-timer logic above a sample
Upper A session with the rest timer showing. It never touches saved data. The service worker caches aggressively: after editing,
either bump `V` in `sw.js`, use a private window, or unregister the worker in DevTools.

Headless layout check at iPhone width. Headless Chromium lays pages out at about 480 px minimum
whatever `--window-size` says, so load the app through `tools/phone.html`, which frames it at
390 px. Use a fresh profile so the worker cache cannot serve a stale copy:

```sh
chrome --headless=new --disable-gpu --user-data-dir=/tmp/fresh --virtual-time-budget=4000 \
  --hide-scrollbars --force-device-scale-factor=2 --window-size=390,1800 \
  --screenshot=/tmp/shot.png "http://localhost:8123/tools/phone.html#test"
```

The self-check's last line must read `viewport 390px`. Drop `#test` to see the home screen.

On Windows the binary is `msedge.exe` under `C:\Program Files (x86)\Microsoft\Edge\Application\`.

## Deploy

Hosted on Vercel (Hobby plan) from this private repo. Framework "Other", no build command, no
output directory. Push to `main` and Vercel redeploys.

Production URL: https://liftlog-lilac.vercel.app/

Vercel Hobby deploys private repos as long as they belong to a personal GitHub account, which
is why Vercel was chosen over GitHub Pages (free Pages needs a public repo).

## Update procedure

1. Edit `index.html` (or manifest/icons).
2. Bump `V` in `sw.js` (`liftlog-v1` → `liftlog-v2`).
3. Open `#test`, all lines PASS. Add a line in `runTests()` for any new logic.
4. Commit, push. The app checks for a new version every time it comes back on screen. When
   one has downloaded it reloads itself, but only on the home screen; an open session keeps
   the old copy until you go back home, so a reload never drops the session or the rest timer.

## Data model

localStorage key `liftlog`:

```json
{"sessions":[{"id":"mg9k2x1","date":"2026-10-01","name":"Upper A","bw":80.4,"note":"",
  "ex":{"Barbell Bench Press":[{"w":60,"r":8,"rir":1},{"w":60,"r":8,"rir":1},{"w":60,"r":7,"rir":0}]}}]}
```

- `rir` null means the set was not done. `w`/`r` null means not entered.
- `start` and `last` (ms timestamps) are the first and latest rated set, for the clock.
- `fin: true` marks a session closed with Done, so home stops offering to continue it.
- `deload: true` marks a deload session. Top-level `deload` is the first day of the latest
  deload week. Import keeps the later of the two.
- History lookup is by exact exercise name. Renaming an exercise in PROGRAM orphans its
  history unless a migration renames the keys in stored sessions too.
- A session created from an older program version keeps its own sets; exercises added later
  appear empty when the session is reopened.
- Exports are plain copies of this object. Import adds sessions whose id is not present.

## Install on iPhone

Open the production URL in Safari, Share, Add to Home Screen. Open it from the icon.

## Not built, deliberately

- Points, XP and levels: numbers that mean nothing. No trophy for total kilos lifted either,
  since that rewards junk volume. No daily streak: rest days are part of the program.
- Sound or vibration when the rest timer ends (iOS web apps cannot vibrate).
- Deload due when reps stall two weeks running. Only the 6-week count is built.
- Editing the program inside the app. Edit the PROGRAM table in `index.html` instead.
- Per-side exercises (split squat) log one line for both sides.
- The iOS numeric keypad has no Done key. Tapping a RIR chip dismisses it, which is the
  normal flow anyway.
