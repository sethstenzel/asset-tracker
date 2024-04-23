import tomllib


class Config:
    def __init__(self, path):
        self.path = path
        self.config = tomllib.load(path)

    def get(self, key):
        return self.config[key]
