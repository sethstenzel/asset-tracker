from dataclasses import dataclass
from datetime import datetime


@dataclass
class FileInstance:
    relative_path: str
    last_modified: datetime
    sha256_hash: str
