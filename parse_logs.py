#!/usr/bin/env python
import argparse
import re
import sys
import json
from collections import defaultdict

ensure_stage_backup = None
ensure_stage_pods_deleted = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('namespace')
    args = parser.parse_args()

    namespace_pattern = re.compile(args.namespace)
    lines = sys.stdin.readlines()
    for line in lines:
        result = re.search(namespace_pattern, line)
        if result != None:
            if (ensure_stage_backup == None) and ("EnsureStageBackup" in line):
                ensure_stage_backup = line
            if (ensure_stage_pods_deleted == None) and ("EnsureStagePodsDeleted" in line):
                ensure_stage_pods_deleted = line
        if ensure_stage_backup and ensure_stage_pods_deleted:
            break

    ensure_stage_backup = json.loads(ensure_stage_backup)
    ensure_stage_pods_deleted = json.loads(ensure_stage_pods_deleted)
    print(ensure_stage_pods_deleted["ts"] - ensure_stage_backup["ts"])
