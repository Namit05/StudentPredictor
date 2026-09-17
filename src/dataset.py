#The modules used
import pandas as pd
from pathlib import Path


def create_dataset():
    """Creating dataset of students"""

    data = {
        "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "attendance": [60, 65, 70, 75, 80, 85, 90, 95, 100],
        "sleep_hours": [5, 6, 7, 8, 6, 7, 8, 7, 8],
        "marks": [35, 42, 50, 58, 65, 72, 80, 88, 95]
    }

    df = pd.DataFrame(data)

    return df


if __name__ == "__main__":

    df = create_dataset()

    BASE_DIR = Path(__file__).resolve().parent.parent
    output_path = BASE_DIR / "student_data.csv"

    df.to_csv(output_path, index=False)

    print("Dataset created")
    print("it is saved at:", output_path)

    print("Student Dataset:")
    print(df)