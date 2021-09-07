import datetime
import time #temp import for testing
import json
import os

import WateringScheduler


def getCurrentTime():
    """
    this function will return the current time of day
    :return:
    """

    time = datetime.datetime.now().time().strftime('%I:%M %p')
    return time


def getDayOfWeek():
    """
    this function will return the day of the week as a word(ex: Sunday)
    :return:
    """

    day = 0
    return day


def waterPlants():
    """
    This function will be responsible for accessing all water nozzles and turning them on or off.
    It will access the GPIO pins on the raspberry pi 4 hooked up to system and water for specified
    amount of time from waterSettings.json file. It will only water plants on days of week in json
    file.
    :return:
    """
    waterSchedule = WateringScheduler.WaterSchedule()
    while (not waterSchedule.isWateringTime()):
        print("Not time yet")
        time.sleep(5)
    # if nozzle does not report back true, nozzle is broken somewhere.
    return 0





