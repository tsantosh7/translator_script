
import os
import subprocess
from subprocess import PIPE


current_dir = os.getcwd()+'/'
file_to_convert = 'English.txt'


with open(current_dir+file_to_convert) as f:
    all_lines = f.readlines()

with open('Spanish.txt', 'a') as the_file:
    for each_line in all_lines:
        # print(each_line.strip())

        if "'" in each_line:
            split_line = each_line.split(':')
            print(split_line[1])
            args_translate = ['./trans', '-no-auto', '-b', ':es', split_line[1]]
            proc = subprocess.Popen(args_translate, stdout=PIPE, stderr=PIPE)
            proc_output = proc.communicate()
            try:
                stdout_translate = str(proc_output[0], 'utf-8')
                each_line.replace(split_line[1], stdout_translate)
                the_file.write(each_line)
            except UnicodeDecodeError as e:
                the_file.write(each_line)
                pass
        else:
            the_file.write(each_line)

