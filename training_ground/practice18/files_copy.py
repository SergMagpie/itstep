import os
# Finding a directory with a script.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# Create an absolute path to the file.


def files_copy(file_name: str, destination_file_name: str) -> bool:
    try:
        with open(file_name, "r") as f:
            with open(destination_file_name, "w") as f_w:
                for i in f:
                    f_w.write(i)
        return True
    except:
        return False


if __name__ == "__main__":
    file_name = 'next_generation.txt'
    destination_file_name = 'new_generation.txt'
    print(files_copy(file_name, destination_file_name))