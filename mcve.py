import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
def _():
    from datetime import date
    import polars as pl

    df = pl.read_csv('https://raw.githubusercontent.com/Mcompetitions/M6-methods/refs/heads/main/assets_m6.csv', try_parse_dates=True)
    return date, df, pl


@app.cell
def _(df):
    df
    return


@app.cell
def _(pandas, polars):
    # I will now press:
    # ^ c e polars ESC j ^ . j ^ .
    polars
    polars

    pandas
    pandas
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
