import unittest
import asyncio
from unittest.mock import AsyncMock, patch
from route import Route
from station import Station
from train import Train

from train import Train, Station, Route

class TestTrain(unittest.IsolatedAsyncioTestCase):
    async def test_init(self):
        train_name = "Test Train"
        route = Route(Station("Station 1"), Station("Station 2"))
        train = Train(train_name, route)
        self.assertEqual(train.name, train_name)
        self.assertEqual(train.route, route)
        self.assertIsNone(train.current_station)

    async def test_move_to_next_station(self):
        station_1 = Station("Station 1")
        station_2 = Station("Station 2")
        route = Route(station_1, station_2)
        train = Train("Test Train", route)
        train.current_station = station_1

        with patch('train.asyncio.sleep', new=AsyncMock()) as mock_sleep:
            await train.move_to_next_station()

        mock_sleep.assert_called_once_with(5)
        self.assertEqual(train.current_station, station_2)

    async def test_wait_at_station(self):
        station = Station("Station 1")
        route = Route(station)
        train = Train("Test Train", route)
        train.current_station = station

        with patch('train.asyncio.get_event_loop') as mock_get_event_loop:
            mock_event_loop = mock_get_event_loop.return_value
            mock_event_loop.create_task = AsyncMock()

            await train.wait_at_station()

        mock_event_loop.create_task.assert_called_once_with(train.move_to_next_station())



if __name__ == '__main__':
    unittest.main()