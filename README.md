# dbt-covid-streamlit
DBT project running on a local PostgreSQL database connected to a Streamlit dashboard.

### Project Initialization
To get up and running with this project:
1. Install dbt using [these instructions](https://docs.getdbt.com/docs/installation).

2. Clone this repository.
3. Change into the `dbt_streamlit` directory from the command line:
```bash
$ cd dbt_streamlit
```

4. Set up a profile called `dbt_streamlit` to connect to a data warehouse by following [these instructions](https://docs.getdbt.com/docs/configure-your-profile). If you have access to a data warehouse, you can use those credentials – we recommend setting your [target schema](https://docs.getdbt.com/docs/configure-your-profile#section-populating-your-profile) to be a new schema (dbt will create the schema for you, as long as you have the right privileges). If you don't have access to an existing data warehouse, you can also set up a local postgres database and connect to it in your profile.

Your profile file should contain something like this:
```yml
dbt_streamlit:
  outputs:
    dev:
      dbname: covid_dbt
      host: localhost
      pass: YOUR_PASSWORD
      port: 5432
      schema: public
      threads: 4
      type: postgres
      user: YOUR_USERNAME
      keepalives_idle: 0
```

5. Ensure your profile is set up correctly, run this command from the command line:
```bash
$ dbt debug
```

6. Upload the CSV data to the postgres database
```bash
dbt seeds
```

6. Run the models:
```bash
$ dbt run
```

7. Generate documentation for the project:
```bash
$ dbt docs generate
```

8. View the documentation for the project:
```bash
$ dbt docs serve
```
