hsl_color = lambda h, s, l: f"\033[38;2;{int((lambda n: l/100 - (s/100 * min(l/100, 1 - l/100)) * max(-1, min(n - 3, 9 - n, 1)))((h / 60 + 0) % 6)*255)};{int((lambda n: l/100 - (s/100 * min(l/100, 1 - l/100)) * max(-1, min(n - 3, 9 - n, 1)))((h / 60 + 8) % 6)*255)};{int((lambda n: l/100 - (s/100 * min(l/100, 1 - l/100)) * max(-1, min(n - 3, 9 - n, 1)))((h / 60 + 4) % 6)*255)}m"


from pathlib import Path

current_path = Path.cwd()
print()
print(f"{hsl_color(260, 100, 60)}{current_path}\033[0m is the current working path !")
print()

new_folder = Path.cwd() / "New_Folder"
new_folder.mkdir(parents=True, exist_ok=True)

current_path = Path.cwd() / new_folder

new_file = current_path / "test.txt"
new_file.write_text("Hello")
print(f"Does it exist now? {new_file.exists()}")

empty_file= current_path / "empty.txt"
empty_file.touch()

current_path = current_path.parent