import os
import shutil
import yaml

# CHANGE THIS if your path is different
ROOT = "src/wiki"

def extract_frontmatter(file_path):
    """
    Extract YAML frontmatter from a markdown file.
    Returns a dict or None.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].strip().startswith("---"):
        return None

    yaml_lines = []
    for line in lines[1:]:
        if line.strip().startswith("---"):
            break
        yaml_lines.append(line)

    try:
        return yaml.safe_load("".join(yaml_lines))
    except Exception as e:
        print(f"[WARN] Could not parse YAML in {file_path}: {e}")
        return None


def categorize_files():
    for root, _, files in os.walk(ROOT):
        for file in files:
            if not file.endswith(".md"):
                continue

            full_path = os.path.join(root, file)

            # Skip files already inside a category folder
            # (ROOT/category/file.md → category already done)
            rel_path = os.path.relpath(full_path, ROOT)
            if os.path.dirname(rel_path) != "":
                continue

            front = extract_frontmatter(full_path)
            if not front:
                print(f"[SKIP] No frontmatter: {file}")
                continue

            category = front.get("category")
            if not category:
                print(f"[SKIP] No category in: {file}")
                continue

            # Create category folder if missing
            category_folder = os.path.join(ROOT, category)
            if not os.path.exists(category_folder):
                print(f"[CREATE] Folder: {category_folder}")
                os.makedirs(category_folder, exist_ok=True)

            # Move file
            new_path = os.path.join(category_folder, file)

            print(f"[MOVE] {file} → {category}/")
            shutil.move(full_path, new_path)


if __name__ == "__main__":
    print("📂 Running Wiki Categorizer…")
    categorize_files()
    print("✅ Done.")
