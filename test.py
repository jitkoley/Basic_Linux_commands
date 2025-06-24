import os
import json
import shutil
from typing import Dict, List


class ModelCopyError(Exception):
    """Custom exception for model copy errors."""

    pass


class ModelCopier:
    def __init__(self, source_dir: str, dest_dir: str, json_path: str):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.json_path = json_path

        if not os.path.isdir(self.source_dir):
            raise ModelCopyError(f"Source directory does not exist: {self.source_dir}")
        os.makedirs(self.dest_dir, exist_ok=True)

    def load_model_map(self) -> List[Dict[str, str]]:
        """Load the model name mappings from JSON."""
        try:
            with open(self.json_path, "r") as file:
                data = json.load(file)
            return data.get("models_name", [])
        except FileNotFoundError:
            raise ModelCopyError(f"JSON file not found: {self.json_path}")
        except json.JSONDecodeError as e:
            raise ModelCopyError(f"Invalid JSON format: {e}")

    def copy_and_rename_models(self):
        """Copy and rename model files based on the JSON mappings."""
        model_mappings = self.load_model_map()

        for mapping in model_mappings:
            for old_name, new_name in mapping.items():
                src_path = os.path.join(self.source_dir, old_name)
                dst_path = os.path.join(self.dest_dir, new_name)

                try:
                    if not os.path.isfile(src_path):
                        print(f"[WARN] Source file not found: {src_path}")
                        continue

                    shutil.copy2(src_path, dst_path)
                    print(f"[INFO] Copied: {old_name} ➜ {new_name}")
                except Exception as e:
                    print(f"[ERROR] Failed to copy {old_name} ➜ {new_name}: {e}")


if __name__ == "__main__":
    # Define paths
    SOURCE_DIR = r"D:\project\Automation\model_download\models"
    DEST_DIR = r"D:\project\Automation\model_download\edited_models"
    JSON_FILE = r"D:\project\Automation\model_download\model_map.json"

    try:
        copier = ModelCopier(SOURCE_DIR, DEST_DIR, JSON_FILE)
        copier.copy_and_rename_models()
    except ModelCopyError as e:
        print(f"[FATAL] {e}")
    except Exception as ex:
        print(f"[UNEXPECTED ERROR] {ex}")
