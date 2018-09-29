"""Info related to the build command.
"""
import os
import subprocess
import sys

from . import base


__all__ = ("Build",)

class Build(base.CommandBase):
    """
    """
    name = "build"
    help_text = "The project to create."
    def __init__(self, args):
        """
        """
        # Create new path with directory to create
        self.path = os.path.join(args.path, args.name)
        self.name = args.name
        self.project = args.project

        self.verbose = args.verbose

        try:
            os.mkdir(self.path)
        except FileExistsError:
            print(f"The directory already exists: {self.path}")
            sys.exit(1)

        self.run()

    def run(self):
        """Default run method for each command.
        """
        if self.project == "repository":
            # building a git repo
            self.build_repository()
        elif self.project == "containers":
            # generating some containers
            print("Not implemented yet G")
        else:
            # generating some docker images
            print("Not implemented either my guy")

    def build_repository(self):
        """Method to generate a git repository for a new project.
        """
        # Change directory to the new git repo location
        os.chdir(self.path)

        # Initialize new folder as a git repo
        git_out = subprocess.run(
            ["git", "init"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Generate a python3.6 venv
        venv_out = subprocess.run(
            ["virtualenv", "-p", "python3.6", "--no-download", "venv"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if self.verbose:
            # TODO: If verbosity is set, then print out the output
            print(git_out.stdout.decode("utf-8"))

            print(venv_out.stdout.decode("utf-8"))
