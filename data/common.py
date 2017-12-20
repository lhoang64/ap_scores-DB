#!/usr/bin/env python3

import os


def create_output_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)