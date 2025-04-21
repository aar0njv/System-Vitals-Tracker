import psutil as ps


def get_cpu_load():

    cpu_percent = ps.cpu_percent(interval = 1)

    cpu_times = ps.cpu_times()

    cpu_statistics = {
        "CPU Usage (%)": cpu_percent,
        "User Time (seconds)": cpu_times.user,
        "System Time (seconds)": cpu_times.system,
        "Idle Time (seconds)": cpu_times.idle
    }

    return cpu_statistics
