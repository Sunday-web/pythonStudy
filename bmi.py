h=input('请输入身高（厘米）：')
w=input('请输入体重（公斤）：')
height = float(h)/100
weight = float(w)
bmi = weight/(height*height)
print('你的bmi指数为:%.2f' % bmi)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
#不用忘记判断条件后的冒号

