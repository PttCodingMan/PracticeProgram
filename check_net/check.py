import time
import subprocess
import platform

from SingleLog.log import Logger


def ping_ip(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True, timeout=1)
        if 'unreachable' in output:
            return False
        else:
            return True
    except Exception:
        return False


def ping_all():
    for ip in check_list:
        if ping_ip(ip):
            return True
    return False


check_list = [
    '1.1.1.1',
    '168.95.1.1',
    '101.101.101.101'
]

logger = Logger('check_bot', Logger.INFO)
last_state = None
while True:

    time.sleep(1)

    if ping_all():
        if last_state == 'ok':
            continue
        last_state = 'ok'
        logger.info('連線狀態', '正常')
    else:
        if last_state == 'error':
            continue
        last_state = 'error'
        logger.info('連線狀態', 'ConnectionError')
        continue
