"""
演示if-elif-else 多条件判断语句的使用
"""
# 可以将input输入语句直接写入判断条件中，节省代码量
# 条件的判断是互斥的，上一个满足后面的就不会判断了
# 通过if判断，可以使用多条件判断语法
# 第一个条件就是if
if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于120cm，可以免费。")

elif int(input("请输入你的VIP等级（1~5）：")) > 3:
    print("您的vip级别大于3，可以免费游玩。")
elif int(input("请告诉我今天几号（1~31）：")) == 1:
    print("今天是1号免费日，可以免费。")
else:
    print("不好意思，条件都不满足，需要买票10元。")
