from mendeleev import element
import random


def generate_ques():
    atno = random.randint(0,118)
    ele = element(atno)
    ans = ele.symbol
    return atno, ans


def main(result):
    atno, ans = generate_ques()
    return result == ans

