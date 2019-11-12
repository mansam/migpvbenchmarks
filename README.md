# Performance metrics on PV handling

This repo contains all necessary scripts for gathering performance metrics on PV handling.

## Usage
  1. TODO

## Content description

* `randomdata/bigapp/big_app.py` - script for seeding 10 PVs in 1 namespace with random data

* `randomdata/bigapp/Dockerfile`

* `randomdata/smallapp/small_app.py` - script for seeding 1 PVs in 1 namespace with random data

* `randomdata/smallapp/Dockerfile`

* `templates/big_template.json` - openshift template for creating 10 pods, 10 PVC and 1 Job for seeding PVs with data. Requires 2 arguments: VOLUME_CAPACITY, STORAGE_CLASS. Example usage: `oc process -f big_template.json -p VOLUME_CAPACITY=1Gi -p STORAGE_CLASS=nfs1 | oc create -f - `

* `templates/small_template.json` - openshift template for creating 1 pods, 1 PVC and 1 Job for seeding PV with data. Requires 2 arguments: VOLUME_CAPACITY, STORAGE_CLASS. Example usage: `oc process -f small_template.json -p VOLUME_CAPACITY=1Gi -p STORAGE_CLASS=nfs1 | oc create -f - `

## Supported PVC sizes

  * small_template
    * 60Mi - 5OMi of actual data on PV
    * 2Gi - 1Gi of actual data on PV
    * 12Gi - 10Gi of actual data on PV
    * 115Gi - 100Gi of actual data on PV
    * 1120Gi - 1024Gi of actual data on PV

  * big_template
    * 2Gi - 1Gi of actual data on PV
    * 11Gi - 10Gi of actual data on PV
