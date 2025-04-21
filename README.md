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
├── main.py                        
├── app/                           
│   ├── __init__.py                # Makes this a Python package (can be empty)
│   ├── disk_usage.py              # Checks disk space
│   ├── cpu_load.py                # Checks CPU usage
│   ├── memory_usage.py            # Checks memory usage
│   ├── running_services.py        # Checks running services
│   ├── uptime.py                  # Checks system uptime
│
├── utils/                         # Helper functions
│   ├── __init__.py
│   └── formatter.py               
│
└── requirements.txt               
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



## License

This project is licensed under the MIT License.


Made with ❤️ by [Aaron]


