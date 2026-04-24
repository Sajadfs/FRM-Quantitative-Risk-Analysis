# FRM-Quantitative-Risk-Analysis
# Central Limit Theorem in Financial Risk Management

### Objective
This project visualizes the **Central Limit Theorem (CLT)** within the context of **Operational Risk**. It proves that while individual loss events (e.g., fraud, system failures) follow a highly skewed distribution (Lognormal), the **average loss** over a large number of events converges to a **Normal Distribution**.

### Why this matters for Risk Managers?
As a Model Validator or Risk Analyst, understanding CLT is crucial because:
- It justifies the use of **Parametric VaR** for large portfolios.
- It helps determine the required sample size ($n \ge 30$) for statistical significance.
- It highlights why small samples ($n < 30$) require the use of **Student's t-distribution** instead of Normal.
> [!IMPORTANT]
> **A Critical Note on CLT and Tail Risk:** > While CLT justifies the use of Normal-based models for aggregating risks, a professional Risk Analyst must remain cautious. CLT focuses on the **convergence of the mean**, but in Financial Risk, we are primarily concerned with the **Tails** (Extreme Events). 
> In reality, financial data often exhibits **Fat Tails (Excess Kurtosis)**, and CLT may underestimate risk during market crashes. This project serves as a foundational exercise, but for robust risk management, one should also consider **Extreme Value Theory (EVT)** or **Stress Testing**.

### Methodology
1. **Population**: Generated 10,000 synthetic loss events using a **Lognormal Distribution**.
2. **Sampling**: Conducted 1,000 iterations of random sampling for $n \in \{2, 10, 30, 100\}$.
3. **Visualization**: Plotted the sampling distribution of the mean against a theoretical Normal curve.

### Results
The plots clearly show that as the sample size $n$ increases, the **Skewness** of the average loss decreases and the distribution becomes symmetrical (Gaussian), proving the CLT's validity for risk aggregation.
