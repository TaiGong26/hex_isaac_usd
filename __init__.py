from pathlib import Path

HEX_ASSETS_DIR = Path(__file__).parent.resolve() / "base_model"
"""Path to the root of classified USD asset directories.

Structure: ``base_model/{category}/{model}/{hex_usd_model[_variant]}/``
Categories: manipulator, gripper, lift, chassis
"""
