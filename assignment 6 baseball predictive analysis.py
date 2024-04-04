import pandas as pd
import statsmodels.api as sm

# Read the Excel file
file_path = 'C:\\Users\\kylew\\Downloads\\baseball.xlsx'
df = pd.read_excel(file_path)

# Filter out data for the year 2012
df_filtered = df[df['Year'] != 2012]

# Define independent variables
independent_vars = ['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average']

# Define dependent variable
dependent_var = 'Playoffs'

# Create the model
X = df_filtered[independent_vars]
y = df_filtered[dependent_var]

# Add constant for intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Print regression statistics
print(model.summary())

# Predicting playoffs for 2012
df_2012 = df[df['Year'] == 2012]
X_2012 = df_2012[independent_vars]
X_2012 = sm.add_constant(X_2012)

# Predicting playoffs for 2012
predicted_playoffs = model.predict(X_2012)

# Combine predictions with team names and leagues
predicted_teams = pd.concat([df_2012[['Team', 'League']], predicted_playoffs], axis=1)
predicted_teams.columns = ['Team', 'League', 'Predicted_Playoffs']

# Get top 5 teams from each league
top_5_AL = predicted_teams[predicted_teams['League'] == 'AL'].nlargest(5, 'Predicted_Playoffs')
top_5_NL = predicted_teams[predicted_teams['League'] == 'NL'].nlargest(5, 'Predicted_Playoffs')

# Print top 5 teams from each league
print("\nTop 5 Teams Predicted to Make Playoffs in AL:")
print(top_5_AL[['Team', 'Predicted_Playoffs']])
print("\nTop 5 Teams Predicted to Make Playoffs in NL:")
print(top_5_NL[['Team', 'Predicted_Playoffs']])

# Actual teams that made playoffs in 2012
actual_playoffs = df_2012[df_2012['Playoffs'] == 1]

# Comparison of predicted vs actual teams
predicted_teams_set = set(top_5_AL['Team']).union(set(top_5_NL['Team']))
actual_teams_set = set(actual_playoffs['Team'])
correct_predictions = predicted_teams_set.intersection(actual_teams_set)

# Teams not chosen
not_chosen_teams = actual_teams_set - predicted_teams_set

# Calculate percentage of correctly chosen teams
percentage_correct = len(correct_predictions) / 10 * 100

# Print correctness and percentage
print("\nCorrectly Predicted Teams:")
print(correct_predictions)
print("\nTeams Not Chosen:")
print(not_chosen_teams)
print(f"\nPercentage of Correctly Chosen Teams: {percentage_correct}%")

print('Milwaukee Brewers 2024 World Series Champions')
