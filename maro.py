#!/usr/bin/env python3
import argparse
import sys
import os
import subprocess

try:
    from haikunator import Haikunator
except ImportError:
    print("Cannot download 'haikunator', is it installed?")
    sys.exit(1)

# class Maro(object):
#     """
#     Example usage:
#             ./maro.py build {project type} repo --name MyNewProject1 --path
#             ./maro.py build --type containers --type python3, rabbitmq, etc --location
#             ./maro.py --help
#     """

def build(args):
    """
    Args:
        args (list): The command line arguments called with the build command.
    """
    if args.project == "repository":
        # Building a git repo
        if os.path.isdir(args.path):
            # Create new path with directory to create
            # Will want to move path related stuff outside of if statements for each option to use
            path = os.path.join(args.path, args.name)
            os.mkdir(path)
            os.chdir(path)
            # Initialize new folder as a git repo
            subprocess.run(["git", "init"], stdout=subprocess.PIPE)
            # Generate a python3.6 venv
            subprocess.run(["virtualenv", "-p" "python3.6", "venv"])
        else:
            # Path isn't a directory
            print(f"The selected path is not a directory: {args.path}")
    else:
        # Haven't implemented other project types yet
        print(f"you {args.name} rang?")

        print(f"My location is: {args.path}")


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

build_parser = subparsers.add_parser("build")
build_parser.add_argument(
    "project",
    help="The type of project to build",
    choices=["repository", "containers", "images"],
) # add type argument
# Add option for name w/default randomly generated name
build_parser.add_argument(
    "--name",
    default=Haikunator().haikunate(),
    help="The name of the project to create.",
)
# Add option for location w/default
build_parser.add_argument(
    "--path",
    default=os.getcwd(),
    help="The path where the project should be built.",
)
build_parser.set_defaults(func=build) # Set default function to hello

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args) # call the default function
