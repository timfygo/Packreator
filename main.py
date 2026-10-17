import json
import os
from pathlib import Path

print("Welcome to packreator!")
pack_name = input("What will the name of your pack be? ")
pack_version = input("What version of Minecraft will it be for? (No snapshots or april fools) ")
pack_description = input("Description? ")

current_directory = Path(pack_name)
file_path = current_directory / "pack.mcmeta"

# 1. Load the file
with open("formats.json", "r") as file:
    formats = json.load(file)

format = formats.get(pack_version)

if format is not None:
    mcmeta = {
  "pack": {
    "min_format": 88,
    "max_format": 88,
    "description": pack_description
  }
}

current_directory.mkdir(parents=True, exist_ok=True)
with open(file_path, "w") as f:
    json.dump(mcmeta, f, indent=2)

print("Complete!")
