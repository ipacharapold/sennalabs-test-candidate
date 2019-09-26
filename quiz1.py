def helloString(string_input):
    return "Hello, {string}!".format(string=string_input)

if __name__ == '__main__':
    print(helloString('Sennalabs'))