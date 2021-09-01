import os

separator = os.sep


def choose_file(dir_path, number_of_lines, is_folder_var):
    number_of_lines += 1
    for name in os.listdir(dir_path):
        if is_folder_var:
            if os.listdir(dir_path)[-1] == name:
                print(("  |" * (number_of_lines-1)) + " -" + name)
            else:
                print(("  |" * (number_of_lines-1)) + "  |-" + name)
        else:
            if os.listdir(dir_path)[-1] == name:
                print("  -" + name)
            else:
                print("  |-" + name)
        if os.path.isdir(dir_path+separator+name):
            is_folder = True
            choose_file(dir_path+separator+name, number_of_lines, is_folder)
