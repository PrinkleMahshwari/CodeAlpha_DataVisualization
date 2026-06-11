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

# visual 3: violin plot - price distribution by cut
print("Creating Visual 3: Violin Plot...")

fig3 = px.violin(
    data_frame=df_sample, # using our 5000 sample
    x='cut',
    y='price',
    color='cut',
    box=True, # adds a mini box plot inside violin
    points='outliers', # show the outlier dots
    title='<b>Price Distribution by Cut Quality</b>Violin shape shows density of data<br>',
    labels={'cut': 'Cut Quality', 'price': 'Price (USD)'}
)

fig3.write_html("interactive_plots/violin_price_cut.html")
fig3.write_image("screenshots/violin_price_cut.png")
print("✅ Visual 3 saved to interactive_plots/ and screenshots/")

# visual 4: 3D scatter plot - carat s depth vs price
print("Creating Visual 4: 3D Scatter Plot...")

df_sample_3d = df.sample(2000,  random_state=420) # smaller sample for 3D performance

fig4 = px.scatter_3d(
    data_frame=df_sample_3d,
    x='carat',
    y='depth',
    z='price',
    color='cut',
    title='<b>3D View: Carat, Depth & Price</b>Rotate the plot to explore<br>',
    labels={'carat': 'Carat', 'depth': 'Depth (%)', 'price': 'Price (USD)', 'cut': 'Cut Quality'},
    opacity=0.5
)

fig4.write_html("interactive_plots/3d_scatter.html")
fig4.write_image("screenshots/3d_scatter.png")
print("✅ Visual 4 saved to interactive_plots/ and screenshots/")

