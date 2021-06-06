from verlat import latest_release

from tgcf import __version__


def test_version():
    assert __version__ == latest_release("tgcf")
