import psutil as ps
from datetime import datetime

def get_uptime():
    boot_time = ps.boot_time()      # System boot time
    current_time = datetime.now()  # Current time
    uptime = current_time - datetime.fromtimestamp(boot_time)  # Calculate uptime

    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime_str = f"{days}days {hours}hours {minutes}minutes {seconds}seconds "
    
    return uptime_str