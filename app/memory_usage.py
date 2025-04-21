import psutil as ps
from utils.formatter import bytes_to_gb

def get_memory_usage():
    virtual_memory = ps.virtual_memory()

    memory_statistics = {
        "total": virtual_memory.total,
        "used": virtual_memory.used,
        "free": virtual_memory.free,
        "percent": virtual_memory.percent,
        "available": virtual_memory.available
    }

    return {
        "total": round(bytes_to_gb(memory_statistics["total"]), 2),
        "used": round(bytes_to_gb(memory_statistics["used"]), 2),
        "free": round(bytes_to_gb(memory_statistics["free"]), 2),
        "percent": memory_statistics["percent"],
        "available": round(bytes_to_gb(memory_statistics["available"]), 2)
    }
