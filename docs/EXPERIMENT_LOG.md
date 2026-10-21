# M8 Experiment Log

The tracker (W&B/MLflow) records **what happened**. This file records **why you tried it and what you concluded**.

**Rules**
- Write the **hypothesis before the run**, never after. It stops you rationalizing results.
- Name runs by what changed (`coach-v0-lora-r16`), never `run-7`.
- Paste the **run link** so this log is the index and the tracker is the evidence.
- Record failures. They are the most valuable entries.
- Newest entries go at the bottom.

---

## Template (copy for each experiment)

```
## YYYY-MM-DD · run-name
**Status:** planned | running | done | abandoned
**Hypothesis:** If I [change], then [metric] will [improve/stay/drop] because [reason].
**Setup:** base model, method (SFT/LoRA/DPO), key hyperparameters
**Data:** dataset name + version/hash, size, what changed vs. last time
**Code:** git commit
**Run link:** 
**Baseline to beat:** 
**Result:** numbers (loss, rubric score, held-out case score, latency)
**What I saw in the outputs:** (read samples by hand; note patterns)
**Conclusion:** hypothesis confirmed / rejected / unclear, and why
**Next:** 
```

---

## 0000-00-00 · example-entry (delete me)
**Status:** done
**Hypothesis:** If I LoRA-tune a small instruct model on 500 coaching sessions, then the "no answer leaking" rubric score will beat the prompted baseline because the model sees the hint-ladder pattern.
**Setup:** <base-model>, LoRA r=16, lr 2e-4, 2 epochs
**Data:** sessions_v3, 500 sessions, added 100 code-walkthrough cases
**Code:** a1b2c3d
**Run link:** (W&B URL)
**Baseline to beat:** prompted baseline, rubric 3.4
**Result:** rubric 3.9 overall, but leaking worse on code cases
**What I saw in the outputs:** in code sessions the assistant gives the fix in turn 2
**Conclusion:** partly confirmed; training data for code cases leaks answers too early
**Next:** rewrite 40 code sessions, retrain as coach-v0-lora-r16-b
