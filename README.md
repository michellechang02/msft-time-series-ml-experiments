# Time-Series ML Ensemble Learning: Evaluation Rigor & Responsible Experimentation

**FHL Project Theme**: *Changing how we work in the era of AI*

## Overview

This project demonstrates rigorous evaluation practices and responsible experimentation in machine learning applied to time-series forecasting. Using public historical Microsoft stock data, we explore ensemble modeling techniques while emphasizing transparency, reproducibility, and awareness of real-world constraints such as transaction costs and modeling assumptions.

In the era of AI, this work exemplifies how we should approach ML experimentation with scientific rigor, acknowledging both the potential and limitations of predictive models.

## Project Objectives

Explore time-series machine learning techniques using public historical data to study:
- **Feature Engineering**: Creation and evaluation of technical indicators
- **Ensemble Modeling**: Combination of multiple ML algorithms for improved predictions
- **Evaluation Rigor**: Comprehensive performance assessment including transaction costs
- **Responsible Experimentation**: Transparent methodology and clear limitations

### Key Parameters
- **Prediction Horizon**: 5 days ahead
- **Data Source**: Public historical MSFT price data
- **Frequency**: Daily
- **Cost Assumption**: 5 basis points (bps) per position change
- **Positioning**: Long-only (for simplicity and interpretability)

> **Important Note**: This notebook is a learning and evaluation exercise. It is **not** intended as a trading system or investment recommendation.

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
The project demonstrates best practices in ML evaluation:

#### Data Integrity
- **Lookahead Prevention**: Features are shifted to prevent data leakage
- **Clean Train/Val/Test Split**: 60% train, 20% validation, 20% test
- **Proper Scaling**: StandardScaler fitted only on training data

#### Performance Metrics
- **Accuracy**: Classification performance on directional predictions
- **Sharpe Ratio**: Risk-adjusted returns including transaction costs
- **Annual Return**: Annualized performance metrics
- **Volatility**: Strategy risk measurement
- **Maximum Drawdown**: Worst peak-to-trough decline
- **Transaction Count**: Trading frequency analysis

#### Cost Sensitivity Analysis
The notebook evaluates performance across multiple cost assumptions:
- 5 bps (0.05%)
- 10 bps (0.10%)
- 20 bps (0.20%)

This demonstrates how transaction costs significantly impact strategy viability.

### 4. Responsible AI Practices

This project embodies responsible experimentation in the AI era:

✅ **Transparency**: All code, assumptions, and limitations are clearly documented

✅ **Reproducibility**: Fixed random seeds and clear data processing steps

✅ **Reality-Grounded**: Includes transaction costs and real-world constraints

✅ **Honest Evaluation**: Out-of-sample testing with no data leakage

✅ **Clear Disclaimers**: Explicitly states this is not investment advice

✅ **Interpretability**: Uses explainable features and simple ensemble methods

## Project Structure

```
msft-time-series-ml-experiments/
├── README.md                                    # This file (FHL documentation)
└── time_series_ml_ensemble_learning.ipynb      # Main Jupyter notebook
```

## Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook or Google Colab
- Required libraries:
  - numpy
  - pandas
  - matplotlib
  - scikit-learn

### Running the Notebook

1. **Data**: The notebook expects a `Microsoft.csv` file with historical MSFT stock data
   - Required columns: Date, Open, High, Low, Close, Adj Close, Volume

2. **Execution**: Run cells sequentially from top to bottom
   - Data loading and preprocessing
   - Feature engineering
   - Model training
   - Evaluation and visualization

3. **Outputs**: 
   - Performance metrics (Sharpe ratio, returns, drawdown)
   - Comparison charts (strategy vs. buy-and-hold)
   - Cost sensitivity analysis

## Key Findings

The notebook demonstrates that:

1. **Ensemble methods** can capture patterns in time-series data
2. **Transaction costs** significantly impact strategy performance
3. **Rigorous evaluation** is essential for honest assessment
4. **Feature engineering** plays a crucial role in model quality
5. **Out-of-sample testing** reveals true generalization capability

### Performance Visualization

The following chart shows the out-of-sample performance comparison between the ensemble model strategy and a simple buy-and-hold baseline:

![Out-of-Sample Model Signal vs Baseline](https://github.com/user-attachments/assets/929ca546-7be9-4aeb-ab2a-9606fe132e7c)

This visualization demonstrates the model's ability to generate signals that outperform the baseline strategy over the test period, while accounting for transaction costs and maintaining rigorous evaluation standards.

## FHL Theme: Changing How We Work in the Era of AI

This project reflects the changing landscape of work in the AI era in several ways:

### 1. **Rigorous Methodology Over Quick Results**
In an era where AI can generate predictions rapidly, this project emphasizes the importance of:
- Careful evaluation procedures
- Understanding model limitations
- Accounting for real-world constraints

### 2. **Transparent and Reproducible Science**
As AI becomes more prevalent, transparency becomes critical:
- Clear documentation of all steps
- Explicit statement of assumptions
- Reproducible experimental setup

### 3. **Responsible AI Development**
The project models responsible AI practices:
- Honest evaluation with proper train/test splits
- Acknowledgment of limitations
- Clear ethical boundaries (not investment advice)

### 4. **Human-Centered AI**
Rather than black-box prediction, the approach prioritizes:
- Interpretable features
- Explainable model choices
- Clear communication of results and limitations

### 5. **Learning and Education Focus**
This is explicitly positioned as a learning exercise, demonstrating how AI should be used for:
- Skill development
- Understanding methodologies
- Building expertise responsibly

## Limitations and Future Work

### Current Limitations
- Single-asset focus (MSFT only)
- Long-only strategy (no shorting)
- Daily frequency (no intraday data)
- Limited feature set
- Historical backtesting (not live trading)

### Future Enhancements
- **Multi-asset portfolios**: Expand to sector or market-wide analysis
- **Advanced features**: Include alternative data sources
- **Deep learning**: Explore neural network architectures (LSTM, Transformers)
- **Risk management**: Implement dynamic position sizing and stop-losses
- **Regime detection**: Identify market conditions and adapt strategies
- **Explainability tools**: Add SHAP values or feature importance analysis

## Contributing

This is a learning and research project. Contributions that enhance:
- Evaluation rigor
- Documentation clarity
- Responsible AI practices
- Educational value

are welcome.

## Disclaimer

**This project is for educational and research purposes only.**

- This is NOT investment advice
- This is NOT a trading system
- Past performance does not guarantee future results
- Financial markets involve significant risk
- Consult qualified professionals before making investment decisions

## License

This project is provided as-is for educational purposes.

---

**Project Type**: FHL (Future of Human Learning) Research Project  
**Focus Area**: Time-Series ML, Ensemble Learning, Responsible AI  
**Theme**: Changing how we work in the era of AI  
**Status**: Educational Exercise - Not for Production Use
