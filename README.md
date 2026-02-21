# Kalpi Trade Engine

A broker-agnostic trade execution engine designed to make automated trading strategies reliable and portable across brokers.

While building my own trading strategies, I realized most failures were not in signal generation — but during order execution.  
Different brokers require different request formats, retries, and response handling.  
To solve this, I separated execution into its own independent layer instead of coupling it with strategy logic.

---

## What it does
- validates trade orders
- converts request into broker-specific format
- sends execution requests
- handles failure & retry logic
- stores execution response logs

---

## Why this project
In automated trading systems, strategy logic usually stays simple — but execution logic becomes messy very quickly, especially when:

- switching brokers
- debugging rejected orders
- handling network failures
- managing retries

Instead of rewriting execution code for every strategy, this project provides a reusable execution layer that sits between strategy and broker API.

---

## Architecture
Strategy → Execution Engine → Broker Interface

- Strategy generates signals only
- Engine guarantees order reliability
- Broker adapters only translate format

---

## Current Support
- Zerodha (basic adapter structure)
- Easily extendable to other brokers

---

## Tech Stack
- Python
- FastAPI
- Modular adapter architecture

---

## Future Work
- async order execution
- multi-broker fallback routing
- paper trading simulator
- latency measurement logs

---

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open API docs: http://127.0.0.1:8000/docs


