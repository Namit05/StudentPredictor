# Student Performance Predictor

## Project Title

**Student Performance Predictor using Machine Learning**

## Overview

A beginner-level Python application demonstrating supervised machine
learning with **Linear Regression**. It estimates examination marks out
of 100 using daily study hours, attendance percentage, and daily sleep
hours. The project uses nine synthetic sample records and is intended
for learning only---not reliable prediction about real students.

## Features

-   Generate `student_data.csv` from nine sample records.
-   Train a Linear Regression model using study hours, attendance, and
    sleep hours.
-   Evaluate with Mean Absolute Error (MAE) and R².
-   Enter values and receive estimated marks.
-   Generate scatter plots for study hours vs. marks, attendance
    vs. marks, and sleep hours vs. marks.
-   Use a simple menu-driven command-line interface.
-   Keep code separated into Python modules.

## Technologies and Tools

-   Python
-   pandas --- tabular data
-   scikit-learn --- train/test split, Linear Regression, evaluation
    metrics
-   matplotlib --- plots
-   CSV --- dataset storage
-   Git and GitHub --- version control and repository hosting

## Project Structure

``` text
StudentPredictor/
├── src/
│   ├── main.py
│   ├── dataset.py
│   ├── model.py
│   ├── prediction.py
│   └── visualization.py
├── student_data.csv       # generated
├── Screenshots/           # plots / evidence
├── requirements.txt
├── README.md
└── statement.md
```

## Installation

1.  Install Python.

2.  Clone or download the repository.

3.  Open a terminal in the project root.

4.  Optionally create a virtual environment:

    ``` powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

5.  Install dependencies:

    ``` bash
    python -m pip install -r requirements.txt
    ```

    Ensure `requirements.txt` includes `pandas`, `scikit-learn`, and
    `matplotlib`. If needed:

    ``` bash
    python -m pip install pandas scikit-learn matplotlib
    ```

## Run the Project

From the project root:

``` bash
python src/main.py
```

Use the menu to generate the dataset, train/evaluate the model, predict
marks, generate visualizations, or exit. Generate the dataset first if
`student_data.csv` is missing.

## Testing Instructions

1.  Generate the dataset and confirm `student_data.csv` is created.
2.  Train/evaluate and confirm training/testing counts, MAE, and R² are
    printed.
3.  Make a prediction with study hours (0--24), attendance (0--100), and
    sleep hours (0--24).
4.  Try non-numeric and out-of-range inputs; confirm they are handled
    clearly.
5.  Generate plots and confirm the three image files appear in
    `Screenshots/`.
6.  If practical, test a dependent operation before generating the CSV
    and confirm the program gives a helpful message.

## Screenshots

Add genuine screenshots from your final run: - Main menu and dataset
generation - Model evaluation output - Example prediction - Three
scatter plots

## Limitations

The dataset contains only nine synthetic records and uses only three
features. Metrics from such a small test set may be unstable.
Predictions are educational estimates, not guaranteed outcomes and must
not be used for grading or other consequential decisions.

## Author

-   Name: \[Your Name\]
-   Course: Fundamentals of AIML
-   Institution: VIT Bhopal University
