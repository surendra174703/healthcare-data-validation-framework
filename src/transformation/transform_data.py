import pandas as pd

def transform_data(input_path, output_path):
    df = pd.read_csv(input_path)

    print("Initial row count:", len(df))

    # 🔹 Remove duplicates
    df = df.drop_duplicates()

    # 🔹 Remove null BMI values
    df = df[df["bmi"].notnull()]

    # 🔹 Business rule: age should be > 0
    df = df[df["age"] > 0]

    print("Final row count after cleaning:", len(df))

    # Save processed data
    df.to_csv(output_path, index=False)

    print("Data transformation completed and saved.")


if __name__ == "__main__":
    transform_data(
        "data/raw/healthcare_data.csv",
        "data/processed/processed_healthcare_data.csv"
    )

