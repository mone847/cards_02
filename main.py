from js import document, window
import random
import asyncio

img1 = document.getElementById("card1-img")
img2 = document.getElementById("card2-img")

async def _get_cards():
    # cards.js が window.cards を作るまで待つ
    while not hasattr(window, "cards"):
        await asyncio.sleep(0)
    return window.cards

async def shuffle_and_show(event=None):
    cards = await _get_cards()

    # JS の length を Python int に
    n = int(cards.length)

    indices = list(range(n))
    random.shuffle(indices)

    img1.src = cards.getUrl(indices[0])
    img2.src = cards.getUrl(indices[1])

# 初期表示もシャッフル
asyncio.create_task(shuffle_and_show())