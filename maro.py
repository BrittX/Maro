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

import commands

# Functions
available_commands = [
    commands.Build,
]


def main():
    """
    Example usage:
            ./maro.py build {project type} repo --name MyNewProject1 --path
            ./maro.py build --type containers --type python3, rabbitmq, etc --path
            ./maro.py --help
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # basic parser options for all commands
    parser.add_argument(
        "--verbose",
        help="Display output of each command",
        action="store_true",
    )

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
    build_parser.set_defaults(func=commands.Build) # Set default function to hello
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    sys.exit(main())
