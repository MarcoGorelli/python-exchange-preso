import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Order-dependence

        Narwhals has 4 main classes:

        1. `nw.DataFrame`. Eager dataframe, all data is in-memory, row-order is well-defined. Supports NumPy-style indexing (e.g. `df[[1, 3, 5]]`)
        2. `nw.LazyFrame`. Lazy dataframe, data might not be in-memory, row-order is undefined.
        3. `nw.Expr`: Expressions, can be used with both `nw.DataFrame` and `nw.LazyFrame`.
        4. `nw.Series`: Eager 1-dimensional structure, can only be used with `nw.DataFrame`.

        `DataFrame` and `LazyFrame` are similar, but `LazyFrame` behave differently for:

        - Indexing. In a DataFrame, you can easily select, say, the first and third rows. In a LazyFrame, the concept of "first row" is not defined.
        - Window functions. In a DataFrame, you can perform a cumulative sum. In a LazyFrame, you must specify the order in which to perform it.
        """
    )
    return


@app.cell
def _():
    import duckdb
    import pandas as pd
    import narwhals as nw
    from datetime import datetime

    df_pd = pd.DataFrame(
        {
            "store": [1, 1, 2],
            "price": [4, 5, 6],
            "date": [
                datetime(2025, 3, 25),
                datetime(2025, 3, 26),
                datetime(2025, 3, 27),
            ],
        }
    )
    df_duckdb = duckdb.table("df_pd")

    df = nw.from_native(df_pd)
    lf = nw.from_native(df_duckdb)
    return datetime, df, df_duckdb, df_pd, duckdb, lf, nw, pd


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Indexing

        - For DataFrame, you can go wild and use NumPy-style indexing.
        - For LazyFrame, you can only use expressions.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Window functions

        - For DataFrame, order-dependent functions like `cum_sum` happen in order of appearance.
        - For LazyFrame, you need to specify which column(s) to order by.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
