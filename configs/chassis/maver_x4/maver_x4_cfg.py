"""ArticulationCfg for maver_x4 (wheeled chassis).

USD: base_model/chassis/maver_x4/hex_usd_maver_x4/maver_x4.usd
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = (
    hex_isaac_usd.HEX_ASSETS_DIR
    / "chassis"
    / "maver_x4"
    / "hex_usd_maver_x4"
    / "maver_x4.usd"
)

HEX_ISAAC_USD_MAVER_X4_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(_HEX_USD_PATH),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=1.0,
            angular_damping=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=32,
            solver_velocity_iteration_count=16,
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "joint_yaw1": 0.0,
            "joint_yaw2": 0.0,
            "joint_yaw3": 0.0,
            "joint_yaw4": 0.0,
            "joint_wheel1": 0.0,
            "joint_wheel2": 0.0,
            "joint_wheel3": 0.0,
            "joint_wheel4": 0.0,
        },
    ),
    actuators={
        "maver_x4_steering": ImplicitActuatorCfg(
            joint_names_expr=["joint_yaw.*"],
            stiffness=400.0,
            damping=20.0,
            effort_limit_sim=50.0,
            velocity_limit_sim=20.0,
        ),
        "maver_x4_driver": ImplicitActuatorCfg(
            joint_names_expr=["joint_wheel.*"],
            stiffness=0.0,
            damping=200.0,
            effort_limit_sim=40.0,
            velocity_limit_sim=20.0,
        ),
    },
)


