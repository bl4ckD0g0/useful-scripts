import os.path

folder_path = "C:/Users/myUser/myImages"
files = os.listdir(folder_path)

i = 1
for file_name in files:
    print(file_name)
    if file_name.endswith(".png"):
        new_name = str(i) + ".png"
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))
        i += 1
