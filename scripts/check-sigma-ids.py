import re
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

technique_pattern = re.compile(r"attack\.t[0-9]{4}(?:\.[0-9]{3})?")
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

    if name.parts[0] == "detections":
        author = rule.get("author")
        if not isinstance(author, str) or not author.strip():
            raise SystemExit(f"FAIL: {name}: author must be a nonempty string")

        tags = rule.get("tags")
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            raise SystemExit(f"FAIL: {name}: tags must be a list of strings")
        techniques = [tag for tag in tags if tag.lower().startswith("attack.t") and tag[8:9].isdigit()]
        if not techniques or any(not technique_pattern.fullmatch(tag) for tag in techniques):
            raise SystemExit(f"FAIL: {name}: tags must include a valid ATT&CK technique ID in attack.tNNNN or attack.tNNNN.NNN format")

    if rule_id in seen:
        raise SystemExit(f"FAIL: duplicate Sigma ID {rule_id}: {seen[rule_id]} and {name}")
    seen[rule_id] = name

print(f"PASS: checked {len(seen)} unique Sigma rule ID(s).")
