import time
import shutil
from pathlib import Path

home = Path.home()

size = shutil.get_terminal_size()
column_size = size.columns
seps = (column_size * '-')

running = True
while running:
    print(seps)
    folder = str(input("Which folder you want to sort (downloads / documents) ? \nTo exit type s \n")).lower().strip()

    if folder.startswith("dow"):
        target_path = home / "Downloads"
        print(seps)
        print(f"\nYour downloads folder is: {target_path}\n")
        running = False
    elif folder.startswith("doc"):
        target_path = home / "Documents"
        print(seps)
        print(f"\nYour documents folder is: {target_path}\n")
        running = False
    elif folder.startswith("s"):
        print("Exiting Program... \nBye")
        print(seps)
        running = False
        continue
    else:
        print("Try again")
        continue

    if target_path and target_path.exists():
        print(f"Scanning {target_path} ...")

        total_files = 0
        unique_extensions = set()

        for item in target_path.iterdir():
            if item.is_dir():
                continue

            total_files += 1

            if item.suffix:
                unique_extensions.add(item.suffix.lower())

        print(f"Scan Completed !")
        time.sleep(0.60)
        print(f"{total_files} loose files found")
        time.sleep(0.40)
        print(f"Unique file extetions detected : {', '.join(unique_extensions) if unique_extensions else 'None'}\n")
        print(seps)

    else:
        print("This path doesn't exist on your machine !")