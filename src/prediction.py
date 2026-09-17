#modules used
import pandas as pd
from model import train_model


def get_student_input():
    """Collect and check details"""

    while True:
        try:
            study_hours = float(
                input("how many hours yo ustudy per day (0-24 hrs): ")
            )

            attendance = float(
                input("what is your attendance percentage out of 100: ")
            )

            sleep_hours = float(
                input("How many sleep hours u get(0-24): ")
            )

            if not 0 <= study_hours <= 24:
                print("Study housrs need to be between 0 and 24")
                continue

            if not 0 <= attendance <= 100:
                print("attendance need to be between 0 and 100")
                continue

            if not 0 <= sleep_hours <= 24:
                print("sleep hour need to be beteen 0 and 24")
                continue

            return pd.DataFrame(
                [[study_hours, attendance, sleep_hours]],
                columns=[
                    "study_hours",
                    "attendance",
                    "sleep_hours"
                ]
            )

        except ValueError:
            print("Please enter vaid values")


def predict_student():
    """marks prediction via liear regression"""

    model, mae, r2 = train_model()

    print("Student Preditor")
    print("-----------------------------")

    student_data = get_student_input()

    prediction = model.predict(student_data)[0]

    prediction = max(0, min(100, prediction))

    print("Result")
    print("---------")
    print(f"Prediced Marks: {prediction:.2f}/100")
    print(f"Moel MAE: {mae:.2f}")
    print(f"Modl R2 Score: {r2:.2f}")


if __name__ == "__main__":
    predict_student()