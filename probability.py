#%%
# importing libraries
import numpy as np
import pandas as pd
#%%
# Simluate random numbers
size = 1000
df_sim = pd.DataFrame({
    'uniform': np.random.uniform(low=0, high=1, size =size),
    'normal': np.random.normal(loc=0, scale=1, size=size),
    'exponential': np.random.exponential(scale=1, size=size),
    'binomial': np.random.binomial(n=1, p=0.5, size=size),
    'poisson': np.random.poisson(lam=3, size=size),
    'beta':np.random.beta(a=2,b=5,size=1000),
    'gamma':np.random.gamma(shape=2,scale=2,size=1000),
    'chi_squared': np.random.chisquare(df=2, size=size)
    })

df_sim.head()

#%%
#Calculate statistics

quantiles = df_sim.quantile([0.25, 0.5, 0.75])

cov_mat = df_sim.cov()

corr_mat = df_sim.corr()
