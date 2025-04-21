import shutil as sh
from utils.formatter import bytes_to_gb

def get_disk_usage(path="/"):
    total, used, free = sh.disk_usage(path)

    disk_data = {
        "total": total,
        "used": used,
        "free": free,
        "percent": round((used / total) * 100, 2)
    }

    return {path: disk_data}
