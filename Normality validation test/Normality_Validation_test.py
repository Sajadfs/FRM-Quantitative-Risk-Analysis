#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:45:38 2026

@author: sajadadeli
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

"""
Project: Market Risk Model Validation: Jarque-Bera Normality Test
Objective: Validate the 'Normality Assumption' for Parametric VaR models.
"""
# 1. Generate Data
np.random.seed(42)
n_sample = 1000

# Benchmark: Perfectly Normal Data
normal_data = np.random.normal(loc=0, scale=1, size=n_sample)

# Real-world Proxy: Simulated Stock Returns (Student's t-dist with 5 degrees of freedom)
# This mimics the "Fat Tails" found in actual market data.
market_returns = np.random.standard_t(df=5, size=n_sample)

# 2. Perform Jarque Bera Test
# Null Hypothesis (H0): The data is normally distributed.
jb_stat_norm, p_val_norm = stats.jarque_bera(normal_data)
jb_stat_mkt, p_val_mkt = stats.jarque_bera(market_returns)

# 3. Visualization
plt.figure(figsize=(14,6))

# Subplot 1: Normal Distribution
plt.subplot(1,2,1)
plt.hist(normal_data, bins=50, alpha=0.7, density=True)
plt.title(f"Benchmark: Normal Distribution\nJB p-value: {p_val_norm:.4f}")
plt.xlabel("Returns")
plt.ylabel("Frequency")

# Subplot 2: Market Returns (Fat Tails)
plt.subplot(1, 2, 2)
plt.hist(market_returns, bins=50, alpha=0.7, color='#e74c3c', edgecolor='white', density=True)
plt.title(f"Market Returns (Fat Tails Detected)\nJB p-value: {p_val_mkt:.4f}")
plt.xlabel("Returns")

plt.tight_layout()

# Save the plot for GitHub Documentation
plt.savefig('normality_test_results.png')
print("Test completed. Chart saved as 'normality_test_results.png'")

# Print Statistical Summary for README
print(f"Market Data - Skewness: {stats.skew(market_returns):.2f}")
print(f"Market Data - Kurtosis: {stats.kurtosis(market_returns):.2f}")
