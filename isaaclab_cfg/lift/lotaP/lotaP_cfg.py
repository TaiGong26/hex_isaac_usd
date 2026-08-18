"""ArticulationCfg for lotaP (1-DOF lift).

USD: base_model/lift/lotaP/hex_usd_lotaP/lotaP.usd

Note: base_link mesh Z range [-0.857, 0.156]; origin at model top.
Config sets init_state.pos Z=0.9 to avoid floor collision.
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = (
    hex_isaac_usd.HEX_ASSETS_DIR
    / "lift"
    / "lotaP"
    / "hex_usd_lotaP"
    / "lotaP.usd"
)

HEX_ISAAC_USD_LOTAP_CFG = ArticulationCfg(
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
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.9), joint_pos={"joint_1": 0.0}
    ),
    actuators={
        "lift": ImplicitActuatorCfg(
            joint_names_expr=["joint_1"],
            effort_limit_sim=100.0,
            stiffness=5000.0,
            damping=500.0,
        ),
    },
)
