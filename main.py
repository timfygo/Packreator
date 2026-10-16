import os
from pathlib import Path

print("Welcome to packreator!")
pack_name = input("What will the name of your pack be?")
pack_version = input("What version of Minecraft will it be for? (No snapshots or april fools)")

folder_path = Path(pack_name)
file_path = folder_path / "pack.mcmeta"

folder_path.mkdir(pack_name)
with open(file_path, "w") as f:
    f.write("")
