import psutil


def check_is_running(name):
    return name in (p.name() for p in psutil.process_iter())
