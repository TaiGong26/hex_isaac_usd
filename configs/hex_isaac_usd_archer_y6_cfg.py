"""ArticulationCfg for Archer_Y6 (6-DOF arm).

USD: base_model/hex_usd_archer_y6/archer_y6.usd
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = hex_isaac_usd.HEX_ASSETS_DIR / "hex_usd_archer_y6" / "archer_y6.usd"

HEX_ISAAC_USD_ARCHER_Y6_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(_HEX_USD_PATH),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "joint_1": 0.0,
            "joint_2": -1.5,
            "joint_3": 3.0,
            "joint_4": 0.0,
            "joint_5": 0.0,
            "joint_6": 0.0,
        },
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=["joint_[1-6]"],
            effort_limit_sim={
                "joint_[1-3]": 25.0,
                "joint_[4-6]": 6.0,
            },
            stiffness={
                "joint_[1-2]": 400.0,
                "joint_3": 500.0,
                "joint_4": 200.0,
                "joint_[5-6]": 100.0,
            },
            damping={
                "joint_[1-4]": 20.0,
                "joint_[5-6]": 2.0,
            },
        ),
    },
)
