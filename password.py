password = "a123456"
i = 3
while i > 0:
    word = input("請輸入密碼： ")
    if word == password:
        print("登入成功！")
        break
    else:
        i -= 1
        print("密碼錯誤，還剩下", i, "次機會")
