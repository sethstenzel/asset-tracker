from classes.file import File


class AssetManager:
    def __init__(self):
        self.files: list[File] = []
        self.asset_includes_file = ".asset_includes"

    def _get_asset_includes(self):
        try:
            with open(self.asset_includes_file) as f:
                return [i.strip() for i in f.readlines()]
        except FileNotFoundError:
            return []

    def add_file(self, file):
        self.files.append(file)

    def get_files(self):
        return self.files

    def drop_file(self, file):
        self.files.remove(file)

    def drop_file_with_hash(self, hash):
        for file in self.files:
            if file.sha256_hash == hash:
                self.files.remove(file)
                break

    def run(self): ...

    def _scan_root(self): ...
