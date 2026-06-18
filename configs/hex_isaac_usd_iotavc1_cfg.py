"""ArticulationCfg for iotavc1 (1-DOF lift).

USD: base_model/hex_usd_iotavc1/iotavc1.usd

Note: base_link mesh Z range [-0.900, 0.153]; origin at model top.
Config sets init_state.pos Z=1.0 to avoid floor collision.
"""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg

import hex_isaac_usd

_HEX_USD_PATH = hex_isaac_usd.HEX_ASSETS_DIR / "hex_usd_iotavc1" / "iotavc1.usd"

HEX_ISAAC_USD_IOTAVC1_CFG = ArticulationCfg(
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
    init_state=ArticulationCfg.InitialStateCfg(pos=(0.0, 0.0, 1.0), joint_pos={"joint_1": 0.0}),
    actuators={
        "lift": ImplicitActuatorCfg(
            joint_names_expr=["joint_1"],
            effort_limit_sim=50.0,
            stiffness=100.0,
            damping=10.0,
        ),
    },
)
