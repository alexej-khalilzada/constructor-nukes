# SET FOLDER ENVIRONMENT
import sys
if sys.platform=='win32':
    dots='..'
    alexejpath=''
else:
    dots='.'
    alexejpath='./Alexej/'

dirs=['Jonas','KaiH','KaiB']
for d in dirs:
    sys.path.insert(0, f'{dots}/{d}')

import plotly.express as px

def dummy(dataframe):
    ##### Plot
    # 'year' in the x-axis and 'nuclear_weapons_stockpile' in the y-axis.
    fig = px.line(dataframe, x="year", y="nuclear_weapons_stockpile", color="country_name")

    # Marker's shape should be square.
    fig.update_traces(
        marker=dict(symbol="circle", line=dict(width=2, color="DarkSlateGrey")),
        selector=dict(mode="markers"),
    )

    # Change color background for the chart and the whole plot.
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 255)',
        'paper_bgcolor': 'rgba(255, 255, 255, 255)'
    })

    # Add title, and x and y labels with font size 18.
    fig.update_xaxes(title_text='Year', title_font = {"size": 18})
    fig.update_yaxes(title_text='Nuclear Weapons Stockpile', title_font = {"size": 18})
    fig.update_layout(title_text="Nuclear Weapons Stockpile per Country per Year", title_yanchor = "top", legend_itemsizing="constant")

    # return figure
    return fig

def get_plots():
    title='Nuclear Weapons Stockpile per Country per Year'
    description = 'This chart shows the nuclear weapons stockpile per country per year'
    key='nuclear'
    lib = 'plotly_express'
    info_dict=dict(title=title, description=description, lib=lib)
    
    # dummy(overall_stockpiles_tests_merged_df)
    # dummy(df_merged)
    dummy(get_data([1]))
    
    return [(key, fig, info_dict)]
