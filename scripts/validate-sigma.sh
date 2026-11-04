#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")/.."
python3 scripts/check-sigma-ids.py
example="examples/sigma-cli/powershell-version"
actual="$(mktemp)"
trap 'rm -f "$actual"' EXIT

sigma convert -t splunk -p splunk_windows "$example.yml" > "$actual"
test -s "$actual" || { echo "FAIL: conversion produced empty SPL" >&2; exit 1; }
diff -u "$example.spl" "$actual"
echo "PASS: generated SPL matches the reviewed example."
