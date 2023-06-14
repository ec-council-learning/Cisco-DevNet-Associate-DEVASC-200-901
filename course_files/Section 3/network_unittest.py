import unittest
from network import Network


def setUpModule():
    print("## Executing the setup module")

def tearDownModule():
    print('## Executing the tear-down module')


class TestNetwork(unittest.TestCase):

    def setUp(self):
        #create resources on per test basis
        print("Executing the setup action")
        self.network = Network("3.3.3.0",30)

    def test_get_host_count(self):
        print("Executing test 1")
        self.assertEqual(self.network.get_host_count(), 4, "Expected to be 4")
        #self.assertEqual(Network("1.1.1.0",30).get_host_count(), 4, "Expected to be 4")
        self.assertTrue(Network("1.1.1.0",24).get_host_count()== 256, "Expected to be 256")

    def test_get_network(self):
        print("Executing test 2")
        self.assertEqual(Network("1.1.1.0",30).get_network(), "1.1.1.0")
        self.assertEqual(Network("1.1.2.0",30).get_network(), "1.1.2.0")
        self.assertEqual(Network("2.2.2.0",30).get_network(), "2.3.2.0")

    def tearDown(self):
        print('Executing the tear-down action')

if __name__ == '__main__':
    unittest.main()