def convert_list(number):
    """Convert Number to list of digits"""
    return [str(num) for num in str(number)]

def rearrange(num):
    output = []

    if num.__len__() == 1:
        return num
    else:
        for index, pointer in enumerate(num):
            for temp in rearrange(num[:index]+num[index+1:]):
                output += [pointer+temp]
    return output

if __name__ == '__main__':
    number = convert_list(209324)
    print(rearrange(number))