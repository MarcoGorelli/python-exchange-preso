import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Stability: building on top of Narwhals

        Narwhals takes backwards-compatibility very seriously.

        We currently expose two namespaces:
        - `import narwhals as nw`. Maybe subject to changes / deprecation cycles.
        - `import narwhals.stable.v1 as nw`. Not expected to ever change (so long as that's possible).

        Suggestion:
        - prototype / explore using `import narwhals as nw`. When you're happy, trying switching over to `import narwhals.stable.v1 as nw`, and if it still works, deploy your tool with confidence that new Narwhals releases won't break it! 🚀
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import narwhals as nw


    def agnostic_clean_dataset(df_native):
        # step 1
        df = nw.from_native(df_native)

        # step 2
        result = (
            df.filter(
                nw.col("productname").is_in(["Tomatoes", "Carrots", "Potatoes"])
            )
            .with_columns(
                nw.col("farmprice").str.strip_chars("$").cast(nw.Float64)
            )
            .with_columns(
                (nw.col("farmprice") - nw.col("farmprice").mean())
                / nw.col("farmprice").std()
            )
            .select("date", "productname", "farmprice")
            .sort("date", "productname")
        )

        # step 3
        return result.to_native()
    return agnostic_clean_dataset, nw


@app.cell
def _(agnostic_clean_dataset):
    import pandas as pd

    agnostic_clean_dataset(pd.read_csv("../scratch/vegetables.csv"))
    return (pd,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
