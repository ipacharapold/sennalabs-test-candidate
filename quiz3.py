def lottery(num_win):
    list_winning = []

    for num in range(int(str(num_win)[-2:]), 1000000, 100):
        temp = "{number:06d}".format(number=num)
        list_winning.append(temp)
    return list_winning

if __name__ == '__main__':
    print(lottery(199872))