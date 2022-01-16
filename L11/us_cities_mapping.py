import plotly.express as px
import pandas as pd
import re

us_cities_data = "us_cities_pop.csv"
usCities = pd.read_csv(us_cities_data, sep=",", header=0)

# plot places
placesAll = usCities[['year', 'cityst', 'population', 'lat', 'lon']]
print(placesAll)

fig = px.scatter_geo(placesAll, lon='lon', lat='lat',
                     hover_name="cityst",
                     animation_frame="year",
                     size='population')

fig.update_layout(
    title_text='Growth of US cities (1790-2010)',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(235, 235, 235)',
    )
)

fig.show()
fig.write_html("us_cities_pop.html")
