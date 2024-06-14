#%%
# Loading packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


sns.set_palette("colorblind")

#%%
# Load Hitters dataset & drop NaN

hitters_df = sm.datasets.get_rdataset("Hitters", "ISLR").data
hitters_df.dropna(inplace=True)
hitters_df_filt = hitters_df[["Salary", "AtBat", "Hits"]]
hitters_df_filt.reset_index(inplace=True)
hitters_df_filt.drop(columns = 'rownames', inplace=True)
hitters_df_filt.head()

#%%
# Select design matrix and dependent variable
X = hitters_df_filt.drop(columns = 'Salary')
y = hitters_df_filt['Salary']

#%%
# Converting categorical variables to dummy
X = pd.get_dummies(X, drop_first=True)

#%%
# Split the data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,random_state=73815)

#%%
# Create and Fit linear regression model
# Sklearn
lm = LinearRegression()
lm.fit(X_train, y_train)

#%%
# statsmodels
X_train_const = sm.add_constant(X_train)
model_sm = sm.OLS(y_train, X_train_const).fit()


#%%
# Predict
y_pred = lm.predict(X_test)

#%%
# Calcualte goodness of fit metrics
gf_metrics = pd.DataFrame({
    'r_squared': [r2_score(y_test, y_pred)],
    'mse': [mean_squared_error(y_test, y_pred)]
})

print(gf_metrics)

#%%
# Summary table
model_sm.summary()



#%%
#Plot true versus predicted

# Calculate residuals
res = y_test - y_pred
plot_df = pd.DataFrame({
    'Predicted' : y_pred,
    'Residuals': res
})

sns.scatterplot(data = plot_df, x = 'Predicted', y='Residuals')
plt.axhline(y=0, color='red', linestyle='--')
plt.title("Residuals vs Predicted")
plt.show()

#%%
# Calculate VIF
vif_data = pd.DataFrame()
vif_data["feature"] = X_train_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_train_const.values, i) for i in range(X_train_const.shape[1])]
print(vif_data)