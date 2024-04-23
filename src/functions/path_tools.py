import sys
import os


def get_launch_directory():
    # This will be packaged with pyinstaller and handling the path can be tricky.
    # Get the directory containing the executable once packaged.
    if getattr(sys, "frozen", False):
        # The application is frozen with PyInstaller
        launch_directory = os.path.dirname(os.path.abspath(sys.executable))
    else:
        # The application is not frozen
        # Get the directory from where the script was launched
        launch_directory = os.getcwd()
    return launch_directory
