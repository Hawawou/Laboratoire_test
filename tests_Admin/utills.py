import time


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)
