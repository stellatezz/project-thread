#!/usr/bin/env python3
"""Compile and run the deterministic Swift 6 fixture harness; no dependencies."""
import argparse
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--baseline", action="store_true")
args = parser.parse_args()
label = "baseline" if args.baseline else "fixed"
source = root / ("artifacts/baseline/FeedStore.swift" if args.baseline else "FeedStore.swift")
destination = root / "artifacts" / label
destination.mkdir(exist_ok=True)
binary = destination / "feed-regression"
command = ["swiftc", "-swift-version", "6", "-strict-concurrency=complete", "-warnings-as-errors",
           "-module-cache-path", str(root / "artifacts/module-cache"), "-parse-as-library",
           str(source), str(root / "Tests/FeedStoreRegression.swift"), "-o", str(binary)]
with (destination / "check.log").open("w") as log:
    for action in [command, [str(binary)]]:
        log.write("COMMAND: " + " ".join(action) + "\n")
        log.flush()
        try:
            result = subprocess.run(action, cwd=root, capture_output=True, text=True, timeout=60)
        except subprocess.TimeoutExpired:
            log.write("TIMEOUT after 60 seconds\n")
            print("TIMEOUT; see", log.name)
            sys.exit(124)
        log.write(result.stdout + result.stderr)
        log.write(f"EXIT: {result.returncode}\n")
        log.flush()
        print(result.stdout + result.stderr, end="")
        if result.returncode:
            sys.exit(result.returncode)
