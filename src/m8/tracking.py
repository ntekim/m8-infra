"""Start a tracked run and append a pre-filled entry to the experiment log.

Usage:
    from m8.tracking import start_run
    run = start_run(
        name="coach-v0-lora-r16",
        hypothesis="LoRA on 500 sessions beats the prompted baseline on no-answer-leaking.",
        config={"base_model": "<model>", "lora_r": 16, "lr": 2e-4, "epochs": 2},
        dataset_path="data/sessions_v3.jsonl",
    )
    ...train, call run.log({...})...
    run.finish()
"""
import datetime
import hashlib
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
LOG = ROOT / "docs" / "EXPERIMENT_LOG.md"


def _git(*args):
    try:
        return subprocess.check_output(
            ["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "unknown"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def start_run(name, hypothesis, config, dataset_path=None, project="m8", use_wandb=True):
    commit = _git("rev-parse", "--short", "HEAD")
    status = _git("status", "--porcelain")
    dirty = status not in ("", "unknown")
    dataset_hash = _sha256(dataset_path) if dataset_path else None

    meta = {
        "git_commit": commit,
        "git_dirty": dirty,
        "dataset": dataset_path,
        "dataset_sha": dataset_hash,
    }

    run, link = None, ""
    if use_wandb:
        import wandb

        run = wandb.init(project=project, name=name, config={**config, **meta})
        link = run.url

    dirty_note = " (UNCOMMITTED CHANGES)" if dirty else ""
    entry = f"""
---

## {datetime.date.today()} · {name}
**Status:** running
**Hypothesis:** {hypothesis}
**Setup:** {config}
**Data:** {dataset_path} (sha {dataset_hash})
**Code:** {commit}{dirty_note}
**Run link:** {link}
**Baseline to beat:** 
**Result:** 
**What I saw in the outputs:** 
**Conclusion:** 
**Next:** 
"""
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(entry)
    return run
