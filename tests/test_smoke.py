"""
Smoke tests for MudraForge repository initialization.
Checks package imports, configuration structure, and feature constants.
"""
import importlib
import json
import sys
from pathlib import Path

# Ensure project root is in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


def test_src_imports():
    """Verify that every module under src/ imports without requiring external hardware."""
    modules = [
        "src.hand_tracker",
        "src.features",
        "src.recorder",
        "src.trainer",
        "src.recognizer",
        "src.actions",
    ]
    for module_name in modules:
        mod = importlib.import_module(module_name)
        assert mod is not None


def test_mapping_config():
    """Verify config/mapping.json is valid and includes all required keys."""
    config_file = ROOT_DIR / "config" / "mapping.json"
    assert config_file.is_file(), "config/mapping.json not found."

    with open(config_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert "arm_gesture" in data
    assert "arm_hold_seconds" in data
    assert "mapping" in data
    assert isinstance(data["mapping"], dict)


def test_feature_dimensions():
    """Verify FEATURE_DIM is set to 63."""
    from src.features import FEATURE_DIM

    assert FEATURE_DIM == 63
