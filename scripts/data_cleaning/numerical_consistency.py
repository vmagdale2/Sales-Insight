import pandas as pd
import os
#Redacted
drive_folder = "/content/drive/My Drive/Redacted"


file_names = ["city_names_1", "product_hierarchy_1", "sales_1_date_formatted"]

for file_name in file_names:
    input_file_path = os.path.join(drive_folder, f"{file_name}.csv")
    output_file_path = os.path.join(drive_folder, f"{file_name}_numbers_cleaned.csv")

    df = pd.read_csv(input_file_path)

    num_cols = df.select_dtypes(include=['number']).columns

    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].round(2)

    df.to_csv(output_file_path, index=False)

    print(f"✅ Cleaned file saved: {output_file_path}")