"""About page"""

def get_about(st):
    st.markdown(
        """
        #### Overview:
        - Create an interactive COVID-19 data dashboard by combining the power of dbt (data build tool) and Streamlit. 
        - This project utilizes two primary data sources, namely **covid_data.csv** and **countries.csv**, serving as seeds files for dbt. 
        - The data transformation and modeling are performed using **dbt**, with the processed data stored in a local **PostgreSQL** database under the default schema 'public'.

        #### Key Components:
        - Data Sources:
            - covid_data.csv: Contains COVID-19 related data, including cases, deaths, and recoveries.
            - countries.csv: Provides additional information about countries, such as population and geographic details.
        - ETL Process with dbt:
            - Use dbt to transform and model raw data into structured tables.
            - Leverage dbt's modular and version-controlled approach for data transformations.
            - Apply transformations to handle data cleaning, aggregations, and other necessary operations.
        - PostgreSQL Database:
            - Store the processed data in a local PostgreSQL database.
            - Utilize the default schema 'public' for organized data storage.
        - Streamlit Dashboard:
            - Develop a user-friendly dashboard using Streamlit.
            - Connect Streamlit to the PostgreSQL database to dynamically fetch and display data.
        - Features:
            - Display key COVID-19 statistics for Italy and Germany countries.
            - Provide trend analysis through time-series charts.

        #### Dependencies:
        - dbt for data transformation and modeling.
        - PostgreSQL for local database storage.
        - Streamlit for building the interactive dashboard.
        """
    )

    st.markdown("""#### dbt-dag""")
    st.image('assets/dbt-dag.png')

    st.markdown(
        """
        #### Resources:
        - Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
        - A hands-on project with dbt, Streamlit, and PostgreSQL [blog article](https://www.data-max.io/post/dbt-streamlit-postgres-handson)
        - dbt-streamlit-covid-analytics [GitHub repository](https://github.com/data-max-hq/dbt-streamlit-covid-analytics)
        """
    )