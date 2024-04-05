import time
import asyncio

class Train:
    def __init__(self, name, route):
            self.name = name
            self.route = route
            self.current_station = None

    async def move_to_next_station(self):
        """Move the train to the next station on its route"""
        await asyncio.sleep(5)  # Wait for 5 minutes at the current station
        full_route = self.route.get_stations()
        await self.current_station.remove_train(self)
        for index in range(len(full_route)):
            if self.current_station == full_route[-1]:
                print("Returning to origin...")
                self.current_station = full_route[0]
                break
            elif self.current_station == full_route[index]:
                print("Moving to next stop...")
                self.current_station = full_route[index+1]
                break
        print(f"{self.name} is in transit to {self.current_station.name}...")
        await asyncio.sleep(30)
        await self.current_station.add_train(self)

    def wait_at_station(self):
        """Wait at the station for 5 minutes and then check for arrival"""
        asyncio.get_event_loop().create_task(self.move_to_next_station())
    