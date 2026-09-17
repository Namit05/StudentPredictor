#All modukles i used
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

#Location of the folder
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "student_data.csv"


def train_model():

    #dataset
    df = pd.read_csv(DATASET_PATH)

    #Input for tghe data
    X = df[
        ["study_hours", "attendance", "sleep_hours"]
    ]

    #Target
    y = df["marks"]

    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.33,
        random_state=42
    )

    #Linear Regression creation
    model = LinearRegression()

    #Model training
    model.fit(X_train, y_train)

    #Predicti marks
    y_pred = model.predict(X_test)

    #Evalution
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model Evalution")
    print("----------------")
    print("Training reords:", len(X_train))
    print("Testing recrds:", len(X_test))
    print(f"Man Absoute Error: {mae:.2f}")
    print(f"R2 Score: {r2:.2f}")

    return model, mae, r2


if __name__ == "__main__":
    train_model()