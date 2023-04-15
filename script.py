 
import pandas as pd

# Read the two CSV files
df1 = pd.read_csv("input_1.csv")
df2 = pd.read_csv("input_2.csv")

# Merge the two dataframes on the "UID" column
merged_df = pd.merge(df1, df2, on="uid")

# Calculate the average statements and reasons per team
team_df = merged_df.groupby("Team Name").agg({"total_statements": "mean", "total_reasons": "mean"})
team_df = team_df.reset_index().rename(columns={"Team Name": "Thinking Teams Leaderboard", "total_statements": "Average Statements", "total_reasons": "Average Reasons"})
# team_df["Team Rank"] = team_df["Average Statements"].rank(ascending=False).astype(int)

team_df = team_df.assign(Rank=team_df['Average Statements'].rank(method='min', ascending=False).astype(int))
team_df = team_df.sort_values('Rank').reset_index()

# Calculate the individual leaderboard
ind_df = merged_df[["Name", "uid", "total_statements", "total_reasons"]]
ind_df = ind_df.sort_values(by=["total_statements", "total_reasons"], ascending=False)
ind_df = ind_df.reset_index(drop=True).reset_index().rename(columns={"index": "Rank"})

# Print the two tables
print("Team Wise Leaderboard\n")
print(team_df.to_string(index=False))
print("\nLeaderboard individual (output)\n")
print(ind_df.to_string(index=False))
