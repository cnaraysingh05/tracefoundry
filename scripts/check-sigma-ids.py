from pathlib import Path
from uuid import UUID

import yaml

root = Path(__file__).resolve().parent.parent
paths = sorted([
    *(root / "examples/sigma-cli").glob("*.yml"),
    *(root / "detections").rglob("sigma.yml"),
])
if not paths:
    raise SystemExit("FAIL: no Sigma rules found")

seen = {}
for path in paths:
    name = path.relative_to(root)
    try:
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(rule, dict):
            raise ValueError("expected a YAML mapping")
        rule_id = UUID(str(rule["id"]))
    except (KeyError, ValueError, yaml.YAMLError) as error:
        raise SystemExit(f"FAIL: {name}: invalid rule or missing UUID: {error}")

    if rule_id in seen:
        raise SystemExit(f"FAIL: duplicate Sigma ID {rule_id}: {seen[rule_id]} and {name}")
    seen[rule_id] = name

print(f"PASS: checked {len(seen)} unique Sigma rule ID(s).")
