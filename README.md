# Kalpi Trade Engine

I built this while trying to run my own trading strategies and realized most failures were happening during order placement rather than signal logic.

Different brokers required different request formats, retry handling and response parsing, so I separated execution into its own layer instead of coupling it with strategy code.


## What it does
- validates trade order
- converts request into broker specific format
- sends execution request
- handles failure & retry
- stores execution response logs


## Why this project
While testing strategies I noticed strategy code stays simple but execution logic becomes messy very quickly — especially when switching brokers or debugging failed orders.

So instead of rewriting execution every time, I designed a small execution engine that sits between strategy and broker API.


## Architecture
Strategy → Execution Engine → Broker Interface

The strategy only generates signals.
The engine handles order reliability.
Broker adapters only translate format.


## Current Support
- Zerodha (basic adapter structure)
- Easily extendable for other brokers


## Tech
Python, FastAPI structure, modular adapters


## Future Work
- async order execution
- multiple broker fallback
- paper trading simulator
- latency measurement logs
