class Route:
    def __init__(self, *stations):
        self.stations = list(stations)

    def add_station(self, station):
        if station not in self.stations:
            self.stations.append(station)

    def remove_station(self, station):
        if station in self.stations:
            self.stations.remove(station)

    def get_stations(self):
        return self.stations
