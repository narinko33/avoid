from random import randint as ri


# 追加：Commentクラス、インスタンス化する時に
# x座標、y座標、tagを指定。コメントと色はランダムでコントラクタで決まる。
class Comment:
    def __init__(self, start_posx, start_posy, tag):
        # 引数から初期値セット
        self.start_posx = start_posx
        self.start_posy = start_posy
        self.tag = tag
        # コントラクタ内で初期値セット
        self.id = 0
        self.text = comment[ri(0, len(comment) - 1)]
        self.color = fill_list[ri(0, len(fill_list) - 1)]


comment = [
    "初見です。こんにちは",
    "いつも見てます！頑張ってください！",
    "おばあちゃんの味、使いきりサイズ",
    "ひき肉です",
    "ブンブンハローYOUTUBE",
    "捌いていく！",
    "全YOUTUBERに告ぐ！道を開けろ！",
    "ぴっぴっぴー！山口県から来ました！コラボしてください！",
    "ウホッ",
    "人生は冒険や！！！",
    "なくなったら追加するだけや",
    "ハイサーイ",
    "寿限無寿限無うんこ投げ器一昨日の新ちゃんのパンツ",
    "素に銀と鉄。礎に石と契約の大公",
    "I am the bone of my sword.",
    "佐々木先生のおかげで楽しく勉強できてます！！",
    "金曜日の騒音をどうにかすることを検討してください",
    "それってあなたの感想ですよね？",
    "スパチャってどうやって投げるんですか？",
    "お茶(´･ω･)っ旦~",
    "キタ―――(゚∀゚)――――",
]

fill_list = [
    "white",
    "white",
    "white",
    "white",
    "red",
    "yellow",
    "yellow",
    "green",
    "green",
    "green",
]