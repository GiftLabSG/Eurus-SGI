import os

# Replace with the correct path to your manual HTML directory
manual_scrapes = "/workspaces/Eurus-SGI/data/manual_scrapes"

# List all .html files
html_files = sorted(f for f in os.listdir(manual_scrapes) if f.endswith(".html"))

for f in html_files:
    print(f)
