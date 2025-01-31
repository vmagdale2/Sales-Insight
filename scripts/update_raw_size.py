import os

# Paths
DATA_DIR = "data"
RAW_DIR = os.path.join(DATA_DIR, "raw")
README_PATH = os.path.join(DATA_DIR, "README.md")

def get_total_raw_size():
    """Calculates total size of all files in the raw/ folder."""
    total_size = 0
    for root, _, files in os.walk(RAW_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)  # Get size in bytes

    # Convert to MB with 2 decimal places
    return f"{total_size / (1024 * 1024):.2f} MB"

def update_readme():
    """Replaces 'Size: X MB' in README.md with the total size of raw/ folder."""
    if not os.path.exists(README_PATH):
        print("README.md not found!")
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
