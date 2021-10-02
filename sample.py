def calc(number):
    if number == 0:
        return "ゼロです。"
    elif number == 1:
        return "イチです。"
    elif number == 2:
        return "二です。"
    else:
        return "どれでもありません。"

if __name__ == "__main__":
    for i in range(1,4):
        calc(i)