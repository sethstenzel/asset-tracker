from classes.suspect_file_instance import SuspectFileInstance
from datetime import datetime


def test_suspect_file_instance_creation():
    last_modified_time = datetime(2023, 4, 24, 12, 30)
    sample_data = b"example data"
    suspect_file = SuspectFileInstance(
        relative_path="path/to/file.txt",
        last_modified=last_modified_time,
        sha256_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        data=sample_data,
    )

    assert suspect_file.relative_path == "path/to/file.txt"
    assert suspect_file.last_modified == last_modified_time
    assert (
        suspect_file.sha256_hash
        == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )
    assert suspect_file.data == sample_data
