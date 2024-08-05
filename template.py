import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "Brain_Tumor_Detection-Classification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    path = Path(filepath)
    if path.parent != "":
        path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {path.parent} for the file: {path.name}")

    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f"Creating empty file: {path}")
    else:
        logging.info(f"{path.name} already exists")
