from functions import choose_file, os


number_of_lines = 0
is_folder = False


while True:
    path = input("Enter the path to be scanned or quit: ")
    if path == "quit":
        break
    else:
        print(os.path.basename(path))
        choose_file(path, number_of_lines, is_folder)
