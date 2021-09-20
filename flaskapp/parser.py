import os
from abc import ABC, abstractmethod
from sys import platform
from datetime import datetime

import exiftool


class Parser(ABC):
    """"Abstract class for allowing different parsing implementations
    according to future specific use cases"""

    @abstractmethod
    def get_metadata(self, data):
        """"abstract method to extract the metadata for a file"""


class ExiftoolParser(Parser):
    """"Class to allow media metadata extraction using exiftool"""
    def __init__(self, file_extension, exe_path="./exiftool(-k).exe"):
        """

        :param file_extension: One of the allowed media extensions (mp4, png, etc...)
        :param exe_path: path to exiftool executable (required in windows)
        """
        if platform == "linux" or platform == "linux2":
            exe_path = None
        self.et = exiftool.ExifTool(exe_path)
        self.et.start()
        self.file_extension = file_extension

    def get_metadata(self, data):
        """"extract metadata from a file using exiftool"""
        now = datetime.now()
        filename = f"temp{now.strftime('%m_%d_%Y_%H_%M_%S_%f')}.{self.file_extension}"
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


parser_factory = {"default": ExiftoolParser}
