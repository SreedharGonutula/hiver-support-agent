# Hiver Support Agent

AI customer-support agent for the Hiver SDE Intern take-home assignment.

## Dataset
Customer Support on Twitter (Kaggle, `thoughtvector/customer-support-on-twitter`).
The raw `twcs.csv` is not committed to this repository.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/ingest.py --csv data/raw/twcs.csv --brand AppleSupport --sample-size 20000
```

The remaining pipeline will add thread reconstruction, intent classification,
historical-resolution retrieval, reply generation, escalation policy,
baselines, and evaluation.
