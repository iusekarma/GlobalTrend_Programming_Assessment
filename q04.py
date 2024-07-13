import pandas as pd


def clean_and_preprocess(df):
    for column in df.columns:
        if df[column].dtype in ["int64", "float64"]:
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna(df[column].mode()[0], inplace=True)

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[num_cols] = (df[num_cols] - df[num_cols].mean()) / df[num_cols].std()

    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    df = pd.get_dummies(df, columns=cat_cols)

    return df


if __name__ == "__main__":

    # Dummy Data
    data = {
        "age": [25, 30, 35, None, 40],
        "salary": [50000, 60000, 70000, 80000, None],
        "city": ["New York", "Los Angeles", "New York", "San Francisco", None],
    }

    df = pd.DataFrame(data)
    print("Original Data:")
    print(df)

    df_cleaned = clean_and_preprocess(df)
    print("\nCleaned & Preprocessed Data:")
    print(df_cleaned)
