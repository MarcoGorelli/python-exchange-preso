import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Narwhals

        Narwhals is a lightweight compatibility layer between dataframes.

        It's used by Altair, Plotly, Marimo, HierarchicalForecast, Shiny, Bokeh, and many more.

        - Motivational example
        - Narwhals crash course
        - Lazy execution and order-dependence
        - Stability
        - What comes next?
        """
    )
    return


@app.cell
def _():
    import plotly.express as px
    return (px,)


@app.cell
def _():
    # import pandas as pd

    # assets_pd = pd.read_csv("../scratch/assets.csv")
    # assets_pd = assets_pd[assets_pd["symbol"].isin(["ABBV", "XOM"])]
    # px.line(assets_pd, x="date", y="price", color="symbol")
    return


@app.cell
def _():
    # Maybe you want to use Polars instead?
    # Can we pass a Polars dataframe directly to plotly
    # and have it be plotted, without having pandas nor PyArrow even installed?
    return


@app.cell
def _(px):
    import polars as pl

    assets_pl = pl.read_csv("../scratch/assets.csv", try_parse_dates=True)
    assets_pl = assets_pl.filter(pl.col("symbol").is_in(["ABBV", "XOM"]))
    px.line(assets_pl, x="date", y="price", color="symbol")
    return assets_pl, pl


@app.cell
def _(mo):
    mo.md(
        r"""
        plotly can accept pandas or Polars without either being required
        and with no dataframe conversion between them!

        Narwhals in a nutshell:

        1. Call `narwhals.from_native` on the user's input.
        2. Express your logic using the Narwhals API.
        3. Return the object to the user using `.to_native`.
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
