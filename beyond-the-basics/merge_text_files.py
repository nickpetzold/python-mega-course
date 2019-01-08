from datetime import datetime
import glob2

now_string = datetime.now().strftime('%Y-%m-%d-%H-%M-%s')
print(now_string)
files = sorted(glob2.glob('*.txt'))

with open(f'{now_string}.txt', 'a+') as my_text_file:
    for file in files:
        with open(file) as individual_file:
            content = individual_file.read()
            my_text_file.write(content + '\n')


