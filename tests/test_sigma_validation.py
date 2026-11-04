import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULE = Path("detections/tag-test/sigma.yml")


class SigmaTagTests(unittest.TestCase):
    def validate(self, tag=None):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            script = root / "scripts/check-sigma-ids.py"
            script.parent.mkdir()
            shutil.copyfile(ROOT / "scripts/check-sigma-ids.py", script)
            rule = root / RULE
            rule.parent.mkdir(parents=True)
            fixture = "id: 91f619f6-0bcf-49b0-b173-29a7143ed674\nauthor: TraceFoundry\n"
            if tag is not None:
                fixture += f"tags: [{tag}]\n"
            rule.write_text(fixture, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(script)], cwd=root, capture_output=True, text=True
            )

    def test_parent_technique(self):
        result = self.validate("attack.t1059")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_subtechnique(self):
        result = self.validate("attack.t1059.001")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_tags(self):
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"{RULE}: tags must be a list", result.stderr)

    def test_short_subtechnique_suffix(self):
        result = self.validate("attack.t1059.01")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(f"{RULE}: tags must include a valid ATT&CK technique ID", result.stderr)
