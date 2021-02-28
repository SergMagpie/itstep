from requests import get
from io import BytesIO
from zipfile import ZipFile
from pandas import read_excel
import os


def get_file(url_name=None, file_name=None):
    if not url_name:
        url_name = input('Enter url adress ')
    if not file_name:
        file_name = input('Enter file name ')
    r = get(url_name)
    with open(file_name, "wb") as code:
        code.write(r.content)


def unzip_file(file_name=None, path_name=None):
    if not file_name:
        file_name = input('Enter url file name ')
    if not path_name:
        path_name = input('Enter path name ')
    with ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(path_name)


def new_func(get_file, unzip_file):
    get_file("https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip",
             "training_ground/excel/rogaikopyta.zip")
    unzip_file("training_ground/excel/rogaikopyta.zip",
               "training_ground/excel/rogaikopyta")


new_func(get_file, unzip_file)

file_list = os.listdir("training_ground/excel/rogaikopyta")
list_text = []
for file in file_list:
    s, d = read_excel(
        "training_ground/excel/rogaikopyta/" + file, usecols=[1, 3]).loc[0]
    list_text += [s + ' ' + str(int(d))]
list_text.sort()
text = '\n'.join(list_text)
with open("training_ground/excel/payroll.txt", "w", encoding='utf-8') as file:
    file.write(text)
# delete trash
for file in file_list:
    os.remove("training_ground/excel/rogaikopyta/" + file)
os.rmdir("training_ground/excel/rogaikopyta/")
os.remove("training_ground/excel/rogaikopyta.zip")

print("I'm OK!")
