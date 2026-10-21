# M8

A real-time, context-aware AI companion ("mate"). This repo holds the ML work: data, evals, training, and experiment tracking.

## Layout

```
docs/EXPERIMENT_LOG.md   # the "why" behind every run (write the hypothesis BEFORE you run)
src/m8/tracking.py       # starts a tracked run and appends a pre-filled log entry
data/                    # datasets (JSONL). Large files are git-ignored
evals/                   # eval scenarios and rubrics
configs/                 # training configs
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .                                     # makes `import m8` work
wandb login                                          # paste your API key once
git init && git add . && git commit -m "Initial M8 repo"
```

## Workflow for every experiment

1. Write the hypothesis in `docs/EXPERIMENT_LOG.md` (or let `start_run` pre-fill it).
2. Run training with tracking on (`start_run(...)`, or `report_to="wandb"` in TRL/Transformers).
3. Paste the W&B run link and the result into the log entry.
4. Write what you conclude and what you'll try next.
5. Commit the log with the code that produced the result.
# m8-infra
