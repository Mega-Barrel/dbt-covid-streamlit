"""Graph page"""

def generate_fct_monthly_plot(engine, pd, px):
    df = pd.read_sql_table('fct_monthly_confirmed', con=engine, schema='public')
    df.loc[:, 'year_month'] = pd.to_datetime(df.year_month, format='%Y-%m')
    df = df.sort_values(by=['year_month'], ascending=False)

    fig = px.line(
        df,
        x='year_month',
        y='confirmed_cases',
        color='name',
        color_discrete_sequence=[
            "rgba(67,24,255,0.85)", 
            "rgba(106,210,255,0.85)"
        ]
    )

    # update fig layout
    fig.update_layout(
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        title_x=0.5,
        title="Italy Vs Germany monthly confirmed cases",
        margin_t=100,
        hovermode="x"
    )

    fig.update_xaxes(
        showgrid=False,
    )

    fig.update_yaxes(
        showgrid=False,
    )

    fig.update_traces(
        line = dict(width=4)
    )

    # fig.add_annotation(
    #     text='<b>$90.8M',
    #     align='left',
    #     showarrow=False,
    #     xref='paper',
    #     yref='paper',
    #     x=0.07,
    #     y=0.9,
    #     font_size = 24
    # )

    # fig.add_annotation(
    #     text='<br>Total spent launched health</br>education campaigns by <br>Australia & New Zealand Govt in 1972',
    #     align='left',
    #     xref='paper',
    #     yref='paper',
    #     x=0.07,
    #     y=0.76,
    #     font_size = 13,
    #     font_color = '#808080',
    #     showarrow=False
    # )

    return fig

def generate_fct_monthly_death_rate(engine, pd, px):
    df = pd.read_sql_table('fct_monthly_death_rate', con=engine, schema='public')
    df.loc[:, 'year_month'] = pd.to_datetime(df.year_month, format='%Y-%m')
    df = df.sort_values(by=['year_month'], ascending=False)

    fig = px.line(
        df,
        x='year_month',
        y='death_rate',
        color='name',
        color_discrete_sequence=[
            "rgba(67,24,255,0.85)", 
            "rgba(106,210,255,0.85)"
        ]
    )

    # update fig layout
    fig.update_layout(
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        title_x=0.5,
        title="Italy Vs Germany monthly death rate %",
        margin_t=100,
        hovermode="x"
    )

    fig.update_xaxes(
        showgrid=False,
    )

    fig.update_yaxes(
        showgrid=False,
    )

    fig.update_traces(
        line = dict(width=4)
    )

    return fig