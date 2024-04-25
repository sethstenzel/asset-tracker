from unittest import mock
from classes.asset_manager import AssetManager
from classes.file import File
import os
import pytest

MOCK_ASSET_INCLUDES = """
test_dir
test_file.dat
*.test
test*wildcard.txt
testwildcardpost*
!testfile.skip
!excluded_subdir_parent/excluded_subdir
excluded_subdir_parent
"""


@pytest.fixture(scope="session", autouse=True)
def set_src_directory():
    os.chdir("src")
    yield
    os.chdir("..")


def test_asset_manager_get_files():
    file1 = File(sha256_hash="ab12", data=b"1234")
    asset_manager = AssetManager()
    asset_manager.add_file(file1)
    files = asset_manager.get_files()
    assert len(files) == 1


def test_asset_manager_add_file():
    file1 = File(sha256_hash="ab12", data=b"1234")
    asset_manager = AssetManager()
    asset_manager.add_file(file1)
    files: list[File] = asset_manager.get_files()
    assert len(files) == 1
    assert files[0] == file1
    assert files[0].sha256_hash == "ab12"
    assert files[0].data == b"1234"


def test_asset_manager_drop_file():
    file1 = File(sha256_hash="ab12", data=b"1234")
    asset_manager = AssetManager()
    asset_manager.add_file(file1)
    files: list[File] = asset_manager.get_files()
    assert len(files) == 1
    asset_manager.drop_file(file1)
    files = asset_manager.get_files()
    assert len(files) == 0
    assert files == []


def test_asset_manager_drop_file_with_hash():
    file1 = File(sha256_hash="ab12", data=b"1234")
    asset_manager = AssetManager()
    asset_manager.add_file(file1)
    files: list[File] = asset_manager.get_files()
    assert len(files) == 1
    asset_manager.drop_file_with_hash("ab12")
    files = asset_manager.get_files()
    assert len(files) == 0
    assert files == []


def test_asset_manager_get_asset_includes_not_found():
    asset_manager = AssetManager()
    with mock.patch.object(
        asset_manager, "asset_includes_file", new="non_existent_file"
    ):
        actual_includes = len(asset_manager._get_asset_includes())
        expected_includes = 0
        assert actual_includes == expected_includes


def test_asset_manager_get_asset_includes():
    # Setup the mock to mimic file read with multiple lines
    with mock.patch(
        "builtins.open",
        mock.mock_open(read_data=MOCK_ASSET_INCLUDES),
    ):
        asset_manager = AssetManager()
        includes = asset_manager._get_asset_includes()
        actual_value = len(includes)
        expected_value = 9
        assert actual_value == expected_value
