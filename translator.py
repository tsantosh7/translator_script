
import os
import subprocess
from subprocess import PIPE

# for aperitum:  Need to install sudo apt-get install apertium and apertium-en-es/ apertium-en-ca

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
            args_translate = ['./trans', '-b', ':es',  '-e', 'apertium', split_line[1]]
            # args_translate = ['./trans', '-b', '-u', 'chrome', ':es', '-e', 'google', split_line[1]]
            # args_translate = ['echo', split_line[1], '|', 'apertium en-ca']
            proc = subprocess.Popen(args_translate, stdout=PIPE, stderr=PIPE)
            proc_output = proc.communicate()
            try:
                stdout_translate = proc_output[0]
                # each_line.replace(split_line[1], stdout_translate.encode('utf-8').decode('utf-8'))
                new_line = split_line[0] + ': ' + stdout_translate.decode('utf-8')
                print(stdout_translate)
                the_file.write(new_line)
            except UnicodeDecodeError as e:
                the_file.write(each_line)
                pass
        else:
            the_file.write(each_line)

