"""ArticulationCfg for Trigger_A3 (wheeled chassis).

USD: base_model/chassis/Trigger_A3/hex_usd_Trigger_A3/trigger_a3.usd
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = (
    hex_isaac_usd.HEX_ASSETS_DIR
    / "chassis"
    / "Trigger_A3"
    / "hex_usd_Trigger_A3"
    / "trigger_a3.usd"
)

HEX_ISAAC_USD_TRIGGER_A3_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(_HEX_USD_PATH),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=32,
            solver_velocity_iteration_count=16,
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={"joint_1": 0.0, "joint_2": 0.0, "joint_3": 0.0},
    ),
    actuators={
        "drive_wheels": ImplicitActuatorCfg(
            joint_names_expr=["joint_[1-3]"],
            stiffness=0.0,
            damping=10.0,
            effort_limit_sim=40.0,
            velocity_limit_sim=20.0,
            armature=0.0,
            friction=0.0,
        ),
    },
)
