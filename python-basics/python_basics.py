store_address = ["Flat Street", "99", "Lisbon"]
pins = {"Nick":9048, "Laurie":5428}

print(store_address[0], store_address[1])
pin = int(input("Enter your pin: "))

def find_fruit_in_list(fruit):
    myfile = open('sample.txt')
    fruits = myfile.read().splitlines()
    if fruit in fruits:
        return "That fruit is in the list"
    else:
        return "That fruit isn't in the list..."

if pin in pins.values():
    fruit = input("Enter a fruit here: ")
    print(find_fruit_in_list(fruit))
else:
    print("Incorrect pin!")
    print("This info can only be accessed by:")
    for key in pins.keys():
        print(key)

