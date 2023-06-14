import pytest

from network import Network
# Don't forget pip install pytest


@pytest.fixture
def create_network():
    #return Network("1.2.3.0",24)
    yield Network("1.2.3.0",24)
    print("Network Deleted")

def test_subnet(create_network):
    assert create_network.get_host_count() == 253

def test_network():
    assert Network("1.1.1.0",24).get_network() == "1.1.1.0"

