# hex_isaac_usd

hexfellow 机器人在 Isaac Lab 下的 USD Assets包,提供各机型的 USD 模型与
预定义的 `ArticulationCfg`。

---

## 仓库结构

```
hex_isaac_usd/
├── base_model/    # 各机型 USD 模型
├── isaaclab_cfg/  # 预定义 ArticulationCfg,通过 hex_isaac_usd.isaaclab_cfg 导入
└── setup.py       # pip 可编辑安装入口
```

> ⚠️ **关于 `ImplicitActuatorCfg` 参数**:
> - `isaaclab_cfg/` 中各 CFG 的 `stiffness`、`damping`、`effort_limit` 等参数
> **并非真实机器人的力矩或 PD 值**。
> - 它们用于保证仿真中的视觉表现与基本运动可达性,不应用于真机控制参数选型。
