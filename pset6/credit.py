def find_card(num):
    if (len(num) == 13 or len(num) == 16) and num[0] == "4":
        return "VISA"
    elif len(num) == 16 and num[0] == "5" and (num[1] == "1" or num[1] == "2" or num[1] == "3" or num[1] == "4" or num[1] == "5"):
        return "MASTERCARD"
    elif len(num) == 15 and num[0] == "3" and (num[1] == "4" or num[1] == "7"):
        return "AMEX"
    else:
        return "INVALID"

# Converts two digit number to one digit number
def convert(num):
    if num > 9:
        a = int(str(num)[0])
        b = int(str(num)[1])
        return a + b
    else:
        return num

def validate(num):
    card = find_card(num)
    if card == "INVALID":
        return "INVALID"
    num_list = []
    for i in range(int(len(num) / 2)):
        index = (i + 1) * -2
        num_list.append(int(num[index]))
        num[index] = "0"
    num_list = [convert(i * 2) for i in num_list]
    numsum = sum([int(i) for i in num if i != ""])
    if str(sum(num_list) + numsum)[-1] == "0":
        return card
    else:
        return "INVALID"

def main():
    num = list(input("Number: "))
    print(validate(num))


if __name__ == "__main__":
    main()

