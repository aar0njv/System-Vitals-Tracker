
def bytes_to_gb(bytes_val, decimal_places = 2):

    gb = bytes_val / (1000**3)
    return round(gb, decimal_places)


def bytes_to_mb(bytes_val, decimal_places = 2):

    mb = bytes_val / (1000**2)
    return round(mb, decimal_places)


def format_percentage(used,total,decimal_places = 2):
    if total == 0:
        return 0

    percentage = (used/total) * 100
    return round(percentage, decimal_places)