import datetime
import os
import json
import time

import functions


class WaterSchedule:

    def __init__(self):
        self.__loadJson()
        self.__FirstDay = self.__wateringInfo["DaysToWater"][0]["FirstDay"]
        self.__SecondDay = self.__wateringInfo["DaysToWater"][0]["SecondDay"]
        self.__WateringHour = str(self.__wateringInfo["TimeToWater"][0]["Hour"])
        self.__WateringMinute = str(self.__wateringInfo["TimeToWater"][0]["Minute"])
        self.__ampmTime = self.__wateringInfo["TimeToWater"][0]["AmPm"]
        self.__TimeToWater = datetime.time(int(self.__WateringHour),int(self.__WateringMinute)).strftime('%I:%M %p')
        print("First watering day is: " + self.__FirstDay)
        print("Second watering day is: " + self.__SecondDay)
        print("The time the lawn will be watered is: " + str(self.__TimeToWater))
    def __loadJson(self):
        directory = os.path.dirname(__file__)
        fileLoc = os.path.join(directory, 'waterSettings.json')
        JSONfile = open(fileLoc, 'r')
        self.__wateringInfo = json.load(JSONfile)
        JSONfile.close()

    def isWateringTime(self):
        return functions.getCurrentTime() == self.__TimeToWater

    def isWateringDay(self):
        if functions.getDayOfWeek() == self.__FirstDay or functions.getDayOfWeek() == self.__SecondDay:
            return True
        else:
            return False
