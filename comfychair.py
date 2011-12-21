#! /usr/bin/python2

import argparse

from comfychair import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sit In The Comfy Chair")
    parser.add_argument("app", help="directory where the Comfy Chair app is located")
    args = parser.parse_args()
    main.main(args.app)