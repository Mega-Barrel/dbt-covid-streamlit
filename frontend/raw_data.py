""" Raw Data """

def raw_table(st, conn):
    """
    Method to generate Streamlit dataframe for seeds table
    """
    df1, df2 = st.columns(2)
    covid_data_seed = ''
    
    df1.write('covid_data table')
    df2.write('countries table')
