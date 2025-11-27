
#!/usr/bin/env python3

import os
import re
import time
import json
import sys
from pathlib import Path
from datetime import datetime

root = Path(__file__).parent.name


USE_DEFAULT = True


def is_ignored(path, ignore_list):
    """
    Return True if the given path should be ignored based on the ignore list.
    Supports both substring and regex patterns (case-insensitive).
    """
    p = Path(path)
    lower_path = str(p).lower()
    name = p.name.lower()
    stem = p.stem.lower()

    for pattern in ignore_list:
        pat = str(pattern).strip().lower()
        if not pat:
            continue

        # Simple substring match (for .git, node_modules, etc.)
        if pat in lower_path:
            return True

        # Try regex match (against full name and stem)
        try:
            if (
                re.fullmatch(pat, name, re.IGNORECASE)
                or re.fullmatch(pat, stem, re.IGNORECASE)
            ):
                return True
        except re.error:
            # Ignore invalid regex patterns
            pass

    return False



# Terminal color codes
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"


DEFAULT_CONFIG = {
    "input": ".",
    "output": "flat",
    "format": "md",
    "theme": "default",
    "ignore": [
        "node_modules", ".git", ".vscode", ".astro", "dist" , "__pycache__", ".svg",
        "flatshot.py", "flatConf.config",
        r"^flat-[\w\-]+(?:\(\d+\))?(?:-\d{4}-\d{2}-\d{2}_\d{2}-\d{2})?\.md$"

    ],
    "only_formats": ["html", "css", "js"],
    "enable_only_formats": False,
    "include_tree": True,
    "max_size": 2 * 1024 * 1024,
    "naming": "incremental"
}




# ───────────────────────────────
# Config file helpers
# ───────────────────────────────
def create_default_config(path="flatConf.config"):
    """Create default config file if not found."""
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(r"""
# flatshot configuration file
# Default configuration is safe and optimized for most projects.
# Edit values as needed. Save and rerun flatshot.

input = .
output = flat
format = md
theme = default
ignore = node_modules, .git, flatshot.py, flatConf.config, .vscode, ^flat-[\w\-]+(?:\(\d+\))?(?:-\d{4}-\d{2}-\d{2}_\d{2}-\d{2})?\.md$
max_size = 2MB
only_formats = html, css, js
enable_only_formats = false
include_tree = true
naming = incremental

naming_mode = incremental 
#alternative naming methods: timestamp | incremental | overwrite
""")
        print(f"{C.YELLOW}⚙️  flatConf.config created.{C.RESET}")
        print(f"{C.DIM}Default configuration is designed to be fast and ignore large files.{C.RESET}")
        print(f"Press {C.BOLD}Y{C.RESET} to continue with default settings, or {C.BOLD}N{C.RESET} to halt and edit flatConf.config.")
        choice = input("> ").strip().lower()
        if choice != "y":
            print(f"{C.CYAN}🛑 Process halted. You can edit flatConf.config manually.{C.RESET}")
            exit(0)
    else:
        print(f"{C.CYAN}⚙️ Using flatConf.config{C.RESET}")


def parse_config_file(path):
    """Parse .config files with key=value syntax."""
    conf = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(("#", ";")):
                continue
            if "=" in line:
                key, value = map(str.strip, line.split("=", 1))

                # Handle booleans
                if value.lower() in ["true", "false"]:
                    value = value.lower() == "true"

                # Handle human-readable sizes (e.g. "2MB")
                elif re.match(r"^[0-9]", value):
                    match = re.match(r"^([0-9.]+)\s*(kb|mb|gb)?$", value.lower())
                    if match:
                        num = float(match.group(1))
                        unit = match.group(2) or ""
                        mult = {"kb": 1024, "mb": 1024**2, "gb": 1024**3}.get(unit, 1)
                        value = int(num * mult)

                # Handle lists
                elif "," in value:
                    value = [v.strip() for v in value.split(",")]

                conf[key] = value
    return conf


def load_config():
    """Load config with defaults."""
    config = DEFAULT_CONFIG.copy()
    if not USE_DEFAULT:
        create_default_config()
        config.update(parse_config_file("flatConf.config"))
    else:
        print(f"{C.CYAN}⚙️  Using internal default configuration (flatConf.config ignored).{C.RESET}")
    return config



# ───────────────────────────────
# File system helpers
# ───────────────────────────────
def list_files(root, config):
    """Recursively gather all files to bundle, excluding ignored ones."""
    ignore = config["ignore"]
    collected = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        # Skip the output file itself and any similar SnapFold outputs
        if is_ignored(path, ignore):
            continue
        if re.fullmatch(r"^SnapFold(?:\(\d+\))?(?:\..+)?$", path.name, re.IGNORECASE):
            continue
        if path.resolve() == root:
            continue

        # File too large
        if path.stat().st_size > config["max_size"]:
            continue

        # Restrict to certain formats
        if config["enable_only_formats"]:
            ext = path.suffix.lstrip(".").lower()
            if ext not in config["only_formats"]:
                continue

        collected.append(path)

    return collected





def get_output_path(config):
    """Determine output path based on naming_mode."""
    out = Path(config["output"]).resolve()
    format = str(config.get("format")).lower()
    folder = out.parent
    stem = out.stem
    folder.mkdir(parents=True, exist_ok=True)
    ext = ".md"

    if USE_DEFAULT:
        naming_mode = str("incremental").lower()
        
    else:
        naming_mode = str(config.get("naming_mode")).lower()

    if naming_mode == "incremental":
        i = 1
        final_path = folder / f"{stem}-{root}{ext}"
        while final_path.exists():
            i += 1
            final_path = folder / f"{stem}-{root}({i}){ext}"
        return final_path

    elif naming_mode == "timestamp":
        ts = datetime.now().strftime("%Y-%m-%d_%H-%M")
        return folder / f"{stem}-{root}-{ts}{ext}"
    
    elif naming_mode == "overwrite":
        return folder / f"{stem}-{root}-{ext}"
    

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M")
    return folder / f"{stem}-{root}-{ts}{ext}"

# ───────────────────────────────
# Output helpers
# ───────────────────────────────
def generate_tree(root, files):
    """Generate folder tree view."""
    tree = {}
    for f in files:
        rel = Path(f).relative_to(root)
        parts = rel.parts
        cur = tree
        for p in parts[:-1]:
            cur = cur.setdefault(p, {})
        cur[parts[-1]] = None

    def render(subtree, prefix=""):
        out = ""
        for i, (name, val) in enumerate(sorted(subtree.items())):
            connector = "└── " if i == len(subtree) - 1 else "├── "
            out += prefix + connector + name + "\n"
            if isinstance(val, dict):
                ext = "    " if i == len(subtree) - 1 else "│   "
                out += render(val, prefix + ext)
        return out

    return render(tree)


def bundle_files(files, root, config):
    """Bundle all files into one markdown."""
    md = "# 📦 flatshot Project Snapshot\n\n"
    md += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    if config["include_tree"]:
        md += "## raw structure\n"
        md += "```\n" + generate_tree(root, files) + "```\n\n"

    for f in files:
        rel = Path(f).relative_to(root)
        md += f"---\n### `{rel}`\n```{f.suffix.lstrip('.')}\n"
        try:
            content = Path(f).read_text(encoding="utf-8")
        except Exception as e:
            content = f"[Error reading file: {e}]"
        md += content + "\n```\n\n"

    return md


def save_output(md, config):
    """Save markdown to file."""
    path = get_output_path(config)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"\n{C.GREEN}✨ Output saved as:{C.RESET} {C.BOLD}{path.name}{C.RESET}")
    print(f"{C.DIM}📂 {path.parent}{C.RESET}")

    return path

# ───────────────────────────────
# Progress bar
# ───────────────────────────────
def progress_bar(current, total, width=30):
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    percent = (current / total) * 100
    print(f"\r{C.RED}🚀 flatshot running... [{bar}] {percent:5.1f}%", end="", flush=True)

# ───────────────────────────────
# Main execution
# ───────────────────────────────
def main():
    start_time = time.time()
    config = load_config()
    root = Path(config["input"]).resolve()
    files = list_files(root, config)
    total = len(files)
    for i, _ in enumerate(files, 1):
        progress_bar(i, total)
        time.sleep(0.01)  # Smooth animation

    md = bundle_files(files, root, config)
    save_output(md, config)

    elapsed = time.time() - start_time
    print(f"{C.BOLD}⏱️  Completed in {elapsed:.2f} seconds{C.RESET}\n")

# CLI arguments
# -c: create new config file or use existing one
# -r: recreates the config and runs the code using new config

if "--reset" in sys.argv or "-r" in sys.argv:
    conf_path = Path("flatConf.config")
    if conf_path.exists():
        os.remove("flatconf.config")
        time.sleep(0.05)  # tiny delay ensures filesystem refresh
        print(f"{C.YELLOW}♻️  flatConf.config deleted. {C.RESET}")
        create_default_config()

if "--config" in sys.argv or "-c" in sys.argv:
    USE_DEFAULT = False

if __name__ == "__main__":
    main()
    print(root)

'''
🧭 Content & Output Enhancements

Table of Contents generation – auto-create a clickable section list for large snapshots.

Syntax highlighting – embed Markdown code blocks with language tags and optional color themes.

Preview mode – open the final .md file in a browser or VS Code preview automatically.

Compression or minify option – collapse long lines or strip comments for lighter output.

Diff snapshots – compare two generated flatshots and show what changed between versions.

Multiple output formats – export as HTML, PDF, or plain text besides Markdown.

Metadata header – include project name, size summary, and file counts at the top.

⚙️ Configuration & UX

CLI arguments override config – e.g., flatshot --output myfile.md --theme dark.

Profiles or presets – e.g., “docs mode”, “light mode”, “full source mode”.

Interactive setup wizard – first-run prompt to customize config easily.

Verbose / quiet modes – control how much info prints during run.

Automatic config migration – update old configs when the schema changes.

🧩 File Handling & Intelligence

File grouping or sorting – group by type (HTML, CSS, JS) or by folder depth.

Include/exclude by glob pattern – more powerful than regex (like *.css, **/tests/*).

Checksum cache – skip unchanged files to speed up repeated runs.

Parallel reading – multi-threaded or async file reading for big projects.

Detect binary files – skip images or binaries automatically.

🎨 Themes & Presentation

Custom themes – template-based output, e.g., “technical doc”, “code archive”, “minimal”.

Add file size & date info – annotate each file block with its size and last-modified time.

Tree collapsibility – generate collapsible Markdown (GitHub-style folding sections).

🌐 Integration

Git integration – show current branch, latest commit, and ignored files via .gitignore.

VS Code extension hook – “Generate Flatshot” command from the editor.

GitHub Action support – auto-generate flatshots on push or release.

Web UI wrapper – small local web app to configure and preview before export.

💡 Quality of Life

Auto-update checker – notify if a newer Flatshot version exists.

Logging & diagnostics – write a flatshot.log for debugging.

Undo / cleanup option – delete last generated flatshot files with one command.

Progress time estimate – show ETA while bundling.

Color theme customization – light/dark terminal modes.

Easter egg – maybe an ASCII art logo or a fun message on completion 🎉
'''