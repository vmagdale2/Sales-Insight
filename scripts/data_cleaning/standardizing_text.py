drive_path = "/content/drive/My Drive/Redacted"

file_mappings = {
    "product_names.csv": "product_names_3.csv",
    "city_names_1_numbers_cleaned.csv": "city_names_3.csv",
    "store_names.csv": "store_names_3.csv"
}


def clean_spaces(df):
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

def clean_multiple_spaces(df):
    return df.applymap(lambda x: ' '.join(x.split()) if isinstance(x, str) else x)

for original_file, new_file in file_mappings.items():
    file_path = os.path.join(drive_path, original_file)
    new_file_path = os.path.join(drive_path, new_file)

    try:
        df = pd.read_csv(file_path, dtype=str)
        print(f"🔹 Processing: {original_file}")

        df = clean_spaces(df)

        if original_file == "store_names.csv":
            df = clean_multiple_spaces(df)

        df.to_csv(new_file_path, index=False)
        print(f"✅ Cleaned and saved: {new_file}")

    except FileNotFoundError:
        print(f"❌ Error: File {original_file} not found. Skipping...")
    except Exception as e:
        print(f"❌ Error processing {original_file}: {e}")

print("\n🎉 All applicable files have been processed successfully!")