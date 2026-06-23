# hex_isaac_usd

USD asset package for hexfellow robots under Isaac Lab, providing USD models
for each robot variant and pre-defined `ArticulationCfg`.

---

## Repository Structure

```
hex_isaac_usd/
├── base_model/    # USD models for each robot variant
├── configs/       # Pre-defined ArticulationCfgs, importable via hex_isaac_usd.configs
└── setup.py       # pip editable install entry
```

> ⚠️ **About `ImplicitActuatorCfg` parameters**:
> - The `stiffness`, `damping`, `effort_limit`, etc. parameters in each CFG
> under `configs/` **are NOT the actual robot's torque or PD values**.
> - They are chosen to keep the visual appearance and basic motion reachability
> in simulation, and must not be used for parameter selection on the real robot.
