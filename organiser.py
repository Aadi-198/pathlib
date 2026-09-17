import time
import shutil
from pathlib import Path

from config import extension_map

home = Path.home()

size = shutil.get_terminal_size()
column_size = size.columns - 1
seps = (column_size * '-')

target_path = None

running = True
while running:
    print(seps)
    folder = str(input("Which folder you want to sort (downloads / documents / custom) ? \nTo exit type s \n")).lower().strip()

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
    elif folder.startswith("c"):
        print(seps)
        user_path = str(input("Enter you custom absolute path \n")).strip()
        target_path = Path(user_path).expanduser().resolve()
        print(seps)
        print(f"\nTarget folder set to: {target_path}\n")
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
        time.sleep(0.40)

        total_files = 0
        moved_files = 0
        unique_extensions = set()

        for item in target_path.iterdir():
            if item.is_dir():
                continue

            total_files += 1
            file_ext = item.suffix.lower()

            if file_ext:
                unique_extensions.add(file_ext)

                folder_name = extension_map.get(file_ext, "Others")
                
                destination_dir = target_path / folder_name
                
                destination_dir.mkdir(exist_ok=True)
                
                final_destination = destination_dir / item.name
                
                try:
                    item.rename(final_destination)
                    print(f"Moved: {item.name} to {folder_name}/")
                    moved_files += 1
                except Exception as e:
                    print(f" Could not move {item.name}: {e}")
        print(f"Scan Completed !")
        time.sleep(0.60)
        print(f"{total_files} loose files found")
        time.sleep(0.40)
        print(f"Unique file extensions detected : {', '.join(unique_extensions) if unique_extensions else 'None'}\n")
        print(seps)

    else:
        print("This path doesn't exist on your machine !")