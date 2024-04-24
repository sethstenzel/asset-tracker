import sys
import os


def get_launch_directory() -> str:
    """Because this utility will be packaged with pyinstaller and
    handling the path can be tricky, this function will get the directory
    containing the script if ran directly or the executable once packaged.

    Returns:
        str: Path to the directory containing the script or executable.
    """

    frozen = getattr(sys, "frozen", False)
    if frozen:
        launch_directory = os.path.dirname(os.path.abspath(sys.executable))
    elif not frozen:
        launch_directory = os.getcwd()
    return launch_directory


def get_all_files_details():
    pass
