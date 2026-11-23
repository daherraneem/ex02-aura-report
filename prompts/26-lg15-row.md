# 26 – Accurate LG-15 / LG-11 Row

**Author:** Raneem · **Agent:** Claude Code · **Date:** 2026-11-23

## Prompt

```
Make the LG-15/LG-11 row accurate: there was one prompt-numbering clash, fixed by renaming,
and some commit messages were longer than the rule; we did not update the rule files because
the work was finished. Commit and push as a minor change. Do not move the tag.
```

## What the agent did

- Ran `git pull` (up to date).
- Rewrote the reason in the README's LG-15 / LG-11 row: one prompt-numbering clash, fixed by
  renaming; some commit messages longer than the rule; rule files not updated because the
  work was finished.
- Added a Progress Log line, committed as a minor change and pushed. The tag
  `submission-ex02` was not moved.

## What was corrected

- The previous wording ("the rules themselves were followed in practice") was not accurate:
  the committee had found one numbering clash (LG-15) and long commit messages (LG-11).
