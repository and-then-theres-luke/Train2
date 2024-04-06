import unittest
import asyncio
from unittest.mock import AsyncMock, patch
from route import Route
from station import Station
from train import Train

class TestStation(unittest.IsolatedAsyncioTestCase):
    async def test_init(self):
        station_name = "Test Station"
        station = Station(station_name)
        self.assertEqual(station.name, station_name)
        self.assertListEqual(station.trains, [])
        self.assertListEqual(station.tracks, [False, False])

    async def test_add_train(self):
        station = Station("Test Station")
        train = Train("Test Train", Route())

        await station.add_train(train)

        self.assertListEqual(station.trains, [train])
        self.assertTrue(station.tracks[0])

    async def test_remove_train(self):
        station = Station("Test Station")
        train = Train("Test Train", Route())
        station.trains.append(train)
        station.tracks[0] = True

        await station.remove_train(train)

        self.assertListEqual(station.trains, [])
        self.assertFalse(station.tracks[0])
        
if __name__ == '__main__':
    unittest.main()