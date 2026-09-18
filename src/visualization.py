#module used
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "student_data.csv"
OUTPUT_DIR = BASE_DIR / "Screenshots"


def create_visualizations():

    #Dataset 
    df = pd.read_csv(DATASET_PATH)

    #SS creation
    OUTPUT_DIR.mkdir(exist_ok=True)

    #Study hours vs marks graph
    plt.figure(figsize=(6, 4))

    plt.scatter(
        df["study_hours"],
        df["marks"]
    )

    plt.title("Study hours vs Marks")
    plt.xlabel("Study hours(per day)")
    plt.ylabel("Marks")
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "hours vs marks .png")
    plt.show()
    plt.close()

    #Attendance vs Marks graph
    plt.figure(figsize=(6, 4))

    plt.scatter(
        df["attendance"],
        df["marks"]
    )

    plt.title("attendance vs marks")
    plt.xlabel("Attendance")
    plt.ylabel("Marks")
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "attendanve vs marks.png")
    plt.show()
    plt.close()

    #Sleep hours vs marks graph
    plt.figure(figsize=(6, 4))

    plt.scatter(
        df["sleep_hours"],
        df["marks"]
    )

    plt.title("sleep hours vs marks")
    plt.xlabel("Sleep hours per day")
    plt.ylabel("Marks")
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "Sleep Hour vs marks.png")
    plt.show()
    plt.close()

    print("Visulizations creaed succesfully!")
    print("Savd in:", OUTPUT_DIR)


if __name__ == "__main__":
    create_visualizations()