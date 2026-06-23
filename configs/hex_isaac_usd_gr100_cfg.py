"""ArticulationCfg for GR100 (2-DOF gripper).

USD: base_model/hex_usd_gr100/gr100.usd
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = hex_isaac_usd.HEX_ASSETS_DIR / "hex_usd_gr100" / "gr100.usd"

HEX_ISAAC_USD_GR100_CFG = ArticulationCfg(
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
    init_state=ArticulationCfg.InitialStateCfg(joint_pos={"J1": 0.5, "J2": 0.5}),
    actuators={
        "gp100": ImplicitActuatorCfg(
            joint_names_expr=["J[12]"],
            effort_limit_sim=10.0,
            stiffness=100.0,
            damping=10.0,
        ),
    },
)
