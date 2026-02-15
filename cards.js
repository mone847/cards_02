// カード画像のベースURL（cards_assets リポジトリの GitHub Pages）
const BASE_URL = "https://mone847.github.io/cards_assets/cards_img/";

// 52枚分のカードURL配列を作成
const cardList = [];
for (let i = 1; i <= 52; i++) {
  cardList.push(`${BASE_URL}c${i}.svg`);
}

// グローバルに公開（Python から参照）
window.cards = {
  list: cardList,

  // index 番目のカードURLを返す関数
  getUrl: function (index) {
    // index が範囲外なら 0〜51 に丸める
    const n = ((index % this.list.length) + this.list.length) % this.list.length;
    return this.list[n];
  },

  length: cardList.length
};