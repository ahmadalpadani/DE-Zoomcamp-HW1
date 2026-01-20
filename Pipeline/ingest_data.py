import pandas as pd
from sqlalchemy import create_engine
import click


@click.command()
@click.option('--user', default='postgres', help='PostgreSQL user')
@click.option('--password', default='postgres', help='PostgreSQL password')
@click.option('--host', default='localhost', help='PostgreSQL host')
@click.option('--port', default=5433, type=int, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='ny_taxi_data', help='Target table name')
@click.option('--table1', default='ny_taxi_zone', help='Target table name')


def ingest_data(user, password, host, port, db, table, table1):
    
    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db}'
    )

    df = pd.read_parquet("green_tripdata_2025-11.parquet")

    df1 = pd.read_csv('taxi_zone_lookup.csv')

    df.head(n=0).to_sql(
        name=table,
        con=engine,
        if_exists='replace'
    )


    df.to_sql(
        name=table,
        con=engine,
        if_exists='append'
    )
    print(f"Inserted data: {len(df)} rows")


    df1.head(n=0).to_sql(
        name=table1,
        con=engine,
        if_exists='replace'
    )

    df1.to_sql(
        name=table1,
        con=engine,
        if_exists='append'
    )
    print(f"Inserted data: {len(df1)} rows")

if __name__ == "__main__":
    ingest_data()


