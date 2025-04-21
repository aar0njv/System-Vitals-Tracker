import psutil as ps

def get_running_services():
    running_services = []

    for proc in ps.process_iter(['pid', 'name', 'status']):
        try:
            if proc.info['status'] == ps.STATUS_RUNNING:    #.info returns a dict with each of above mentioned attributes
                running_services.append(proc.info)  
        except (ps.NoSuchProcess, ps.AccessDenied, ps.ZombieProcess):
            continue

    
    if not running_services:
        return ["No actively running services found."]

    return running_services
