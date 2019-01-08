my_file = open('sample.txt')
fruits = my_file.read().splitlines()
my_file.close()
for fruit in fruits:
    print(len(fruit))

