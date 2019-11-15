# PV Migration Benchmark Scripts

This repo contains all necessary scripts for gathering performance metrics on PV handling.

## Deploying scenario pods

```
./create_small_scenario.sh storage_class volume_capacity
```
Creates a namespace with a name in the form of "mig-pv-benchmark-small-[storage_class]-[volume_capacity]" and deploys the Openshift template in `templates/small_scenario.json` to that namespace.

```
./destroy_small_scenario.sh storage_class volume_capacity
```
Deletes a namespace created by `./create_small_scenario.sh`

```
./create_big_scenario.sh storage_class volume_capacity
```

Creates a namespace with a name in the form of "mig-pv-benchmark-big-[storage_class]-[volume_capacity]" and deploys the Openshift template in `templates/big_scenario.json` to that namespace.

```
./destroy_big_scenario.sh storage_class volume_capacity
```
Deletes a namespace created by `./create_big_scenario.sh`

## Running a migration

`./run_migration` takes the following parameters, and uses them to create a `migplan` and `migmigration` on your logged in cluster:

  ```
  --scenario <scenario>         must be "big" or "small"
  --source <source>             the name of the source cluster (defaults to "benchmark-src")
  --src-sc <src-sc>             the storage class on the source cluster to migrate from
  --dest-sc <dest-sc>           the storage class on the destination cluster to migrate to
  --action <action>             "copy" or "move", defaults to "copy"
  --copy-method <copy_method>   "filesystem" or "snapshot", defaults to "filesystem"
  --size <pvc_size>             the max capacity of the pvc to be moved (see supported sizes below)
  --storage <storage>           the name of the MigStorage repository to use for backups
  --stage                       runs a stage migration if this flag is present

  ```

#### Example

```
  ./run_migration --scenario small --source ocp3 --storage noobaa --src-sc glusterfs-storage --dest-sc csi-rdb --size 60Mi
```

  This runs a glusterfs to ceph migration from a cluster named `ocp3` to `host` using a repository named `noobaa`, with `copy` as its action and `filesystem` as its copy method. This would assume the namespace `mig-pv-benchmark-small-glusterfs-storage-60mi` already exists as a result of running `./create_small_scenario.sh glusterfs-storage 60mi`.

## Parsing benchmark times from logs

`TODO`

## Seed scripts

The following seed scripts are used automatically as part of deploying the scenario pods, and do not need to be run directly.

* `randomdata/bigapp/big_app.py` - script for seeding 10 PVs in 1 namespace with random data

* `randomdata/bigapp/Dockerfile`

* `randomdata/smallapp/small_app.py` - script for seeding 1 PVs in 1 namespace with random data

* `randomdata/smallapp/Dockerfile`

## Templates

* `templates/big_template.json` - openshift template for creating 10 pods, 10 PVC and 1 Job for seeding PVs with data. Requires 2 arguments: VOLUME_CAPACITY, STORAGE_CLASS. Example usage: `oc process -f big_template.json -p VOLUME_CAPACITY=1Gi -p STORAGE_CLASS=nfs1 | oc create -f - `

* `templates/small_template.json` - openshift template for creating 1 pods, 1 PVC and 1 Job for seeding PV with data. Requires 2 arguments: VOLUME_CAPACITY, STORAGE_CLASS. Example usage: `oc process -f small_template.json -p VOLUME_CAPACITY=1Gi -p STORAGE_CLASS=nfs1 | oc create -f - `

* `templates/migration_resources.json` - openshift template for creating a MigPlan and associated MigMigration.

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
