This folder shows the reference structure of one task in this project.

Acceptance rules for every task folder that lives under tasks/<developer>/:

1. A task is considered implemented only if its folder contains at least 5 files
   in total, and both docs/task.md and evaluation/main.py are among those files.
   Folders with 4 or fewer files, or folders missing either of the two core
   files, are still implementing.

2. docs/task.md must be non-empty and must contain English text only. A task
   whose docs/task.md is empty or contains any Chinese character does not count
   as implemented, no matter how many files its folder has.

3. Except for the docs/task.md content rule above, only the existence of files
   matters; the content of the other files is never checked.

This reference folder itself holds 8 files and shows the recommended layout.
A folder with all 8 files is implemented, and so is any folder that keeps at
least 5 files while still including docs/task.md and evaluation/main.py.
