#!/bin/bash
set -euo pipefail

# defaults
STAGE="false"
SRC_MIGCLUSTER_REF="benchmark-src"
MIGSTORAGE_REF="benchmark-storage"
ACTION="copy"
COPY_METHOD="filesystem"

while [ -n "${1-}" ]
do
	case "$1" in
		--scenario)
			SCENARIO="$2"
			shift
			;;
                --source)
			SRC_MIGCLUSTER_REF="$2"
			shift
			;;
		--src-sc) 
			SRC_STORAGE_CLASS="$2"
			shift
			;;
		--dest-sc)
			DEST_STORAGE_CLASS="$2"
			shift
			;;
		--storage)
			MIGSTORAGE_REF="$2"
			shift
			;;
		--copy-method)
			COPY_METHOD="$2"
			shift
			;;
		--action)
			ACTION="$2"
			shift
			;;
		--size)
			SIZE="$2"
			shift
			;;
		--stage)
			STAGE="true"
			;;
		*) break;;
	esac
	shift
done

oc project openshift-migration
oc process -f templates/migration_resources.json -p BENCHMARK_NAME=mig-pv-benchmark-$SCENARIO-$SRC_STORAGE_CLASS-${SIZE,,} \
       					            SRC_MIGCLUSTER_REF=$SRC_MIGCLUSTER_REF DEST_MIGCLUSTER_REF=host \
						    MIGSTORAGE_REF=$MIGSTORAGE_REF VOLUME_CAPACITY=$SIZE \
						    SRC_STORAGE_CLASS=$SRC_STORAGE_CLASS DEST_STORAGE_CLASS=$DEST_STORAGE_CLASS \
						    VOLUME_ACTION=$ACTION COPY_METHOD=$COPY_METHOD STAGE=$STAGE \
						    | oc create -f -
