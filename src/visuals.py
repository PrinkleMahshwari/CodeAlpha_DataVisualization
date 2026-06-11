# import libraries
import pandas as pd 
import plotly.express as px

# load datasets
print("Loading dataset...")
df = pd.read_csv('data/diamonds.csv')

# data cleaning - removing 0 dimensions
df = df[(df['x'] != 0) & (df['y'] != 0) & (df['z'] != 0)]
print(f"Data cleaned. Total rows: {len(df)}\n")

# visual 1: interactive scatter plot - carat vs price
print("Creating Visual 1: Interactive Scatter Plot...")
df_sample = df.sample(5000, random_state=42)
fig1 = px.scatter(
    data_frame = df_sample,
    x = 'carat',
    y='price',
    color='cut', # color points by cut quality
    title='<b>Diamond Price VS. Carat Weight</b>Hover to see details! (sample of 5000)<br>',
    labels={'carat': 'Carat (Weight)', 'price': 'Price (USD)', 'cut': 'Cut Quality'},
    hover_data=['color', 'clarity'], # show extra info when you hover
    opacity=0.6
)

# save as Interactive HTML - Can opened by any browser
fig1.write_html("interactive_plots/scatter_carat_price.html")

# save as static png
fig1.write_image("screenshots/scatter_carat_price.png")

print("✅ Visual 1 saved to interactive_plots/ and screenshots/")

# visual 2: donut chart - market share of diamond cuts
print("Creating Visual 2: Donut Chart...")

# count the concurrence of each cut
cut_counts = df['cut'].value_counts().reset_index()
cut_counts.columns = ['cut', 'count']

fig2 = px.pie(
    data_frame=cut_counts,
    values='count',
    names='cut',
    hole=0.5, # this makes donut chart instead of pie chart
    title='<b>Market Share of Diamond Cuts</b>',
    color_discrete_sequence=px.colors.sequential.Viridis
)

fig2.write_html("interactive_plots/donut_cut_share.html")
fig2.write_image("screenshots/donut_cut_share.png")
print("✅ Visual 2 saved to interactive_plots/ and screenshots/")

