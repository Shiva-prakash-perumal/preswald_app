from preswald import text, plotly, connect, get_df, table, query, slider, playground, sidebar
import pandas as pd
import plotly.express as px

# sidebar(title="Welcome to Shiva's Project")

text("# Welcome to Shiva's Preswald Assesment!")

# Load data 
text (" ### 1. Load the dataset")
connect()
df = get_df('student')

# Display table
text("#### Student Habits Performance Table we are going to work with:")
table(df)

text("### 2. Query or manipulate the data & 3. Build an interactive UI")

# Filtering data based on mental_health_rating > 5
sql = "SELECT mental_health_rating, AVG(study_hours_per_day) AS avg_study_hours FROM student GROUP BY mental_health_rating HAVING mental_health_rating > 5"
filtered_df = query(sql, "student")

text("#### Filtering data based on mental_health_rating > 5")
table(filtered_df, title="mental_health_rating of students")

# Add user controls
text("### 3.i Adding User Controls Based on Age")
threshold = slider("Age", min_val=15, max_val=25, default=20)
table(df[df["age"] >= threshold], title="Dynamic Data View based on Age")

# Create a scatter plot comparing study_hours_per_day and mental_health_rating with gender as color
fig = px.scatter(df, x='study_hours_per_day', y='mental_health_rating', color='gender',
                 title='Study Hours vs. Mental Health Rating by Gender',
                 labels={'study_hours_per_day': 'Study Hours per Day', 'mental_health_rating': 'Mental Health Rating'},
                 hover_data=['age', 'internet_quality'])

# Style the plot
fig.update_layout(template='plotly_white')

text("### 4. Create a visualization")
plotly(fig)

text("### Other Widgets")
text("#### displaying only necessary columns of the table")
table(df[['gender', 'age', 'mental_health_rating']])

text("#### Playground")
# playground(label: str, query: str, source: str = None, size: float = 1.0) -> pd.DataFrame

play_df = playground(
    label="Student Data",
    query="SELECT age, AVG(social_media_hours) FROM student GROUP BY age Order by age desc"
)

