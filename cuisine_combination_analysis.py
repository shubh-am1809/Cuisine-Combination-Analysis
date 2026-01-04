import pandas as pd

df = pd.read_csv("dataset .csv")
df = df[['Cuisines', 'Aggregate rating']].dropna()

df['Cuisine_Combination'] = (
    df['Cuisines']
    .str.split(', ')
    .apply(lambda x: ', '.join(sorted(x)))
)

top_combinations = df['Cuisine_Combination'].value_counts().head(10)

print("\nTop 10 Most Common Cuisine Combinations:\n")
print(top_combinations)

combo_ratings = (
    df.groupby('Cuisine_Combination')['Aggregate rating']
    .mean()
    .sort_values(ascending=False)
)

print("\nCuisine Combinations with Highest Average Ratings:\n")
print(combo_ratings.head(10))


top_combinations_df = top_combinations.reset_index()
top_combinations_df.columns = ['Cuisine Combination', 'Restaurant Count']

combo_ratings_df = combo_ratings.reset_index()
combo_ratings_df.columns = ['Cuisine Combination', 'Average Rating']

top_combinations_df.to_csv(
    "output/top_cuisine_combinations.csv", index=False
)
combo_ratings_df.to_csv(
    "output/cuisine_combination_ratings.csv", index=False
)

print("\nResults saved in output/ folder")
