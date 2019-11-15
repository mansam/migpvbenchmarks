#!/bin/bash
set -euo pipefail

usage() {
	echo -e "Usage: $0 storage_class volume_size"
	exit 1
}

[ "$#" -eq 2 ] || usage

STORAGE_CLASS="$1"
VOLUME_CLASS="$2"
PROJECT_NAME=mig-pv-benchmark-big-$STORAGE_CLASS-${VOLUME_SIZE,,}
oc delete project/$PROJECT_NAME

