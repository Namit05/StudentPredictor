# Student Performance Prediction System

## Project Title

**Student Performance Predictor made using Machine Learning**

## Overview

This is a beginner-level Python application demonstrating supervised machine
learning with **Linear Regression**. it exxamines the marks scored out of 100 by analysisng the sleep schedule , atteandacne and hours studied.
The project uses 9 synthetic records for the Model training.

## Features

-  It  Generates `student_data.csv` from nine sample records.
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

4.  Install dependencies: Pandas and Sikit-learn

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
1)Main Interface :

<img width="470" height="233" alt="Main Interface" src="https://github.com/user-attachments/assets/cbffa812-84f7-47aa-849f-1269b337aa16" />


2)Model Training
<img width="464" height="227" alt="Student Prediction" src="https://github.com/user-attachments/assets/f9bcbbd5-967e-4d31-9e78-25b31f88f313" />



3)Prediction

<img width="465" height="464" alt="Prediction" src="https://github.com/user-attachments/assets/c4c04019-a36d-4017-9d9a-8f3480d95ab9" />


