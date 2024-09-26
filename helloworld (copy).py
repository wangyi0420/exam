import turtle

# 设置turtle的速度和背景颜色
turtle.speed(10)
turtle.bgcolor("skyblue")

# 定义绘制树的递归函数
def draw_branch(branch_length):
    if branch_length > 5:
        # 绘制树干部分
        turtle.forward(branch_length)
        # 右转一个角度
        turtle.right(20)
        # 绘制右侧的树枝
        draw_branch(branch_length - 15)
        # 左转双倍角度
        turtle.left(40)
        # 绘制左侧的树枝
        draw_branch(branch_length - 15)
        # 回到上一个状态
        turtle.right(20)
        turtle.backward(branch_length)

# 设置初始位置和初始朝向
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.left(90)

# 设置笔的颜色和宽度
turtle.color("brown")
turtle.pensize(4)

# 开始绘制树
draw_branch(100)

# 隐藏turtle
turtle.hideturtle()

# 完成绘制
turtle.done()
