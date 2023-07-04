import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from models.X_model import XModel

def transformData(data : XModel):

    old_df = pd.read_csv("./cleaned_dataset.csv").drop(columns=["Unnamed: 0", "title"])

    # insert the record to be predicted so that it can be transformed along with the other records

    new_row = pd.DataFrame({
        "drug_id": [data.drug_id],
        "status": [data.status],
        "points": [data.points],
        "vector": [data.vector],
        "safety_met": [data.safety_met],
        "efficacy_met": ["No"],
        "administration_therapeutic_route ": [data.route],
        "administration_therapeutic_area": [data.area],
        "phases": [data.phase],
        "primary_completion": [data.completion]
    })

    df = pd.concat([old_df, new_row], ignore_index=True)

    # Labling the data
    encoder = LabelEncoder()

    data_before = df.efficacy_met
    data_to_label = df.efficacy_met

    df.efficacy_met = encoder.fit_transform(data_to_label)
    df.safety_met = encoder.fit_transform(data_to_label)


    pd.DataFrame({
        "Label" : data_before,
        "Label When Encoded": df.efficacy_met
    }).head(3)

    # one hot encoding the data
    df = pd.get_dummies(df, columns=[
        "status", "administration_therapeutic_route ", "administration_therapeutic_area",
        "phases", "vector", "drug_id"
    ])

    # Spliting the data
    X = df.drop(columns=["efficacy_met"])
    y = df.efficacy_met

    # Select only the record we want to analyse
    X_len = len(X) - 1

    for x in range(0, X_len):
        X.drop(index=x, inplace=True)

    # Return the model
    return X