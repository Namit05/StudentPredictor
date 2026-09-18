# Project Statement: Student Performance Predictor

## Problem Statement

Students and educators may want to explore how measurable study-related
habits relate to examination marks. This project accepts daily study
hours, attendance percentage, and daily sleep hours, then estimates
marks out of 100 using a simple machine-learning model. It is an
educational demonstration, not a tool for grading or other consequential
decisions.

## Scope of the Project

The project is a local , prediction tool which uses the supervised learning concept of Linear Regression to predict 
a student's marks out of 100 using key inputs namely 
Attendance , Sleep hours and study hours.
It firsts uses this data to train the model before making predictions based on a dataset provided to the said model.
In the end it generates Graphs for more better visalization and also saves the screenshots!
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

The project uses **Linear Regression**, which is a supervised regression
algorithm used for estimating a continous numerical value. The features are attendance , sleep hours , study hours
and the target is marks.
The code uses `train_test_split(test_size=0.33, random_state=42)`, fits
the model on the training subset, and evaluates it using MAE and R².

## Constraints and Limitations

-   Only nine synthetic records are used.
-   The data is not real and does not represent actual students.
-   A lot of other factors affect the academic outcomes but only 3 are included.
-  This is a very small test so the results might be quite unstable for us.
-   Predictions are estimates, not guaranteed results.

## Expected Outcome

A working Python program demonstrating dataset creation, Linear
Regression training, basic evaluation, interactive marks prediction, and
visualization in a modular code structure.
