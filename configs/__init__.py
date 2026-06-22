"""Pre-defined ArticulationCfgs for HEX USD robot assets.

Each config resolves its USD path via ``hex_isaac_usd.HEX_ASSETS_DIR``,
so it works regardless of where the package is installed.

Usage::

    from hex_isaac_usd.configs import HEX_ISAAC_USD_ARCHER_Y6_CFG
    # use in InteractiveSceneCfg:
    #   my_robot: ArticulationCfg = HEX_ISAAC_USD_ARCHER_Y6_CFG.replace(
    #       prim_path="{ENV_REGEX_NS}/MyRobot"
    #   )
"""

from .hex_isaac_usd_archer_y6_cfg import HEX_ISAAC_USD_ARCHER_Y6_CFG
from .hex_isaac_usd_archer_y6_gp100_cfg import HEX_ISAAC_USD_ARCHER_Y6_GP100_CFG
from .hex_isaac_usd_trigger_a3_cfg import HEX_ISAAC_USD_TRIGGER_A3_CFG
from .hex_isaac_usd_maver_x4_cfg import HEX_ISAAC_USD_MAVER_X4_CFG
from .hex_isaac_usd_iotavc1_cfg import HEX_ISAAC_USD_IOTAVC1_CFG
from .hex_isaac_usd_lotap_cfg import HEX_ISAAC_USD_LOTAP_CFG
from .hex_isaac_usd_zeta_vc2_cfg import HEX_ISAAC_USD_ZETA_VC2_CFG
from .hex_isaac_usd_gr100_cfg import HEX_ISAAC_USD_GR100_CFG

__all__ = [
    "HEX_ISAAC_USD_ARCHER_Y6_CFG",
    "HEX_ISAAC_USD_ARCHER_Y6_GP100_CFG",
    "HEX_ISAAC_USD_TRIGGER_A3_CFG",
    "HEX_ISAAC_USD_MAVER_X4_CFG",
    "HEX_ISAAC_USD_X4_RIGID_CFG",
    "HEX_ISAAC_USD_IOTAVC1_CFG",
    "HEX_ISAAC_USD_LOTAP_CFG",
    "HEX_ISAAC_USD_ZETA_VC2_CFG",
    "HEX_ISAAC_USD_GR100_CFG",
]
