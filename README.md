## Features

**CPU Load**: Displays CPU usage, user time, system time, and idle time.

**Disk Usage**: Monitors the disk usage of the system, including total, used, free space, and percentage usage.

**Memory Usage**: Tracks total, used, free, and available memory along with memory usage percentage.

**Running Services**: Lists all running services with their PID, name, and status.

**Uptime**: Displays the system's uptime since the last boot.

## Folder Structure
<pre>
system_health_monitor/
│
├── main.py                        # Entry point: runs all checks
├── app/                           # Folder for system health check modules
│   ├── __init__.py                # Makes this a Python package (can be empty)
│   ├── disk_usage.py              # Checks disk space
│   ├── cpu_load.py                # Checks CPU usage
│   ├── memory_usage.py            # Checks memory usage
│   ├── running_services.py        # Checks running services
│   ├── security_updates.py        # Checks pending security updates
│   ├── uptime.py                  # Checks system uptime
│
├── utils/                         # Helper functions
│   ├── __init__.py
│   └── formatter.py               # e.g., bytes to GB
│
└── requirements.txt               # Dependencies (like psutil, if used)
</pre>


                     
## Installation

To get started with System-Vitals-Tracker, you'll need to have Python 3.x installed.

### Clone the repository:

git clone https://github.com/yourusername/System-Vitals-Tracker.git
cd System-Vitals-Tracker


### Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'


### Install the required dependencies:

pip install -r requirements.txt


### Usage

To run the system health monitoring, simply execute the following command:

python main.py

This will display the health metrics of your system, including disk usage, CPU load, memory usage, running services, and uptime.


### Sample Output

System Health Monitoring 

==================================================
Disk Usage
==================================================
/: 24.66 GB used out of 46.12 GB total (53.46%, remaining 19.09 GB free)

==================================================
CPU Load
==================================================
CPU Usage: 0.6%
User Time: 654.84s | System Time: 276.83s | Idle Time: 32669.94s

==================================================
Memory Usage
==================================================
Total: 16.15 GB | Used: 3.17 GB | Free: 10.27 GB | Available: 12.58 GB (22.1%)

==================================================
Running Services
==================================================
PID: 14052 | Name: python3 | Status: running

==================================================
System Uptime
==================================================
0days 1hours 26minutes 54seconds


## License

This project is licensed under the MIT License.


Made with ❤️ by [Aaron]


