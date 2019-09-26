import csv
import os

def read_csv(file):
    output = ""
    people = {}
    file = open(file, 'r')
    render = csv.reader(file)

    for row in render:
        people[row[1]] = row[0]

    for lname, fname in sorted(people.items()):
        output += "{first}{last}\n".format(first=fname, last=lname)
    file.close()
    return output

if __name__ == '__main__':
    print(read_csv('quiz2.csv'))
