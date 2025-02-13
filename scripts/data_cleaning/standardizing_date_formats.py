file_id = "REDACTED"
output_path = "sales_1_date_formatted.csv"
gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)
sales_to_be_date_formatted = pd.read_csv(output_path)

if "date" in sales_to_be_date_formatted.columns:
    sales_to_be_date_formatted["date"] = pd.to_datetime(sales_to_be_date_formatted["date"], errors="coerce", dayfirst=False)
    sales_to_be_date_formatted["date"] = sales_to_be_date_formatted["date"].dt.strftime("%m/%d/%y")

cleaned_file_path = "sales_1_date_formatted.csv"
sales_to_be_date_formatted.to_csv(cleaned_file_path, index=False)

print(f"Full dataset saved with standardized 'date' column: {cleaned_file_path}")

#Redacted
drive_folder = "/content/drive/My Drive/Redacted"

os.makedirs(drive_folder, exist_ok=True)
cleaned_file_path = os.path.join(drive_folder, "sales_1_date_formatted.csv")
sales_to_be_date_formatted.to_csv(cleaned_file_path, index=False)

print(f"File saved to Google Drive: {cleaned_file_path}")