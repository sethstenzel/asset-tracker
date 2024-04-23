from functions.path_tools import get_launch_directory
from classes.config import Config


def main(launch_directory, configuration):
    pass


if __name__ == "__main__":

    launch_directory = get_launch_directory()
    configuration = Config(f"{launch_directory}/.assets-config")

    main(launch_directory, configuration)
