import os
path="./save_img/person.jpg"
is_file = os.path.isfile(path)
if is_file:
    print(f"{path} is a file.")
else:
    pass