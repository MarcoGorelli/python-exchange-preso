import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Narwhals crash-course""")
    return


@app.cell
def _():
    import narwhals as nw
    import pandas as pd
    import polars as pl
    import duckdb
    return duckdb, nw, pd, pl


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(duckdb, pd, pl):
    file = "../scratch/vegetables.csv"

    # Paul
    df_pd = pd.read_csv(file)
    # Polina
    df_pl = pl.read_csv(file, try_parse_dates=True)
    # Dominique
    df_duckdb = duckdb.read_csv(file)
    return df_duckdb, df_pd, df_pl, file


@app.cell
def _(df_duckdb):
    df_duckdb
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Task

        Write a function which, given a dataframe:

        - Only keeps rows where we have Tomatoes, Carrots, or Potatoes
        - Strips currency from `'farmprice'` and converts to `Float64`
        - Scale the farm price (subtract mean, divide by standard deviation)
        - Only keep 'productname', 'farmprice', 'date' columns
        - Sort by date and productname

        This function should for `df_pd`, `df_pl`, and `df_duckdb`.
        """
    )
    return


@app.cell
def _(df_duckdb, duckdb, pd, pl):
    def clean_dataset(df):
        if isinstance(df, pd.DataFrame):
            df = df.loc[
                df["productname"].isin(["Tomatoes", "Carrots", "Potatoes"])
            ]
            df = df.assign(
                farmprice=lambda df: df["farmprice"]
                .str.lstrip("$")
                .astype("float64")
            )
            df = df.assign(
                farmprice=lambda df: (df["farmprice"] - df["farmprice"].mean())
                / df["farmprice"].std()
            )
            return df[["date", "productname", "farmprice"]].sort_values(
                ["date", "productname"]
            )

        if isinstance(df, pl.DataFrame):
            return (
                df.filter(
                    pl.col("productname").is_in(
                        ["Tomatoes", "Carrots", "Potatoes"]
                    )
                )
                .with_columns(
                    pl.col("farmprice").str.strip_chars("$").cast(pl.Float64)
                )
                .with_columns(
                    (pl.col("farmprice") - pl.col("farmprice").mean())
                    / pl.col("farmprice").std()
                )
                .select("date", "productname", "farmprice")
                .sort("date", "productname")
            )

        if isinstance(df, duckdb.DuckDBPyRelation):
            return duckdb.sql("""
            with cte as (
                from df_duckdb
                select date,
                    productname, 
                    cast(REGEXP_REPLACE("farmprice", '^\$', '') as double) as farmprice
                where productname in ('Tomatoes', 'Carrots', 'Potatoes')
            )
            from cte
            select *,
                ("farmprice" - mean(farmprice) over ()) / stddev_samp(farmprice) over () as farmprice
            order by date, productname
            """)
    return (clean_dataset,)


@app.cell
def _(clean_dataset, df_pd):
    clean_dataset(df_pd)
    return


@app.cell
def _(clean_dataset, df_pl):
    clean_dataset(df_pl)
    return


@app.cell
def _(clean_dataset, df_duckdb):
    clean_dataset(df_duckdb)
    return


@app.cell
def _():
    # 1. `from_native` on the user's input
    # 2. use the Narwhals API
    # 3. call `to_native`
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
