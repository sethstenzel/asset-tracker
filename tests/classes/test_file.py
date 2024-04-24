from datetime import datetime
from classes.file import File
from classes.file import FileInstance


def test_file_instance_creation():
    file = FileInstance(
        relative_path="/example.txt",
        last_modified=datetime(2024, 4, 24, 7, 44, 25, 929626),
        sha256_hash="dummyhashvalue123456789",
    )
    assert file.relative_path == "/example.txt"
    assert isinstance(file.last_modified, datetime)
    assert file.sha256_hash == "dummyhashvalue123456789"


def test_file_creation():
    file = File(
        instances=list(),
        sha256_hash="dummyhashvalue123456789",
        data=b"dummydata",
    )
    assert file.sha256_hash == "dummyhashvalue123456789"
    assert file.data == b"dummydata"
    assert len(file.instances) == 0


def test_file_new_file():
    files: list[File] = []
    new_file_hash = "dummyhashvalue123456789"
    new_file_relative_path = "/example.txt"
    new_file_last_modified = datetime(2024, 4, 24, 7, 44, 25, 929626)
    new_file_data = b"dummydata"

    is_new = True
    f: File
    for f in files:
        if new_file_hash == f.sha256_hash:
            is_new = False

    if is_new:
        new_instance = FileInstance(
            relative_path=new_file_relative_path,
            last_modified=new_file_last_modified,
            sha256_hash=new_file_hash,
        )
        new_file = File(
            instances=[new_instance],
            sha256_hash=new_file_hash,
            data=new_file_data,
        )
        files.append(new_file)

    assert files[0].sha256_hash == "dummyhashvalue123456789"
    assert files[0].data == b"dummydata"
    assert len(files[0].instances) == 1
    assert files[0].instances[0].relative_path == "/example.txt"
    assert isinstance(files[0].instances[0].last_modified, datetime)
    assert files[0].instances[0].sha256_hash == "dummyhashvalue123456789"
