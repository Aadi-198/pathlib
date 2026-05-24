from pathlib import Path

home = Path.home()

running = True
while running:
    folder = str(input("Which folder you want to sort (downloads / documents) ? \nTo exit type s \n")).lower().strip()

    if folder.startswith("down"):
        target_path = home / "Downloads"
        print(f"\nYour downloads folder is: {target_path}\n")
        running = False
    elif folder.startswith("doc"):
        target_path = home / "Documents"
        print(f"\nYour documents folder is: {target_path}\n")
        running = False
    elif folder.startswith("s"):
        print("Exiting Program... \nBye")
        running = False
    else:
        print("Try again")