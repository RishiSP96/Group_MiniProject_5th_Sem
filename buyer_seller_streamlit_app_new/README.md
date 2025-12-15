# Buyer/Seller Streamlit App Suite

This repository contains a collection of Streamlit dashboards for market analysis, including:

- **Buyer/Seller Pressure Tool** (`buyer_seller_app.py`):
  - Fetches OHLCV data from Binance (via `ccxt`)
  - Computes normalized buyer/seller pressure curves
  - Generates BUY/SELL/FLAT signals and visualizes them
  - Optional Gemini AI analysis via `ai_module.py`

- **AI Market Dashboard** (within `buyer_seller_app.py` + `market_analysis_module.py`):
  - Combined footprint, volume profile, and technical indicator charts
  - Gemini AI-based market commentary

- **Crypto Dashboard** (`crypto_dashboard.py`):
  - CoinGecko-powered crypto heatmap, BTC dominance, market cap history, and live prices table

- **Market News Panel** (`market_news.py`):
  - RSS-based market news cards with simple sentiment placeholders

- **Quantum Wave Market Predictor** (`quantum_price_backend.py` + section in `buyer_seller_app.py`):
  - Experimental quantum-inspired probability field and signal generator for prices

- **Sentiment / Fear & Greed Dashboard** (`market_sentiment_module.py`):
  - Fear & Greed index visualization and simple market stats

## Installation

```bash
pip install -r requirements.txt
```

## Running the main app

From the project root:

```bash
streamlit run buyer_seller_app.py
```

Make sure to set a valid **Gemini API key** inside `ai_module.py` before using the AI features.

## Notes

- All data sources used are public/free (Binance, CoinGecko, RSS feeds, etc.).
- Some dashboards rely on real-time APIs; if requests fail, the app will show an error in the UI.
- This project is intended for educational and experimental purposes, **not** financial advice.
