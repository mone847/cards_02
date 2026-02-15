from js import document, window
import random

# JavaScript 側の cards オブジェクトを取得
cards = window.cards

# img 要素とボタン要素
img1 = document.getElementById("card1-img")
img2 = document.getElementById("card2-img")
shuffle_btn = document.getElementById("shuffle-btn")


def shuffle_and_show(event=None):
    """カードをシャッフルして先頭2枚を表示"""
    # 0〜(枚数-1) のインデックスリストを作成
    indices = list(range(cards.length))
    # ランダムに並べ替え
    random.shuffle(indices)  # in-place シャッフル[web:110][web:112][web:116][web:119]

    # 先頭2枚の URL を取得
    first = cards.getUrl(indices[0])
    second = cards.getUrl(indices[1])

    # img の src を更新
    img1.src = first_url
    img2.src = second_url


# ボタンにハンドラ登録
shuffle_btn.addEventListener("click", shuffle_and_show)

# 初期表示もシャッフル結果にする
shuffle_and_show()