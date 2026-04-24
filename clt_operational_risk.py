#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:26:48 2026

@author: sajadadeli
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


"""
Project: Central Limit Theorem (CLT) in Operational Risk Modeling
Description: Proving that the average of skewed operational losses
             converges to a Normal Distribution as sample size (n) increases.
"""


# 1. Generate Raw Operational Loss Data.
# Most bank losses are small, but a few are huge (skewed)
# We use Lognormal' to represent this 'Fat-Tail' reality.

np.random.seed(42)
population_losses = np.random.lognormal(mean=2, sigma=0.8, size=10000)

# 2. Define sample sizes (n)
sample_sizes = [2, 10, 30, 1000]


plt.figure(figsize=(15,10))
plt.suptitle("CLT: Convergence of Average Operational Losses", fontsize = 16)

for i, n in enumerate(sample_sizes):
    # Take 1000 random samples of size n and calculate their means.
    sample_means = [np.mean(np.random.choice(population_losses, size=n)) for _ in range(1000)]
    
    plt.subplot(2, 2, i+1)
    
    # plot the histogram of sample means
    plt.hist(sample_means, bins=40, density=True, color='navy', alpha=0.6, edgecolor= 'white')
    
    # Fit and plot a Normal Distribution curve to see the convergence
    mu, std = stats.norm.fit(sample_means)
    x = np.linspace(min(sample_means), max(sample_means), 100)
    plt.plot(x, stats.norm.pdf(x, mu, std), color='crimson', lw=2, label='Normal Fit')
    
    plt.title(f'Sample Size (n) = {n} Events')
    plt.xlabel('Average Loss Amount')
    plt.ylabel('Density')
    plt.legend()
    
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# Save the plot for the GitHub repository
plt.savefig('clt_plot.png')
plt.show()
