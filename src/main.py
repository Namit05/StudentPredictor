#All the modules I used
from pathlib import Path

from dataset import create_dataset
from model import train_model
from prediction import predict_student
from visualization import create_visualizations

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "student_data.csv"


def main():
    while True:
        print("Student Performance Prediction System")
        print("1.Generate the dataset")
        print("2.Train and evaluate the model")
        print("3.Prediction of marks")
        print("4.Generate graphgs ")
        print("5.Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            df = create_dataset()
            df.to_csv(DATASET_PATH, index=False)
            print("Dataset saved")

        elif choice in ["2", "3", "4"]:
            if not DATASET_PATH.exists():
                print("Please generate the dataset first!")
                continue

            if choice == "2":
                train_model()

            elif choice == "3":
                predict_student()

            elif choice == "4":
                create_visualizations()

        elif choice == "5":
            print("Thank you and goodbye")
            break

        else:
            print("Invalid choice try agaibn")


if __name__ == "__main__":
    main()