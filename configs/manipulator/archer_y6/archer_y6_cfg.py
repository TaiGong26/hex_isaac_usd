"""ArticulationCfgs for Archer_Y6.

Contains configs for all Archer_Y6 variants:

- ``HEX_ISAAC_USD_ARCHER_Y6_CFG``: 6-DOF arm only
  (USD: hex_usd_archer_y6/archer_y6.usd)

- ``HEX_ISAAC_USD_ARCHER_Y6_GR100_CFG``: 8-DOF fused arm + GP100 gripper
  (USD: hex_usd_archer_y6_gr100/archer_gripper.usd)

``HEX_ISAAC_USD_ARCHER_Y6_GP100_CFG`` is kept as an alias of ``GR100_CFG``
for backward compatibility with existing demo scripts.
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd


# ---------------------------------------------------------------------------
# Arm-only variant  (6-DOF)
# ---------------------------------------------------------------------------

_HEX_ARM_PATH = (
    hex_isaac_usd.HEX_ASSETS_DIR
    / "manipulator"
    / "archer_y6"
    / "hex_usd_archer_y6"
    / "archer_y6.usd"
)

HEX_ISAAC_USD_ARCHER_Y6_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(_HEX_ARM_PATH),
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


# ---------------------------------------------------------------------------
# Arm + GP100 gripper variant  (8-DOF)
# ---------------------------------------------------------------------------

_HEX_ARM_GRIPPER_PATH = (
    hex_isaac_usd.HEX_ASSETS_DIR
    / "manipulator"
    / "archer_y6"
    / "hex_usd_archer_y6_gr100"
    / "archer_gripper.usd"
)

HEX_ISAAC_USD_ARCHER_Y6_GR100_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=str(_HEX_ARM_GRIPPER_PATH),
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
        joint_pos={
            "joint_1": 0.0,
            "joint_2": -1.5,
            "joint_3": 3.0,
            "joint_4": 0.0,
            "joint_5": 0.0,
            "joint_6": 0.0,
            "J1": 0.0,
            "J2": 0.0,
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
        "gp100": ImplicitActuatorCfg(
            joint_names_expr=["J[12]"],
            effort_limit_sim=10.0,
            stiffness=100.0,
            damping=10.0,
        ),
    },
)

# Backward-compatible alias (was renamed from GP100 to GR100)
HEX_ISAAC_USD_ARCHER_Y6_GP100_CFG = HEX_ISAAC_USD_ARCHER_Y6_GR100_CFG
