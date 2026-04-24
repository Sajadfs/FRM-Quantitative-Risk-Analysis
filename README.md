# FRM-Quantitative-Risk-Analysis
# Central Limit Theorem in Financial Risk Management

### Objective
This project visualizes the **Central Limit Theorem (CLT)** within the context of **Operational Risk**. It proves that while individual loss events (e.g., fraud, system failures) follow a highly skewed distribution (Lognormal), the **average loss** over a large number of events converges to a **Normal Distribution**.

### Why this matters for Risk Managers?
As a Model Validator or Risk Analyst, understanding CLT is crucial because:
- It justifies the use of **Parametric VaR** for large portfolios.
- It helps determine the required sample size ($n \ge 30$) for statistical significance.
- It highlights why small samples ($n < 30$) require the use of **Student's t-distribution** instead of Normal.

### Methodology
1. **Population**: Generated 10,000 synthetic loss events using a **Lognormal Distribution**.
2. **Sampling**: Conducted 1,000 iterations of random sampling for $n \in \{2, 10, 30, 100\}$.
3. **Visualization**: Plotted the sampling distribution of the mean against a theoretical Normal curve.

### Results
The plots clearly show that as the sample size $n$ increases, the **Skewness** of the average loss decreases and the distribution becomes symmetrical (Gaussian), proving the CLT's validity for risk aggregation.
