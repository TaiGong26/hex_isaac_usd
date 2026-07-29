"""ArticulationCfg for Firefly_Y6 (hexacopter).

USD: base_model/manipulator/firefly_y6/hex_usd_firefly_y6/firefly_y6.usd

TODO: Fill in joint layout and actuator config once known.
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = (
    hex_isaac_usd.HEX_ASSETS_DIR
    / "manipulator"
    / "firefly_y6"
    / "hex_usd_firefly_y6"
    / "firefly_y6.usd"
)

HEX_ISAAC_USD_FIREFLY_Y6_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(_HEX_USD_PATH),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(),
    actuators={},
)
