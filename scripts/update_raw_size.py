import os

# Define the root project directory (Sales-Insight)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths relative to the root directory
DATA_DIR = os.path.join(ROOT_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
README_PATH = os.path.join(DATA_DIR, "README.md")

def get_total_raw_size():
    """Calculates total size of all files in the raw/ folder."""
    total_size = 0
    if not os.path.exists(RAW_DIR):
        print(f"⚠️ Error: The 'raw/' directory does not exist. Checked path: {RAW_DIR}")
        return "0.00 MB"

    for root, _, files in os.walk(RAW_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)  # Get size in bytes
            else:
                print(f"⚠️ Warning: File not found: {file_path}")

    # Convert to MB with 2 decimal places
    return f"{total_size / (1024 * 1024):.2f} MB"

def update_readme():
    """Replaces '**Size:** X MB' in README.md with the total size of raw/ folder."""
    if not os.path.exists(README_PATH):
        print(f"⚠️ Error: README.md not found at {README_PATH}")
        return

    total_size = get_total_raw_size()

    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(README_PATH, "w", encoding="utf-8") as f:
        for line in lines:
            if "**Size:** X MB" in line and "data/raw/" in line:
                line = line.replace("**Size:** X MB", f"**Size:** {total_size}")
            f.write(line)

    print(f"✅ README.md updated: Total raw data size = {total_size}")

if __name__ == "__main__":
    update_readme()