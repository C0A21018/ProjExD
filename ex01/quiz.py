import random

def main():
    seikai = shutudai()
    kaitou(seikai)

def shutudai():
    print("問題：")
    m1 = "サザエの旦那の名前は？" 
    m2 = "カツオの妹の名前は？"
    m3 = "タラオはカツオから見てどんな関係？"
    mondai = [m1, m2, m3]
    k1 = "マスオ"
    k2 = "ますお"
    k3 = "ワカメ"
    k4 = "わかめ"
    k5 = "甥"
    k6 = "おい"
    k7 = "甥っ子"
    k8 = "おいっこ"
    kotae = [k1, k2, k3, k4, k5, k6, k7, k8]
    m = random.choice(mondai)
    print(m)
    return m

def kaitou(seikai):
    m1 = "サザエの旦那の名前は？" 
    m2 = "カツオの妹の名前は？"
    m3 = "タラオはカツオから見てどんな関係？"
    mondai = [m1, m2, m3]
    k1 = "マスオ"
    k2 = "ますお"
    k3 = "ワカメ"
    k4 = "わかめ"
    k5 = "甥"
    k6 = "おい"
    k7 = "甥っ子"
    k8 = "おいっこ"
    kotae = [k1, k2, k3, k4, k5, k6, k7, k8]
    string = input("答えを入力して下さい：")
    if seikai == m1:
        if string == k1 or k2:
            print("正解！")
        else:
            print("不正解")
    elif seikai == m2:
        if string == k3 or k4:
            print("正解！")
        else:
            print("不正解")
    elif seikai == m3:
        if string == k5 or k6 or k7 or k8:
            print("正解！")
        else:
            print("不正解")

if __name__ == "__main__":
    main()


