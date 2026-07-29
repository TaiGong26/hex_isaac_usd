"""hex_isaac_usd.configs — Pre-defined ArticulationCfgs for HEX robot assets.

Each config resolves its USD path via ``hex_isaac_usd.HEX_ASSETS_DIR``,
so it works regardless of where the package is installed.

Usage::

    from hex_isaac_usd.configs.manipulator.archer_y6.archer_y6_cfg import HEX_ISAAC_USD_ARCHER_Y6_CFG
"""

# Re-export all configs for convenient access
from hex_isaac_usd.configs.manipulator.archer_y6.archer_y6_cfg import (
    HEX_ISAAC_USD_ARCHER_Y6_CFG,
    HEX_ISAAC_USD_ARCHER_Y6_GR100_CFG,
)
from hex_isaac_usd.configs.manipulator.firefly_y6.firefly_y6_cfg import (
    HEX_ISAAC_USD_FIREFLY_Y6_CFG,
)
from hex_isaac_usd.configs.gripper.gr100.gr100_cfg import (
    HEX_ISAAC_USD_GR100_CFG,
)
from hex_isaac_usd.configs.lift.iotavc1.iotavc1_cfg import (
    HEX_ISAAC_USD_IOTAVC1_CFG,
)
from hex_isaac_usd.configs.lift.lotaP.lotaP_cfg import (
    HEX_ISAAC_USD_LOTAP_CFG,
)
from hex_isaac_usd.configs.lift.zeta_vc2.zeta_vc2_cfg import (
    HEX_ISAAC_USD_ZETA_VC2_CFG,
)
from hex_isaac_usd.configs.chassis.Trigger_A3.trigger_a3_cfg import (
    HEX_ISAAC_USD_TRIGGER_A3_CFG,
)
from hex_isaac_usd.configs.chassis.maver_x4.maver_x4_cfg import (
    HEX_ISAAC_USD_MAVER_X4_CFG,
)

__all__ = [
    "HEX_ISAAC_USD_ARCHER_Y6_CFG",
    "HEX_ISAAC_USD_ARCHER_Y6_GR100_CFG",
    "HEX_ISAAC_USD_FIREFLY_Y6_CFG",
    "HEX_ISAAC_USD_GR100_CFG",
    "HEX_ISAAC_USD_IOTAVC1_CFG",
    "HEX_ISAAC_USD_LOTAP_CFG",
    "HEX_ISAAC_USD_ZETA_VC2_CFG",
    "HEX_ISAAC_USD_TRIGGER_A3_CFG",
    "HEX_ISAAC_USD_MAVER_X4_CFG",
]
