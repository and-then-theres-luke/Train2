from train import Train
from station import Station
from route import Route
import asyncio

# Create some stations
station1 = Station("Station 1")
station2 = Station("Station 2")
station3 = Station("Station 3")
station4 = Station("Station 4")
station5 = Station("Station 5")

# Create some trains
train1 = Train("Train 1", Route(station1, station2, station3))
train2 = Train("Train 2", Route(station1, station2, station4, station5))
train3 = Train("Train 3", Route(station1, station2, station3))
train4 = Train("Train 4", Route(station1, station2, station4, station5))
train5 = Train("Train 5", Route(station1, station2, station3))

async def run_trains():
    trains = [train1,train2,train3,train4,train5]
    for train in trains:
        train.current_station = train.route.stations[0]
    while True:
        for train in trains:
            train.wait_at_station()
        await asyncio.sleep(5)  # Simulate time delay
        
# Start the simulation
loop = asyncio.get_event_loop()
loop.run_until_complete(run_trains())
