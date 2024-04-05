import time
import asyncio

class Station:
    def __init__(self, name):
        self.name = name
        self.trains = []  # List of trains at the station
        self.tracks = [False, False]  # Boolean to indicate if each track is occupied

    def add_train(self, train):
        for i in range(len(self.tracks)):
            if self.tracks[i] == True:
                pass
            elif self.tracks[i] == self.tracks[-1]:
                i = 0
            else:
                self.trains.append(train)
                self.tracks[i] = True  # Mark the track as occupied

    def remove_train(self, train):
        if train in self.trains:
            self.trains.remove(train)
            if not self.tracks[1]:
                self.tracks[0] = False
            else:
                self.tracks[1] = False


# class Station:
#     def __init__(self, name):
#         self.name = name
#         self.trains = []

#     def add_train(self, train):
#         if train not in self.trains:
#             self.trains.append(train)

#     def remove_train(self, train):
#         if train in self.trains:
#             self.trains.remove(train)