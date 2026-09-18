#The modules used
import pandas as pd
from pathlib import Path
def create_dataset():
    """This creates teh dataaset of students"""
    data={
        "study_hours": [1,2,3,4,5,6,7,8,9],
        "attendance": [60,65,70,75,80,85,90,95,100],
        "sleep_hours": [5,6,7,8,6,7,8,7,8],
        "marks": [35,42,50,58,65,72,80,88,95]
    }
    df=pd.DataFrame(data)
    return df
if __name__ == "__main__":
    df=create_dataset()
    output_pathway=Path(__file__).resolve().parent/"student_data.csv"
    df.to_csv(output_pathway,index=False)
    print("Daaset crated")
    print("It is sved at:",output_pathway)
    print("Stdent Datset:")
    print(df)