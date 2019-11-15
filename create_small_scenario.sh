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
oc new-project $PROJECT_NAME || true
oc project $PROJECT_NAME
oc process -f templates/small_template.json -p VOLUME_CAPACITY=$VOLUME_SIZE STORAGE_CLASS=$STORAGE_CLASS | oc create -f - 

