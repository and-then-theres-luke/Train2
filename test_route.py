import unittest
import asyncio
from unittest.mock import AsyncMock, patch
from route import Route
from station import Station
from train import Train

class TestRoute(unittest.TestCase):
    def test_init(self):
        station_1 = Station("Station 1")
        station_2 = Station("Station 2")
        route = Route(station_1, station_2)
        self.assertListEqual(route.stations, [station_1, station_2])

    def test_add_station(self):
        station_1 = Station("Station 1")
        station_2 = Station("Station 2")
        route = Route(station_1)

        route.add_station(station_2)

        self.assertListEqual(route.stations, [station_1, station_2])

    def test_remove_station(self):
        station_1 = Station("Station 1")
        station_2 = Station("Station 2")
        route = Route(station_1, station_2)

        route.remove_station(station_2)

        self.assertListEqual(route.stations, [station_1])

    def test_get_stations(self):
        station_1 = Station("Station 1")
        station_2 = Station("Station 2")
        route = Route(station_1, station_2)

        self.assertListEqual(route.get_stations(), [station_1, station_2])
        
if __name__ == '__main__':
    unittest.main()