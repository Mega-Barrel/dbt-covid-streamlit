""" Raw Data """

def raw_table(st, engine, pd):
    """
    Method to generate Streamlit dataframe for seeds table
    """
    df1, df2 = st.columns(2)
    covid_data_seed = pd.read_sql_table('covid_data', con=engine, schema='public')
    countries_data_seed = pd.read_sql_table('countries', con=engine, schema='public')

    df1.write('covid_data table')
    df1.dataframe(covid_data_seed, use_container_width=True)
    df2.write('countries table')
    df2.dataframe(countries_data_seed, use_container_width=True)

def staging_table(st, engine, pd):
    df1, df2, df3 = st.columns(3)
    stg_country = pd.read_sql_table('stg_country', con=engine, schema='public')
    stg_monthly_deaths = pd.read_sql_table('stg_monthly_deaths', con=engine, schema='public')
    stg_prepared_source = pd.read_sql_table('stg_prepared_source', con=engine, schema='public')

    df1.write('Staging country table.')
    df1.dataframe(stg_country, use_container_width=True)
    df2.write('Staging prepared_source table.')
    df2.dataframe(stg_prepared_source, use_container_width=True)
    df3.write('Staging monthly_deaths table.')
    df3.dataframe(stg_monthly_deaths, use_container_width=True)
    

def mart_table(st, engine, pd):
    df1, df2, df3 = st.columns(3)
    dim_countries = pd.read_sql_table('dim_countries', con=engine, schema='public')
    fct_monthly_confirmed = pd.read_sql_table('fct_monthly_confirmed', con=engine, schema='public')
    fct_monthly_death_rate = pd.read_sql_table('fct_monthly_death_rate', con=engine, schema='public')

    df1.write('Dim countries table.')
    df1.dataframe(dim_countries, use_container_width=True)
    df2.write('Fact monthly_confirmed table.')
    df2.dataframe(fct_monthly_confirmed, use_container_width=True)
    df3.write('Fact monthly_death_rate table.')
    df3.dataframe(fct_monthly_death_rate, use_container_width=True)