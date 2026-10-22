from pathlib import Path


def test_main_file_exists():
    assert Path("main.py").is_file()


def test_project_folders_exist():
    expected_folders = [
        "data",
        "models",
        "experiments",
        "results",
        "notebooks",
        "demo",
        "report",
        "tests",
        "docs",
    ]

    for folder in expected_folders:
        assert Path(folder).is_dir(), f"Missing folder: {folder}"
