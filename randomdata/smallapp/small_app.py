import os
import sys

print("Attempting to fill volume with data")

# fail if volume not empty
files_in_volume = os.listdir('/hellovolume')
if len(files_in_volume) > 0:
    print("Volume directory is not empty, exiting")
    sys.exit(2)

volume_size = os.getenv("VOLUME_CAPACITY")
sizes = {
    "50Mi": None,
    "1Gi": 1073741824,
    "10Gi": 10737418240,
    "100Gi": 107374182400,
    "1Ti": 1099511627776
}

# filter invalid volume sizes
if volume_size not in sizes.keys():
    print("Invalid volume size, exiting")
    sys.exit(2)

# Create files with random data
# Since urandom has a buffer, we should a pass a safe value to it, code below creates
# either 50Mb file or some amount of 1GB files
if volume_size == "50Mi":
    files_count = 1
    file_size = 52428800
else:
    files_count = sizes[volume_size] / 1073741824
    file_size = 1073741824

for i in range(1, int(files_count) + 1):
    with open("/hellovolume/large_file" + str(i), "wb") as fout:
        fout.write(os.urandom(file_size))

print("Done")
