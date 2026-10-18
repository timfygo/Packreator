import json
import os
import shutil
from pathlib import Path

print("Welcome to packreator!")

pack_name = input("What will the name of your pack be? ")
pack_version = input("What version of Minecraft will it be for? (No snapshots or april fools) ")
pack_description = input("What description will the pack have? ")
pack_type = input("Will the pack add sounds, change sounds, or change textures? Answer only AS, CS, or CT ")

current_directory = Path(pack_name)
file_path = current_directory / "pack.mcmeta"

with open("formats.json", "r") as file:
    formats = json.load(file)

format = formats.get(pack_version)

if format is not None:
    mcmeta = {
  "pack": {
    "min_format": format,
    "max_format": format,
    "description": pack_description
  }
}
# Create mcmeta and base folder
current_directory.mkdir(parents=True, exist_ok=True)
with open(file_path, "w") as f:
    json.dump(mcmeta, f, indent=2)

# Create assets folder
Path(f"{pack_name}/assets/minecraft").mkdir(parents=True, exist_ok=True)

print("Base structure complete!")

match (pack_type):
    case "AS":
        Path(f"{pack_name}/assets/minecraft/sounds/custom").mkdir(parents=True, exist_ok=True)
    case "CS":
        Path(f"{pack_name}/assets/minecraft/sounds")
    case "CT":
        Path(f"{pack_name}/assets/minecraft/textures")
        texture_type = input("What will your pack retexture? Blocks, or items? ")
        if "block" in texture_type.lower():
            Path(f"{pack_name}/assets/minecraft/textures/block")
        elif "item" in texture_type.lower():
            Path(f"{pack_name}/assets/minecraft/textures/item")
            
