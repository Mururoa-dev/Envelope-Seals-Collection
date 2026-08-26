import os
import glob

from zipfile import ZipFile

from shutil import make_archive

ROOT=os.path.dirname(__file__)

SEMANTIC = "0.0.1"
VERSION = "1.21.1"

ELEMENTS_TO_WRITE =["assets", "data", "META-INF"]

TO_WRITE = []

for to_write in ELEMENTS_TO_WRITE:

    TO_WRITE.extend(
        glob.glob(pathname=f"{to_write}/**",root_dir=ROOT, recursive=True)
    )

with ZipFile(f"Envelope-seals-collection_{VERSION}_{SEMANTIC}.jar","w") as archive :
    for element in TO_WRITE:
        archive.write(element)
    archive.write("icon.png")
    archive.close()
