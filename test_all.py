import unittest
from train import Train
from station import Station
from route import Route


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.route = Route(Station("A"), Station("B"), Station("C"))
        self.train = Train("TestTrain", self.route)


    def test_train_initialization(self):
        self.assertEqual(self.train.name, "TestTrain")
        self.assertEqual(self.train.route, self.route)
        self.assertIsNone(self.train.current_station)

    async def test_move_to_next_station(self):
        self.train.current_station = self.route.stations[0]
        await self.train.move_to_next_station()
        self.assertEqual(self.train.current_station, self.route.stations[1])

    async def test_wait_at_station(self):
        self.train.current_station = self.route.stations[0]
        with self.assertLogs('root', level='INFO') as cm:
            await self.train.wait_at_station()
        self.assertEqual(cm.output, [f"{self.train.name} is in transit to {self.route.stations[1].name}..."])
class TestStation(unittest.TestCase):
    def setUp(self):
        self.station = Station("TestStation")


    def test_station_initialization(self):
        self.assertEqual(self.station.name, "TestStation")
        self.assertListEqual(self.station.trains, [])
        self.assertListEqual(self.station.tracks, [False, False])

    async def test_add_train(self):
        train = Train("TestTrain", Route(Station("A")))
        await self.station.add_train(train)
        self.assertListEqual(self.station.trains, [train])
        self.assertListEqual(self.station.tracks, [True, False])

    async def test_remove_train(self):
        train = Train("TestTrain", Route(Station("A")))
        await self.station.add_train(train)
        await self.station.remove_train(train)
        self.assertListEqual(self.station.trains, [])
        self.assertListEqual(self.station.tracks, [False, False])
class TestRoute(unittest.TestCase):
    def setUp(self):
        self.route = Route(Station("A"), Station("B"), Station("C"))


    def test_route_initialization(self):
        self.assertListEqual(self.route.stations, [Station("A"), Station("B"), Station("C")])

    def test_add_station(self):
        new_station = Station("D")
        self.route.add_station(new_station)
        self.assertListEqual(self.route.stations, [Station("A"), Station("B"), Station("C"), Station("D")])

    def test_remove_station(self):
        removed_station = self.route.stations[1]
        self.route.remove_station(removed_station)
        self.assertListEqual(self.route.stations, [Station("A"), Station("C")])

    def test_get_stations(self):
        self.assertListEqual(self.route.get_stations(), [Station("A"), Station("B"), Station("C")])

if __name__ == '__main__':
    unittest.main()