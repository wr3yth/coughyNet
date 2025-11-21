import os
import shutil

# ROOT folder of your wiki (change if needed)
ROOT = "src/wiki"

def duplicate_md_files():
    for root, _, files in os.walk(ROOT):
        for file in files:
            # Only target English files (*.md but not *.fa.md)
            if file.endswith(".md") and not file.endswith(".fa.md"):
                
                original_path = os.path.join(root, file)
                fa_filename = file.replace(".md", ".fa.md")
                fa_path = os.path.join(root, fa_filename)

                # If .fa.md already exists, skip
                if os.path.exists(fa_path):
                    print(f"[SKIP] Already exists: {fa_path}")
                    continue

                # Duplicate the file
                shutil.copy2(original_path, fa_path)
                print(f"[CREATE] {fa_path}")

    print("✅ Done duplicating .md → .fa.md files.")

if __name__ == "__main__":
    duplicate_md_files()
