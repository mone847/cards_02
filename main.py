from js import document, window
import random
import asyncio

img1 = document.getElementById("card1-img")
img2 = document.getElementById("card2-img")
status = document.getElementById("status")

_cards = None
deck = []       # 山札（c1～c52）
_busy = False

async def _ensure_cards():
    global _cards
    if _cards is not None:
        return _cards
    while not hasattr(window, "cards"):
        await asyncio.sleep(0)
    _cards = window.cards
    return _cards

async def _show_back():
    cards = await _ensure_cards()
    back = cards.getUrl(0)  # 裏面のカード画像URL
    img1.src = back
    img2.src = back

def _update_status():
    status.innerText = f"残りカード: {len(deck)}枚"

async def reset_async():
    global deck
    await _show_back()
    deck = list(range(1, 53))  # c1～c52
    random.shuffle(deck)
    _update_status()

async def _draw_async():
    global _busy
    if _busy:
        return
    _busy = True
    try:
        cards = await _ensure_cards()
        if len(deck) < 2:
            status.innerText = "カードが足りません。リセットしてください。"
            return
        c1 = deck.pop()
        c2 = deck.pop()
        img1.src = cards.getUrl(c1)
        img2.src = cards.getUrl(c2)
        _update_status()

    finally:
        _busy = False

def draw_two(event=None):
    asyncio.create_task(_draw_async())

# 初期表示
asyncio.create_task(_reset_async())