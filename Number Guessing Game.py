print("hello world!")
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('alarm.mp3')
mixer.music.play()

name = input("اسم خود را وارد کنید: ")
print("سلام", " " ,name, sep="")

print("بازی این جوریه که تو یه عدد بین 1 تا 100 در نظر میگیری بعد من اون عدد رو حدس میزنم")
print("بعد تو باید منو راهنمایی کنی تا به جواب برسم")
print("رو وارد کن","ok","اگر براي بازي آماده هستي")
taiid = input()
if taiid == "ok":
    
    import random
    x = 1
    y = 100
    hads = random.randint(x,y)
    print(hads)
    mixer.music.load('Voice002.mp3')
    mixer.music.play()
    rahnamai = input("(b:بزرگتر,k:کوچکتر,d:درست)\n"
                  "عدد مورد نظر شما از عدد حدس زده شده کوچکتر است یا بزرگتر؟ ")

    while (rahnamai != "d"):
        if(rahnamai == "b"):
            x = hads+1
            mixer.music.load('Voice003.mp3')

            mixer.music.play()

        elif(rahnamai=="k"):
            y = hads-1
            mixer.music.load('Voice003.mp3')
            mixer.music.play()
        hads = random.randint(x,y)
        print(hads)
        rahnamai = input("لطفا دوباره راهنمایی کنید")

    print("کامپیوتر درست حدس زد")
    mixer.music.load('Voice004.mp3')
    mixer.music.play()

