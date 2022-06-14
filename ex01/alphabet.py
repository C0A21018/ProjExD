import random
import datetime


NUM_OF_TRIALS = 5        #最大繰り返し回数
NUM_OF_ALL_CHARS = 10    #対象文字数
NUM_OF_ABS_CHAR = 2      #欠損文字数

def main():
    st = datetime.datetime.now()  #時間計測開始
    for _ in range(NUM_OF_TRIALS):
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1:
            break
    ed = datetime.datetime.now()
    print(f"所要時間：{(ed-st).seconds}秒かかりました")

def shutudai():
    alphabets = [chr(c+65) for c in range(26)]
    all_char_lst = random.sample(alphabets, NUM_OF_ALL_CHARS)

    print(f"対象文字：{all_char_lst}")

    abs_char_lst = random.sample(alphabets, NUM_OF_ABS_CHAR)
    print(f"欠損文字：{abs_char_lst}")

    pre_char_lst = [chr(c+65) for c in range(8)]
    print(F"表示文字：{pre_char_lst}")

    return abs_char_lst

def kaitou(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != NUM_OF_ABS_CHAR:
        print("不正解です。またチャレンジして下さい・")
        print("-"*50)
        return 0
    else:
        print("正解です。それでは具体的に欠損文字を１つずつ入力して下さい。")
        for i in range(NUM_OF_ABS_CHAR):
            c = input(f"{i+1}つ目の文字を入力して下さい：")
            if c not in seikai:
                print("不正解です。またチャレンジして下さい。")
                return 0
            seikai.remove(c)
        print("正解です。ゲームを終了します。")
        return 1
        
if __name__ == "__main__":
    alphabets = [chr(c+65) for c in range(26)]
    main()
