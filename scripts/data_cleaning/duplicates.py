def check_duplicates(file_path):
    df = pd.read_csv(file_path)
    total_rows = df.shape[0]
    duplicate_rows = df.duplicated().sum()

    print(f"File: {os.path.basename(file_path)}")
    print(f"Total Rows: {total_rows}")
    print(f"Duplicate Rows: {duplicate_rows}")
    print("-" * 40)

    return duplicate_rows

for file_name in file_names:
    file_path = os.path.join(drive_path, file_name)
    check_duplicates(file_path)