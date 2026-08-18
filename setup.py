"""Installation script for the hex_isaac_usd python package."""

from setuptools import setup

setup(
    name="hex_isaac_usd",
    version="0.1.0",
    description="HEX USD robot assets and ArticulationCfgs for Isaac Lab",
    packages=[
        "hex_isaac_usd",
        "hex_isaac_usd.isaaclab_cfg",
        "hex_isaac_usd.isaaclab_cfg.manipulator",
        "hex_isaac_usd.isaaclab_cfg.manipulator.archer_y6",
        "hex_isaac_usd.isaaclab_cfg.manipulator.firefly_y6",
        "hex_isaac_usd.isaaclab_cfg.gripper",
        "hex_isaac_usd.isaaclab_cfg.gripper.gr100",
        "hex_isaac_usd.isaaclab_cfg.lift",
        "hex_isaac_usd.isaaclab_cfg.lift.iotavc1",
        "hex_isaac_usd.isaaclab_cfg.lift.lotaP",
        "hex_isaac_usd.isaaclab_cfg.lift.zeta_vc2",
        "hex_isaac_usd.isaaclab_cfg.chassis",
        "hex_isaac_usd.isaaclab_cfg.chassis.Trigger_A3",
        "hex_isaac_usd.isaaclab_cfg.chassis.maver_x4",
    ],
    package_dir={"hex_isaac_usd": "."},
    package_data={
        "hex_isaac_usd": [
            "base_model/**/*.usd",
            "base_model/**/*.usda",
            "base_model/**/*.yaml",
            "base_model/**/.asset_hash",
            "base_model/**/configuration/*.usd",
            "base_model/**/.thumbs/**/*.png",
            "*.md",
        ],
    },
    include_package_data=True,
    python_requires=">=3.10",
    license="MIT",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)