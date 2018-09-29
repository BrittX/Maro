"""
"""
import argparse


__all__ = ("CommandBase",)

class CommandBase(object):
    """The base attributes for any command. This will allow easier plug and play for future commands
    that may be added to Maro.
    """
    usage = None
    name = None
    help_text = None

    def run(self, args):
        """The base run method to call each of the commands.
        """
        pass
