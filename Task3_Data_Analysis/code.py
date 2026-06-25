import pandas as pd
import numpy as np
import os

def main():
    
    data = {
        "Product": ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "Gaming Chair", "Gaming Desk", "Gaming Sofa"],
        "Category": ["Consoles", "Consoles", "Consoles", "Furniture", "Furniture", "Furniture"],
        "Sales": [48000.0, 32000.0, None, 12000.0, 14000.0, 24000.0]
    }

    df = pd.DataFrame(data)
    
    
    df.to_csv("sales_data.csv", index=False)
  
    print("Files in workspace directory:")
    print(os.listdir())
    print("-" * 65)

    df = pd.read_csv("sales_data.csv")
    print("Initial Dataframe Extraction:")
    print(df)
    print("-" * 65)

    print("Dataset Structural Information:")
    df.info()
    print("-" * 65)

    print("Descriptive Statistical Breakdown:")
    print(df.describe())
    print("-" * 65)

    print("Missing Field Counts Per Matrix Column:")
    print(df.isnull().sum())
    print("-" * 65)

    df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
    print("Dataframe After Reconciling Missing Values:")
    print(df)
    print("-" * 65)

    high_sales = df[df["Sales"] > 20000]
    print("Filtered Target Records (Sales > 20000):")
    print(high_sales)
    print("-" * 65)

    print("Department Cumulative Sums:")
    print(df.groupby("Category")["Sales"].sum())
    print("-" * 65)

    print("Comprehensive Statistical Aggregation Breakdown By Category:")
    aggregated_metrics = df.groupby("Category").agg({
        "Sales": ["sum", "mean", "max"]
    })
    print(aggregated_metrics)
    print("=================================================================")

if __name__ == "__main__":
    main()
