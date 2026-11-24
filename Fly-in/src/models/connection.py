class Connection:
    def __init__(self, zone1: str, zone2: str, max_link_capacity: int):
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity

    def __eq__(self, other):
        return (self.zone1 == other.zone1 and self.zone2 == other.zone2)

    def print_connection(self):
        print(f"Connection: {self.zone1} -> {self.zone2}, Max Link Capacity: {self.max_link_capacity}")
