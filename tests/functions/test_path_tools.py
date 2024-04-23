from unittest.mock import patch
from functions.path_tools import get_launch_directory


def test_get_launch_directory_frozen():
    # Test when the application is packaged with PyInstaller
    with patch("sys.frozen", True, create=True), patch(
        "sys.executable", "/path/to/frozen/executable"
    ), patch("os.path.abspath") as mock_abspath, patch(
        "os.path.dirname"
    ) as mock_dirname:

        mock_abspath.return_value = "/path/to/frozen/executable"
        mock_dirname.return_value = "/path/to/frozen"

        launch_directory = get_launch_directory()

        mock_abspath.assert_called_once_with("/path/to/frozen/executable")
        mock_dirname.assert_called_once_with("/path/to/frozen/executable")
        assert launch_directory == "/path/to/frozen"


def test_get_launch_directory_not_frozen():
    # Test when the application is not packaged with PyInstaller
    with patch("sys.frozen", False, create=True), patch("os.getcwd") as mock_getcwd:

        mock_getcwd.return_value = "/current/working/directory"

        launch_directory = get_launch_directory()

        mock_getcwd.assert_called_once()
        assert launch_directory == "/current/working/directory"
