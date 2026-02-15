from js import document, window
import random
import asyncio

img1 = document.getElementById("card1-img")
img2 = document.getElementById("card2-img")

_cards = None
_busy = False

async def _ensure_cards():
    global _cards
    if _cards is not None:
        return _cards
    while not hasattr(window, "cards"):
        await asyncio.sleep(0)
    _cards = window.cards
    return _cards

async def _shuffle_async():
    global _busy
    if _busy:
        return
    _busy = True
    try:
        cards = await _ensure_cards()
        n = int(cards.length)
        i1, i2 = random.sample(range(n+1), 2)
        img1.src = cards.getUrl(i1)
        img2.src = cards.getUrl(i2)
    finally:
        _busy = False

def shuffle_and_show(event=None):
    asyncio.create_task(_shuffle_async())

# 初期表示（任意）
asyncio.create_task(_shuffle_async())