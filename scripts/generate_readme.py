import os
import fnmatch


def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / 1024 ** 2:.2f} MB"
    else:
        return f"{size_bytes / 1024 ** 3:.2f} GB"


def load_gitignore_patterns(gitignore_path):
    ignore_patterns = set()
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignore comments and empty lines
                    ignore_patterns.add(line)
    return ignore_patterns


def is_ignored(item_path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(item_path, pattern) or fnmatch.fnmatch(os.path.basename(item_path), pattern):
            return True
    return False


def generate_tree_with_icons(directory, ignore_patterns, prefix=""):
    tree = ""
    items = sorted(os.listdir(directory))  # Sort for consistency

    for index, item in enumerate(items):
        item_path = os.path.join(directory, item)
        is_last = index == len(items) - 1  # Check if last item

        # Skip ignored files/folders
        if is_ignored(item_path, ignore_patterns):
            continue

        branch = "└── " if is_last else "│── "

        if os.path.isdir(item_path):
            tree += f"{prefix}{branch}📁 {item}/\n"
            tree += generate_tree_with_icons(item_path, ignore_patterns, prefix + ("    " if is_last else "│   "))
        else:
            file_size = format_size(os.path.getsize(item_path))  # Get file size
            tree += f"{prefix}{branch}📄 {item} ({file_size})\n"

    return tree

root_directory = "."  # Current directory
data_directory = os.path.join(root_directory, "data")
gitignore_path = os.path.join(root_directory, ".gitignore")

ignore_patterns = load_gitignore_patterns(gitignore_path)

if not os.path.exists(data_directory):
    print(f"⚠️ Error: The 'data/' directory does not exist. Checked path: {data_directory}")
    print(f"📂 Current working directory: {os.getcwd()}")
    print(f"📁 Folders found in {os.getcwd()}: {os.listdir(os.getcwd())}")
    exit()

folder_structure_data = f"```\n📁 data/\n" + generate_tree_with_icons(data_directory, ignore_patterns) + "```"

readme_path = os.path.join(data_directory, "data_exploration_and_cleaning_results.md")
with open(readme_path, "r", encoding="utf-8") as file:
    readme_content = file.read()

split_marker_start = "## 📂 data Directory Structure"
split_marker_end = "## 📌 Data Sources"

before_structure = readme_content.split(split_marker_start)[0]
after_structure = readme_content.split(split_marker_end)[1]

updated_readme_content = (
    f"{before_structure}{split_marker_start}\n{folder_structure_data}\n{split_marker_end}{after_structure}"
)

with open(readme_path, "w", encoding="utf-8") as file:
    file.write(updated_readme_content)

print("✅ data/data_exploration_and_cleaning_results.md has been updated, excluding ignored files from .gitignore!")