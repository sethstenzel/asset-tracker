import pytest
from unittest.mock import patch
from classes.config import Config
import tomllib
import io


@pytest.fixture
def mock_toml_file():
    """Fixture to simulate TOML content."""
    toml_content = """
    [paths]
    root = "/"

    [track_on]
    size = true
    last_modified = true
    md5 = true

    [versioning]
    version_prefix = "test_"
    version_suffix = "_test"
    versioning_mode = ["last-modified", "version-number", "md5"]

    [options]
    remove_duplicates = false
    warn_duplicates = true
    sumamry = "detailed"
    """
    toml_content_bytes = toml_content.encode("utf-8")
    toml_content_bytes = io.BytesIO(toml_content_bytes)
    return tomllib.load(toml_content_bytes)


def test_config_load_success(mock_toml_file):
    """Test successful loading of config from a TOML file."""
    with patch("tomllib.load", return_value=mock_toml_file) as mock_load:

        config = Config("mock_config.toml")
        mock_load.assert_called_once_with("mock_config.toml")
        assert config.get("paths")["root"] == "/"
        assert config.get("track_on")["size"] is True
        assert config.get("versioning")["version_suffix"] == "_test"
        assert config.get("options")["warn_duplicates"] is True


def test_config_key_error(mock_toml_file):
    """Test accessing a non-existent key in config raises KeyError."""
    with patch("tomllib.load", return_value=mock_toml_file) as mock_load:
        config = Config("mock_config.toml")
        mock_load.assert_called_once_with("mock_config.toml")
        # Check for KeyError on accessing non-existent key
        with pytest.raises(KeyError):
            config.get("non_existent_key")
