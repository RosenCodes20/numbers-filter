number_of_lines = int(input())
list = []

final_list = []

for line in range(number_of_lines):
    number = int(input())

    list.append(number)

command = input()

if command == "even":
    for num in list:
        if num % 2 == 0:
            final_list.append(num)

elif command == "odd":
    for num in list:
        if num % 2 != 0:
            final_list.append(num)

elif command == "negative":
    for num in list:
        if num < 0:
            final_list.append(num)

else:
    for num in list:
        if num >= 0:
            final_list.append(num)

print(final_list)
