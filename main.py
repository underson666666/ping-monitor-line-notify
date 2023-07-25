import os

import requests
from ping3 import ping

LINE_NOTIFY_API = "https://notify-api.line.me/api/notify"


def main():
    monitor_target = os.getenv("TARGET_HOST")
    is_connected = ping_monitoring(monitor_target)
    if not is_connected:
        msg = f"NOT Connect to {monitor_target}"
        notify_line(msg)


def ping_monitoring(target: str) -> bool:
    """指定したIPアドレスにpingを行い、疎通ができたかを返す

    Parameters
    ----------
    target: str
        IPv4 address

    Returns
    -------
    bool: whether had connected or not
    """
    result = ping(target)
    return isinstance(result, float)


def notify_line(message: str):
    """notify to line notify

    Parameters
    ----------
    message: str
        通知するメッセージ
    """
    api_token = os.getenv("LINE_API_TOKEN")
    headers = {"Authorization": f"Bearer {api_token}"}
    data = {"message": message}
    res = requests.post(LINE_NOTIFY_API, headers=headers, data=data)

    if res.status_code != requests.codes.ok:
        print("failed to send message.")


if __name__ == "__main__":
    main()
