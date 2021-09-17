import os
from datetime import datetime

import exiftool


class Parser:
    def __init__(self, exe_path="./exiftool(-k).exe"):
        self.et = exiftool.ExifTool(exe_path)
        self.et.start()

    def get_metadata(self, ext, data):
        now = datetime.now()
        filename = f"temp{now.strftime('%m_%d_%Y_%H_%M_%S_%f')}.{ext}"
        with open(filename, "w+b") as file:
            file.write(data)
            raw_meta = self.et.get_metadata(filename)
        os.remove(filename)

        meta = {}
        for k, v in raw_meta.items():
            names = k.split(":")
            if len(names) > 1:
                meta[names[1]] = v
            else:
                meta[names[0]] = v

        return meta
