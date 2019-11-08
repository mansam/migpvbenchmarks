import os
import sys

print("Attempting to fill volumes with data")
for i in range(1, 11):
    volume_dir = "/hellovolume" + str(i)

    files_in_volume = os.listdir(volume_dir)
    if len(files_in_volume) > 0:
        print("Volume directory" + volume_dir + " is not empty, exiting")
        sys.exit()

    volume_size = os.getenv("VOLUME_CAPACITY")
    sizes = {
        "1Gi": 1073741824,
        "10Gi": 10737418240,
    }

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

    print("Writing random data to volume " + volume_dir)
    for j in range(1, int(files_count) + 1):
        with open(volume_dir + "/large_file" + str(j), "wb") as fout:
            fout.write(os.urandom(file_size))

print("Done")
