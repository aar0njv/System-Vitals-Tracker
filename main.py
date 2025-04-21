from app import cpu_load, disk_usage, memory_usage, running_services, uptime
from utils.formatter import bytes_to_gb, format_percentage


def print_title(title):
    print("\n\n" + "="*50)
    print(title)
    print("="*50)


def main():

    print("\n System Health Monitoring ")


    print_title("Disk Usage")                   # Disk Usage
    disk_data = disk_usage.get_disk_usage()
    for mount, data in disk_data.items():
        total_gb = bytes_to_gb(data['total'])
        used_gb = bytes_to_gb(data['used'])
        free_gb = bytes_to_gb(data['free'])
        percent = data['percent']
        print("{}: {:.2f} GB used out of {:.2f} GB total ({}%, remaining {:.2f} GB free)".format(mount, used_gb, total_gb, percent,free_gb))



    print_title("CPU Load")                     # CPU Usage
    load = cpu_load.get_cpu_load()
    if load is not None:
        print("CPU Usage: {0}%".format(load['CPU Usage (%)']))
        print("User Time: {0}s | System Time: {1}s | Idle Time: {2}s".format(load['User Time (seconds)'], load['System Time (seconds)'], load['Idle Time (seconds)']))
    else:
        print("Error: Unable to retrieve CPU load data.")



    print_title("Memory Usage")                 # Memory Usage
    mem = memory_usage.get_memory_usage()
    total_gb = mem['total']
    used_gb = mem['used']
    free_gb = mem['free']
    available_gb = mem['available']
    percent = mem['percent']
    print("Total: {0:.2f} GB | Used: {1:.2f} GB | Free: {2:.2f} GB | Available: {3:.2f} GB ({4}%)".format(total_gb, used_gb, free_gb, available_gb, percent))



    print_title("Running Services")             # Running Services
    services = running_services.get_running_services()
    if isinstance(services, list):
        if services == ["No actively running services found."]:
            print(services[0])
        else:
            for service in services:
                print("PID: {0} | Name: {1} | Status: {2}".format(service['pid'], service['name'], service['status']))
    else:
        print(services)  



    print_title("System Uptime")                # Uptime
    print(uptime.get_uptime())
    print("\n")

if __name__ == "__main__":
    main()
