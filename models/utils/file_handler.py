from __future__ import annotations
from pathlib import Path


class PathHandler:

    _instance = None

    def __new__(cls) -> PathHandler:
        if cls._instance is None:
            cls._instance = super(PathHandler, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def is_valid_type(path) -> bool:
        if isinstance(path, str) or isinstance(path, Path):
            return True
        else:
            return False

    @staticmethod
    def to_path(path: str | Path) -> Path:
        if isinstance(path, str):
            return Path(path)
        else:
            return path

    @staticmethod
    def to_str(path: str | Path) -> str:
        if isinstance(path, Path):
            return str(path)
        else:
            return path

    @staticmethod
    def get_subdir_names_from(path: str | Path) -> list:
        curr_path = PathHandler.to_path(path)
        subdirs = []
        for child in curr_path.rglob('*'):
            if child.is_dir():
                subdirs.append(child.name)
        return subdirs

    @staticmethod
    def copy_subdirs_from(source: str | Path, other: str | Path) -> None:
        new_path_parent = PathHandler.to_path(other)
        for name in PathHandler.get_subdir_names_from(source):
            new_path = new_path_parent.joinpath(name)
            if not new_path.exists():
                new_path.mkdir()
