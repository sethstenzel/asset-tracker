from dataclasses import dataclass, field
from classes.file_instance import FileInstance


@dataclass
class File:
    sha256_hash: str
    data: bytes
    instances: list[FileInstance] = field(default_factory=list)
