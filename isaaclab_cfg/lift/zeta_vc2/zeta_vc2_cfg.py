"""ArticulationCfg for zeta_vc2 (3-DOF lift).

USD: base_model/lift/zeta_vc2/hex_usd_zeta_vc2/zeta_vc2.usd
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = (
    hex_isaac_usd.HEX_ASSETS_DIR
    / "lift"
    / "zeta_vc2"
    / "hex_usd_zeta_vc2"
    / "zeta_vc2.usd"
)

HEX_ISAAC_USD_ZETA_VC2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(_HEX_USD_PATH),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=32,
            solver_velocity_iteration_count=4,
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={"joint_1": 0.0, "joint_2": 0.0, "joint_3": 0.0},
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=["joint_[1-3]"],
            effort_limit_sim=80.0,
            stiffness=100.0,
            damping=10.0,
        ),
    },
)
