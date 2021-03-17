import os
# Finding a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# Create an absolute path to the file.


def files_copy(file_name: str, destination_file_name: str) -> bool:
    # try:
    with open(file_name, "r+b") as f:
        with open(destination_file_name, "w+b") as f_w:
            f_w.write(f.read())
    return True
    # except:
    #     return False


if __name__ == "__main__":
    file_name = 'Screenshot_3.png'
    destination_file_name = 'Screenshot_4.png'
    print(files_copy(file_name, destination_file_name))