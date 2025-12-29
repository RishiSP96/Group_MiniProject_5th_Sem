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

## Configuration

### Setting up Gemini API Key (for AI features)

**IMPORTANT:** Never commit your API key to git! Use environment variables instead.

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your-actual-api-key-here
   ```

3. The `.env` file is already in `.gitignore` and won't be committed.

Alternatively, you can set it as an environment variable:
```bash
# On Windows (PowerShell)
$env:GEMINI_API_KEY="your-api-key-here"

# On Linux/Mac
export GEMINI_API_KEY="your-api-key-here"
```

## Running the main app

From the project root:

```bash
streamlit run buyer_seller_app.py
```

## Notes

- All data sources used are public/free (Binance, CoinGecko, RSS feeds, etc.).
- Some dashboards rely on real-time APIs; if requests fail, the app will show an error in the UI.
- This project is intended for educational and experimental purposes, **not** financial advice.

