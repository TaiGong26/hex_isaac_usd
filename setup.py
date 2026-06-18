"""Installation script for the hex_isaac_usd python package."""

from setuptools import setup

setup(
    name="hex_isaac_usd",
    version="0.1.0",
    description="HEX USD robot assets and ArticulationCfgs for Isaac Lab",
    packages=["hex_isaac_usd", "hex_isaac_usd.configs"],
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