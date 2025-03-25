import shutil
import os

from datetime import datetime, timedelta


def seconds_to_readable_time(seconds):
    if not seconds:
        return None
    """
    Convert milliseconds to readable time
    """
    minutes = seconds // 60
    hours = minutes // 60

    seconds = seconds % 60
    minutes = minutes % 60

    time_string = ""

    if hours > 0:
        time_string += f"{round(hours)}h"
    if minutes > 0:
        time_string += f"{round(minutes)}m"
    if seconds > 0 or time_string == "":
        time_string += f"{round(seconds)}s"

    return time_string


def format_percentage_change(daily_value, prev_period_value):
    if not daily_value or not prev_period_value:
        return None
    if prev_period_value == 0:
        if daily_value > 0:
            return "(➚100%)"
        elif daily_value < 0:
            return "(➘100%)"
        else:
            return "(≈0%)"

    difference = ((daily_value - prev_period_value) / prev_period_value) * 100
    if difference >= 0.1:
        return f"(➚{difference:.1f}%)"
    elif difference < 0:
        return f"(➘{abs(difference):.1f}%)"
    else:
        return "(≈0%)"


def get_start_end_of_week_by_offset(week_offset) -> tuple:
    if not week_offset:
        return None
    """
    Returns the start (Monday) and end (Sunday) dates of the week determined by a given week offset
    relative to the current date.
    Args:
        week_offset (int): The offset (number of weeks) from the current week.
            - week_offset = 0: The current week.
            - week_offset = 1: The previous week.
            - week_offset = -1: The next week.
    Returns:
        tuple: A tuple containing the start (Monday) and end (Sunday) dates of the specified week in 'YYYY-MM-DD' format.
    """
    today = datetime.today()
    start_of_week = (
        today - timedelta(days=today.weekday()) - timedelta(weeks=week_offset)
    )
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week


def free_up_disk_space(to_remove: str):
    if not to_remove:
        return None
    print("Cleaning up...", to_remove)
    try:
        if os.path.isdir(to_remove):
            shutil.rmtree(to_remove)
            print(f"Folder {to_remove} has been removed.")
        elif os.path.isfile(to_remove):
            os.remove(to_remove)
            print(f"File {to_remove} has been removed.")
    except FileNotFoundError:
        print(f"{to_remove} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def format_bytes(bytes) -> str:
    if not bytes:
        return None

    units = ["TB", "GB", "MB", "KB"]
    sizes = [
        1024**4,  # TB
        1024**3,  # GB
        1024**2,  # MB
        1024**1,  # KB
    ]

    for i in range(len(sizes)):
        if bytes >= sizes[i]:
            return f"{(bytes / sizes[i]):.2f} {units[i]}"

    return f"{bytes} B"  # For values smaller than 1 KB
