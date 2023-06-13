#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:55:24 2023

@author: temuuleu
"""

import pkg_resources
import sys


def main():
    requirements_file = sys.argv[1]
    with open(requirements_file, "r") as f:
        required_packages = [
            line.strip().split("#")[0].strip() for line in f.readlines()
        ]

    installed_packages = [package.key for package in pkg_resources.working_set]

    missing_packages = []
    for package in required_packages:
        if not package:  # Skip empty lines
            continue
        package_name = package.strip().split("==")[0]
        if package_name.lower() not in installed_packages:
            missing_packages.append(package_name)

    if missing_packages:
        print("Missing packages:")
        print(", ".join(missing_packages))
        sys.exit(1)
    else:
        print("All packages are installed.")


if __name__ == "__main__":
    main()
