# nyanpass.py

[にゃんぱすーボタン](https://nyanpass.com)の非公式 API ラッパーなのん

`スコー ┐(๑¯３¯๑) ┌`

## Note

この API はにゃんぱすーボタンを使う非公式サービスのために作者さんが**粋な計らいでこっそり**追加してくださったん。
作者さんに感謝して、**サーバーの負荷にならないように節度を持ったアクセスを**心がけるのん

## Usage

```py:main.py
import nyanpass
n = nyanpass.Nyanpass()
now_time, now_nyanpass = n.get()
print(f"{now_time} のにゃんぱすーは {now_nyanpass}")

>>> 2020-08-19 21:40:18 のにゃんぱすーは 21320503798
```

## Credits

[にゃんぱすーボタン](https://nyanpass.com)
