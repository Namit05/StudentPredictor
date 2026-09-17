#THIS IS THE TEST FILE AND IS USED STRICTLY TO TEST BASIC MODEL USAGE!!!!!!!!!!!!!!
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))
from dataset import create_dataset
from model import train_model


def test_dataset():
    df = create_dataset()

    assert len(df) == 50
    assert "result" in df.columns

    print("Dataset test passed!")


def test_model_training():
    model, accuracy = train_model()

    assert model is not None
    assert 0 <= accuracy <= 1

    print("Model training test passed!")


def test_prediction():
    model, _ = train_model()

    sample = [[4, 85, 72, 9]]
    prediction = model.predict(
        __import__("pandas").DataFrame(
            sample,
            columns=[
                "study_hours",
                "attendance",
                "previous_marks",
                "assignments_completed"
            ]
        )
    )

    assert prediction[0] in ["Pass", "Fail"]

    print("Prediction test passed!")


if __name__ == "__main__":
    test_dataset()
    test_model_training()
    test_prediction()

    print("All tests completed successfully!")