# Project Statement: Student Performance Predictor

## Problem Statement

Students and educators may want to explore how measurable study-related
habits relate to examination marks. This project accepts daily study
hours, attendance percentage, and daily sleep hours, then estimates
marks out of 100 using a simple machine-learning model. It is an
educational demonstration, not a tool for grading or other consequential
decisions.

## Scope of the Project

The project is a local, menu-driven Python application demonstrating a
basic supervised-learning workflow. It includes: - Creating nine
synthetic sample records. - Using **Linear Regression** to estimate a
numerical marks value. - Splitting records into training and testing
subsets. - Reporting Mean Absolute Error (MAE) and R². - Accepting
feature values and displaying an estimated score. - Generating scatter
plots for each input feature against marks. - Saving the dataset as
`student_data.csv` and plot images in `Screenshots/`.

It does not use real student records, a database server, online
services, user accounts, or a graphical web interface. The small
synthetic dataset makes this a learning prototype, not a validated
real-world predictor.

## Target Users

-   Students learning introductory Artificial Intelligence and Machine
    Learning.
-   Instructors demonstrating regression, data preparation, and
    evaluation.
-   Users experimenting with a simple numerical prediction pipeline.

## High-Level Features

1.  **Dataset Generation:** Creates nine illustrative records containing
    study hours, attendance, sleep hours, and marks.
2.  **Model Training:** Trains Linear Regression using the three input
    features.
3.  **Model Evaluation:** Displays MAE and R² on a held-out test subset.
4.  **Marks Prediction:** Validates user inputs and displays estimated
    marks out of 100.
5.  **Data Visualization:** Creates study-hours-vs-marks,
    attendance-vs-marks, and sleep-hours-vs-marks scatter plots.
6.  **Menu-Based Operation:** Offers dataset generation, evaluation,
    prediction, visualization, and exit.

## Inputs and Output

**Inputs** - Study hours per day: 0--24. - Attendance: 0--100 percent. -
Sleep hours per day: 0--24.

**Output** - Estimated examination marks on a 0--100 scale.

## Algorithm

The project uses **Linear Regression**, a supervised regression
algorithm for estimating a continuous numerical target. The features are
`study_hours`, `attendance`, and `sleep_hours`; the target is `marks`.
The code uses `train_test_split(test_size=0.33, random_state=42)`, fits
the model on the training subset, and evaluates it using MAE and R².

## Constraints and Limitations

-   Only nine synthetic records are used.
-   The data does not represent a real student population.
-   Only three features are included; many other factors can affect
    academic outcomes.
-   Metrics from a very small test subset are unstable and should be
    interpreted cautiously.
-   Predictions are estimates, not guaranteed results.

## Expected Outcome

A working Python program demonstrating dataset creation, Linear
Regression training, basic evaluation, interactive marks prediction, and
visualization in a modular code structure.
