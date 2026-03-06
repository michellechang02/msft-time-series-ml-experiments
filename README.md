# Time-Series ML Ensemble Learning: Evaluation Rigor & Responsible Experimentation
**FHL Project Theme:** *Changing how we work in the era of AI*

---

## Overview
This project demonstrates **rigorous evaluation practices** and **responsible experimentation** in machine learning applied to time-series forecasting. Using **public historical Microsoft (MSFT) stock data**, we explore ensemble modeling techniques while emphasizing **transparency, reproducibility, and real‑world constraints** such as transaction costs and modeling assumptions.

In the era of AI, this work exemplifies how ML experimentation should be approached with **scientific rigor**, explicitly acknowledging both the **potential** and **limitations** of predictive models.

---

## Project Objectives
Explore time-series machine learning techniques using public historical data to study:

- **Feature Engineering**: Creation and evaluation of technical indicators
- **Ensemble Modeling**: Combination of multiple ML algorithms for improved predictions
- **Evaluation Rigor**: Comprehensive performance assessment including transaction costs
- **Responsible Experimentation**: Transparent methodology and clearly stated limitations

---

## Key Parameters
- **Prediction Horizon**: 5 days ahead
- **Data Source**: Public historical MSFT price data
- **Frequency**: Daily
- **Cost Assumption**: 5 basis points (bps) per position change
- **Positioning**: Long-only (for simplicity and interpretability)

> **Important Note**  
> This project is a learning and evaluation exercise. It is **not** intended as a trading system or investment recommendation.

---

## Methodology

### 1. Feature Engineering
The project employs multiple feature categories to capture different market dynamics:

- **Returns**: 1-day, 5-day, and 10-day percentage changes
- **Volatility**: 20-day rolling standard deviation of returns
- **Momentum**: 10-day and 20-day price momentum indicators
- **Moving Averages**: 10-day and 20-day MA with ratio calculations
- **Intraday Structure**: Daily range and close-to-open relationships
- **Volume Analysis**: Volume z-score relative to 20-day statistics

### 2. Ensemble Learning Approach
Multiple classification algorithms are trained and combined:

- Logistic Regression (linear baseline)
- Random Forest Classifier (tree-based ensemble)
- Gradient Boosting Classifier (sequential ensemble)

### 3. Rigorous Evaluation
The project demonstrates best practices in ML evaluation.

**Data Integrity**
- Lookahead Prevention: Features are shifted to prevent data leakage
- Clean Train/Validation/Test Split: 60% / 20% / 20%
- Proper Scaling: `StandardScaler` fitted only on training data

**Performance Metrics**
- Accuracy (directional prediction)
- Sharpe Ratio (risk-adjusted returns including transaction costs)
- Annual Return
- Volatility
- Maximum Drawdown
- Transaction Count

**Cost Sensitivity Analysis**
Performance is evaluated across multiple transaction cost assumptions:
- 5 bps (0.05%)
- 10 bps (0.10%)
- 20 bps (0.20%)

---

## Responsible AI Practices
✅ Transparency · ✅ Reproducibility · ✅ Reality‑Grounded · ✅ Honest Evaluation · ✅ Interpretability

---

## Project Structure
```
msft-time-series-ml-experiments/
├── README.md
├── Microsoft.csv
├── requirements.txt
├── run_notebook.py
├── time_series_ml_ensemble_learning.ipynb
└── outputs/
```

---

## Running the Project

```bash
pip install -r requirements.txt
python run_notebook.py
```

---

## Disclaimer
This project is for **educational and research purposes only**.

- This is **NOT** investment advice
- This is **NOT** a trading system
- Past performance does not guarantee future results
