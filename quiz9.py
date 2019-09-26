import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import os

def BNK48():
    # Download elements in web page
    url = "https://www.bnk48.com/index.php?page=members"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    imgs = soup.findAll('div', attrs={'class': 'ImgMem'})
    names = soup.findAll('div', attrs={'class': 'nameMem'})

    #Parser div element that collect name of members
    namesMem = []
    for i in names:
        namesMem.append(str(i).replace(" ","").replace("\n",""))

    # Setup folder to store images
    URL = "https://www.bnk48.com/"
    DIRECTORY = 'BNK48_pictures'
    my_dir = os.path.dirname(__file__)
    file_path = os.path.join(my_dir, DIRECTORY)
    if not (os.path.exists(file_path)):
        os.makedirs(file_path)

    # Regular Expression to find Name and Image url
    nameMem =[]
    imgMem = []
    regex_name = r">(.*?)<"
    regex_img = r"(url)\((.*?)\)"

    for img in imgs:
        matches = re.findall(regex_img, str(img))
        imgMem.append("{url}{dyn}".format(url=URL, dyn=matches[0][1]))

    for name in namesMem:
        matches = re.findall(regex_name, str(name))
        nameMem.append(matches[0])

    # Download Part to store in directory
    for i in range(len(nameMem)):
        urllib.request.urlretrieve(imgMem[i], "{}/{}.jpg".format(file_path,nameMem[i]))

    print('Download Successfully...')

if __name__ == '__main__':
    BNK48()