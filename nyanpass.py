"""
にゃんぱすーボタン (https://nyanpass.com )の非公式APIラッパーなのん

Warning
-------------
サーバーの負荷にならないように節度を持ったアクセスを心がけるのん

Usage:
    ::
    >>> import nyanpass
    >>> n = nyanpass.Nyanpass()
    >>> now_time, now_nyanpass = n.get()
    >>> print(f"{now_time} のにゃんぱすーは {now_nyanpass}")
    2020-08-19 21:40:18 のにゃんぱすーは 21320503798
    ::

"""
import requests
import datetime


BASE_URL = "http://nyanpass.com/"


class Nyanpass:
    """
    にゃんぱすーボタンAPIを叩くクライアントクラス
    """

    def __init__(self):
        self.session = requests.Session()

    def get(self) -> tuple:
        """
        実行時時点のにゃんぱす数を取得するのん。
        Returns
        --------------
        now : datetime
            取得した時間(秒まで)

        nyanpass : int
            取得時点のにゃんぱすーカウント
        """
        r = self.session.get(f"{BASE_URL}api/get_count")
        r.raise_for_status()
        now = datetime.datetime.strptime(
            str(r.json()["time"]), r"%Y-%m-%d %H:%M:%S")
        nyanpass = int(r.json()["count"])
        return now, nyanpass
