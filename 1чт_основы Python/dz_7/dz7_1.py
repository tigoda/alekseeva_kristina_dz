import os


with open('dz_7.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if i == 1:
            dir_name = line
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
                for i, line2 in enumerate(f, 1):
                    dir_path = os.path.join(dir_name, line2)
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)





