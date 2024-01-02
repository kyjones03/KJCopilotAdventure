"""
Objective
- Your task is to create a system that checks all the clocks in the town and synchronizes them with the Grand Clock Tower. 
- You'll be given a list of times from various clocks around the town, and you must determine how many minutes each clock is ahead or behind the Grand Clock Tower's time.
"""

"""
Inputs - Clock Data
- Clock times are provided as a list of strings in the format "HH:MM" (hours and minutes) in 24-hour time
- The Grand Clock Tower is at 15:00
- Clock times around town are:
    Clock 1 - 14:45
    Clock 2 - 15:05
    Clock 3 - 15:00
    Clock 4 - 14:40
"""

"""
Outputs
- You need to determine how many minutes each clock is ahead or behind the Grand Clock Tower.
- The result should be an array of integers representing the time difference in minutes. 
- Positive values indicate the clock is ahead, and negative values indicate it's behind.
"""

# Variables
clockData = ["14:45", "15:05", "15:00", "14:40"]

def clockSync(clockData):
    """
    Calculates the time difference between each clock and the Grand Clock Tower.

    Parameters:
    clockData (list): A list of strings representing the time of each clock in the town.

    Returns:
    list: A list of integers representing the time difference between each clock and the Grand Clock Tower.
    """
    grandClock = "15:00"
    timeDifference = []
    for clock in clockData:
        # Split the clock time into hours and minutes
        clockHours = int(clock.split(":")[0])
        clockMinutes = int(clock.split(":")[1])
        # Split the grand clock time into hours and minutes
        grandClockHours = int(grandClock.split(":")[0])
        grandClockMinutes = int(grandClock.split(":")[1])
        # Calculate the difference in hours and minutes
        hourDifference = clockHours - grandClockHours
        minuteDifference = clockMinutes - grandClockMinutes
        # Convert the difference in hours to minutes
        hourDifferenceInMinutes = hourDifference * 60
        # Add the hour and minute differences together
        totalDifference = hourDifferenceInMinutes + minuteDifference
        # Add the total difference to the timeDifference list
        timeDifference.append(totalDifference)
    return timeDifference

print(clockSync(clockData))