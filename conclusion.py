import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Conclusion, next steps

        Narwhals is a lightweight compatibility layer between dataframes.

        It's used by Altair, Plotly, Marimo, HierarchicalForecast, Shiny, Bokeh, and many more.

        To use it:
        1. `narwhals.from_native` on the user's input.
        2. Use the Narwhals API.
        3. Return the object to the user with `.to_native()`.

        Next steps:
        - Stabilise API into `narwhals.stable.v2`
        - Improve support for lazy-only backends (DuckDB, PySpark, SQLFrame, Ibis)
        - Narwhalify more libraries!
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
