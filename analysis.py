
# analysis.py
# Author: 23f1002420@ds.study.iitm.ac.in

import marimo

app = marimo.App()

# Cell 1: Slider widget for interactive analysis
@app.cell
def cell1():
    import marimo as mo
    # Interactive slider widget
    slider = mo.ui.slider(start=1, stop=100, value=50, label="Select sample size")
    slider
    return slider

# Cell 2: Generate dataset depending on slider value
@app.cell
def cell2(slider):
    import numpy as np
    import pandas as pd

    # Variable dependency on slider value
    n = slider.value
    data = pd.DataFrame({
        "x": np.arange(n),
        "y": np.random.normal(loc=0, scale=1, size=n).cumsum()
    })
    data.head()
    return data

# Cell 3: Dynamic markdown based on widget state
@app.cell
def cell3(slider, data):
    import marimo as mo
    # Dynamic markdown reflecting state
    mo.md(f"""
    ### Data Summary
    - Current Sample Size: **{slider.value}**
    - Mean of Y: **{data['y'].mean():.2f}**
    """)

# Cell 4: Plot the dataset
@app.cell
def cell4(data):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    plt.plot(data["x"], data["y"], label="Random Walk")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Interactive Data Analysis")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    app.run()
