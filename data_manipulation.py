# %%
# Import packages
import pandas as pd

# %%
# Create fake dataframe
df = pd.DataFrame(
data = {
    'ID':[1,2,3],
    'Name':['Alice', 'Bob', 'Martin'],
    'Math':[85,32,12],
    'Science':[29,12,43]
})
print(df)

# %%
# Melt dataframe, to get a single column with "Score"
melted_df = pd.melt(df, id_vars=['ID', 'Name'], value_vars=['Math', 'Science'], var_name='Subject', value_name='Score') #  if non value_vars it uses all vars except id_vars
melted_df

# %%
# Groupby columns and calculate statistics
melted_df[["Subject", "Score"]].groupby('Subject').mean().reset_index()
melted_df.groupby('Subject')["Score"].mean()

melted_df.groupby('Subject')["Score"].agg(['mean', 'sum', 'count']).reset_index()

melted_df['Score'].agg(['sum', 'mean'])

#%%
# Value counts a single column
melted_df['Subject'].value_counts()
# %%
# Merge dataframes

df_2 = pd.DataFrame({
    'ID':[1,2,3],
    'Age':[80,76,81]
})

merged_df = pd.merge(df, df_2, on='ID', how='inner') # change the how with left, right or outer. Also 
merged_df = pd.merge(df, df_2, left_on='ID',right_on="ID", how='inner') # Useful when dif keys 

print(merged_df)

#%%
# Concat
concat_col_df = pd.concat([df, df_2], axis=1) # by column
print(concat_col_df)

concat_row_df = pd.concat([df, df_2], axis=0) # by row, NaNs included when cols don't match
print(concat_row_df)


#%%
# Dealing with NaN
concat_row_df.dropna(inplace=False) # drop
concat_row_df.fillna(0, inplace=False) #replace with value
concat_row_df.fillna({'Name':"Pedro", "Math":df['Math'].mean()}) #replace with diff values

#%%
# Drop columns
df.drop(columns = "Name")




















