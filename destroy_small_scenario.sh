#!/bin/bash
set -euo pipefail


usage() {
	echo -e "Usage: $0 storage_class volume_size"
	exit 1
}

[ "$#" -eq 2 ] || usage

STORAGE_CLASS="$1"
VOLUME_SIZE="$2"
PROJECT_NAME=mig-pv-benchmark-small-$STORAGE_CLASS-${VOLUME_SIZE,,}
oc delete project/$PROJECT_NAME

