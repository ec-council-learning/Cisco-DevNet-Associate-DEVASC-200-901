class Network():
    def __init__(self, network, subnet):
        self.network = network
        self.subnet = subnet
    
    def get_host_count(self):
        
        host_count = 0
        host_count = 2**(32 - self.subnet)
        return host_count
    
    def get_network(self):
        return self.network