"""Module to copy and rename model files based on a JSON mapping."""

import os
import json
import shutil
import logging
from typing import Dict, List


class ModelCopyError(Exception):
    """Custom exception for model copy errors."""

    pass


class ModelCopier:
    """Handles copying and renaming model files based on a JSON configuration."""

    def __init__(self, source_dir: str, dest_dir: str, json_path: str) -> None:
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.json_path = json_path

        if not os.path.isdir(self.source_dir):
            raise ModelCopyError(f"Source directory does not exist: {self.source_dir}")
        os.makedirs(self.dest_dir, exist_ok=True)

    def load_model_map(self) -> List[Dict[str, str]]:
        """Load the model name mappings from a JSON file.

        Returns:
            A list of dictionaries with original and new filenames.

        Raises:
            ModelCopyError: If the JSON file is missing or improperly formatted.
        """
        try:
            with open(self.json_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data.get("models_name", [])
        except FileNotFoundError as exc:
            raise ModelCopyError(f"JSON file not found: {self.json_path}") from exc
        except json.JSONDecodeError as exc:
            raise ModelCopyError(f"Invalid JSON format: {exc}") from exc

    def copy_and_rename_models(self) -> None:
        """Copy and rename model files based on the JSON mappings."""
        model_mappings = self.load_model_map()

        for mapping in model_mappings:
            for old_name, new_name in mapping.items():
                src_path = os.path.join(self.source_dir, old_name)
                dst_path = os.path.join(self.dest_dir, new_name)

                try:
                    if not os.path.isfile(src_path):
                        logging.warning("Source file not found: %s", src_path)
                        continue

                    shutil.copy2(src_path, dst_path)
                    logging.info("Copied: %s ➜ %s", old_name, new_name)
                except (OSError, shutil.SameFileError) as exc:
                    logging.error("Failed to copy %s ➜ %s: %s", old_name, new_name, exc)


def main() -> None:
    """Main execution function."""
    source_dir = r"D:\project\Automation\model_download\models"
    dest_dir = r"D:\project\Automation\model_download\edited_models"
    json_file = r"D:\project\Automation\model_download\model_map.json"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        copier = ModelCopier(source_dir, dest_dir, json_file)
        copier.copy_and_rename_models()
    except ModelCopyError as exc:
        logging.critical("Fatal error: %s", exc)
    except Exception as exc:
        logging.exception("Unexpected error: %s", exc)


if __name__ == "__main__":
    main()
