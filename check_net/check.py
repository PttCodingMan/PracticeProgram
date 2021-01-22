import time
import requests
import urllib3

from SingleLog.log import Logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = Logger('check_bot', Logger.INFO)

first = True
last_state = None
while True:
    if not first:
        if last_state == 'error':
            time.sleep(1)
        else:
            time.sleep(1)
    else:
        first = False

    try:
        r = requests.post('https://www.google.com', timeout=1.5)
    except requests.exceptions.ConnectionError:
        if last_state == 'error':
            continue
        last_state = 'error'
        logger.show(Logger.INFO, '連線狀態', 'ConnectionError')
        continue
    except requests.exceptions.ReadTimeout:
        if last_state == 'error':
            continue
        last_state = 'error'
        logger.show(Logger.INFO, '連線狀態', 'ReadTimeout')
        continue

    if last_state == 'ok':
        continue
    last_state = 'ok'
    logger.show(Logger.INFO, '連線狀態', '正常')
