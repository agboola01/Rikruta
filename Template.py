import os
from pathlib import Path
import logging

list_of_files = [
    ".github/workflows/ci.yaml",
    ".github/workflows/cd.yaml",
    "src/__init__.py",
    "src/data_processing/__init__.py",
    "src/data_processing/data_injestion.py",
    "src/data_processing/preprocess.py",
    "src/data_processing/feature_engineering.py",
    "src/models/__init__.py",
    "src/models/model_train.py",
    "src/models/model_evaluation.py",
    "src/inference/__init__.py",
    "src/inference/predict.py",
    "src/deployment/__init__.py",
    "src/deployment/app.py",
    "src/deployment/Dockerfile",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/README.md",
    "notebooks/01_data_exploration.ipynb",
    "notebooks/02_training_evaluation.ipynb",
    "notebooks/03_inference_tests.ipynb",
    "scripts/train_model.sh",
    "scripts/preprocess_data.sh",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/intg.py",
    "config/config.yaml",
    "config/model_config.json",
    "config/logging_config.json",
    "docs/requirements.md",
    "docs/design_doc.md",
    "docs/user_manual.md",
    "docs/API_documentation.md",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f"creating directory:{filedir} for file: {filename}")

    if (not os.path.exists(filepath))  or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            print(" ")