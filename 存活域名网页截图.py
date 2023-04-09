import sys

def E():
    T()
    E1()

def T():
    F()
    T1()

def E1():
    global word
    if word == "+":
        word = get_w()
        T()
        E1()
    elif word == "#" or word == ")":
        pass
    else:
        error("匹配错误2")

def T1():
    global word
    if word == "*":
        word = get_w()
        F()
        T1()
    elif word == "+" or word == "#" or word == ")":
        pass
    else:
        error("匹配错误3")

def F():
    global word
    if word == "(":
        word = get_w()
        E()
        if word == ")":
            word = get_w()
        else:
            error("应有右括号")
    elif word.isdigit() or word.isalpha():
        word = get_w()
    else:
        error("应有运算对象")

def error(message):
    print("不是文法的句子")
    print("错误提示：", message)
    sys.exit(0)

def get_w():
    global input_str
    if len(input_str) > 0:
        ch = input_str[0]
        input_str = input_str[1:]
        return ch
    else:
        return None

while True:
    print("请输入一个串(以#结束):")
    input_str = input()
    word = get_w()
    E()
    if word == "#":
        print("是文法的句子")
    else:
        error("匹配错误1")
