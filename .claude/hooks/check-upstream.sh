#!/usr/bin/env bash
# SessionStart hook: report how this checkout stands relative to origin/main.
#
# The catalogue is refreshed by a scheduled GitHub Actions job, so the remote
# moves on its own with nothing happening locally. Starting work on a stale
# tree means grepping register metadata that Statistics Finland has already
# superseded — the exact failure this archive exists to prevent.
#
# Every outcome is reported, including "up to date". Silence used to mean both
# "in sync" and "the check never ran" — an offline laptop read as an all-clear,
# which is precisely the failure this guards against.
#
# Reports only; never touches the working tree. Always exits 0, so a network
# problem can never block a session.

set -u

# Prefer the harness-provided root; fall back to this script's own location
# (.claude/hooks/ -> repo root) so cwd does not matter.
repo="${CLAUDE_PROJECT_DIR:-}"
if [ -z "$repo" ]; then
  repo="$(cd "$(dirname "$0")/../.." 2>/dev/null && pwd)" || exit 0
fi
cd "$repo" 2>/dev/null || exit 0

# Not a git checkout: nothing meaningful to say, so say nothing.
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

# The remote could not be consulted. Distinct from "up to date" on purpose.
unreachable() {
  echo "Taika mirror: could not reach origin — freshness unknown, datasets/ and withdrawn/ may be stale."
  exit 0
}

# Never let a credential prompt or a dead network hang session startup.
export GIT_TERMINAL_PROMPT=0
if command -v timeout >/dev/null 2>&1; then
  timeout 10 git fetch --quiet origin main >/dev/null 2>&1 || unreachable
else
  git fetch --quiet origin main >/dev/null 2>&1 || unreachable
fi

git rev-parse --verify --quiet origin/main >/dev/null 2>&1 || unreachable

behind=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
ahead=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)

if [ "$behind" -eq 0 ]; then
  tip=$(git log -1 --format='%h, %ad' --date=short origin/main 2>/dev/null)
  [ -n "$tip" ] && tip=" ($tip)"
  if [ "$ahead" -gt 0 ]; then
    s=""
    [ "$ahead" -ne 1 ] && s="s"
    echo "Taika mirror: up to date with origin/main${tip}; ${ahead} local commit${s} not pushed."
  else
    echo "Taika mirror: up to date with origin/main${tip}."
  fi
  exit 0
fi

s=""
[ "$behind" -ne 1 ] && s="s"

if [ "$ahead" -gt 0 ]; then
  echo "NOTE: this checkout has DIVERGED from origin/main — ${behind} commit${s} behind, ${ahead} ahead."
  echo "The scheduled Taika refresh has pushed upstream. Reconcile before relying on datasets/ or withdrawn/ being current."
else
  echo "NOTE: this checkout is ${behind} commit${s} behind origin/main."
  echo "The scheduled Taika refresh has updated the mirror. Run 'git pull --ff-only' before reading or grepping datasets/ or withdrawn/, so register metadata is current."
fi

exit 0
