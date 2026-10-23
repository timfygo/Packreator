import json
import os
import shutil
from pathlib import Path

print("Welcome to Packreator!")

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

def ensure_dir(path):
    path_obj = Path(path)
    path_obj.mkdir(exist_ok=True, parents=True)
    return path_obj

# Create assets folder
ensure_dir(f"{pack_name}/assets/minecraft")

print("Base structure complete!")

match (pack_type):
    case "AS":
        dest_custom_dir = ensure_dir(f"{pack_name}/assets/minecraft/sounds/custom")
        source_dir = Path(f"Your assets go here/Custom Sounds")
        destination_dir = Path(f"{pack_name}/assets/minecraft/sounds/")
        
        sounds_data = {}
        sound_folder = Path("Your assets go here/Custom Sounds")
        for file_path in sound_folder.iterdir():
            if file_path.is_file() and file_path.suffix == ".ogg":
                sound_name = file_path.stem
                clean_name = sound_name.replace(" ", "_").lower()
                sounds_data[clean_name] = {
                    "sounds": [
                        f"minecraft:custom/{clean_name}"
                    ]
                }
                new_file_dest = dest_custom_dir / f"{clean_name}.ogg"
                shutil.move(file_path, new_file_dest)
                print(f"Successfully moved {file_path.name}")
        with open(f"{pack_name}/assets/minecraft/sounds.json", "w") as f:
            json.dump(sounds_data, f, indent=2)
        print("Custom sound folder structure complete!")
    case "CS":
        ensure_dir(f"{pack_name}/assets/minecraft/sounds")
    case "CT":
        ensure_dir(f"{pack_name}/assets/minecraft/textures")
        texture_type = input("What will your pack retexture? Blocks, or items? ")
        if "block" in texture_type.lower():
            ensure_dir(f"{pack_name}/assets/minecraft/textures/block")
            texture_type = "block"
        elif "item" in texture_type.lower():
            ensure_dir(f"{pack_name}/assets/minecraft/textures/item")
            texture_type = "item"
        source_dir = Path(f"Your assets go here/{texture_type.capitalize()} textures")
        destination_dir = Path(f"{pack_name}/assets/minecraft/textures/{texture_type}")
        for item in source_dir.iterdir():
            if item.is_file():
                shutil.move(item, destination_dir / item.name)
print("Pack complete!")
