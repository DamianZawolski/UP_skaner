import turtle
from PIL import Image

def draw_filled_rectangle(width):
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(140)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(4)


def draw_binary_barcode(binary_string, kod):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-200, 70)

    for digit in binary_string:
        if digit == '0':
            turtle.color("white")
            draw_filled_rectangle(4)
        elif digit == '1':
            turtle.color("black")
            draw_filled_rectangle(4)

    turtle.forward(100)
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file=f"wlasny_kod_{kod}.eps")
    turtle.done()


def control_digit(kod_12):
    checksum = 0
    counter = 0
    kod_int = int(kod_12)
    while kod_int > 0:
        last_digit = int(kod_int % 10)
        if counter % 2 == 0:
            checksum += last_digit * 3
        else:
            checksum += last_digit
        counter += 1
        kod_int /= 10
    return str((10 - (checksum % 10)) % 10)


def encode_to_ean13(int_number):
    number = str(int_number)
    o = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    e = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
    r = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
    parity = [[1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1],
              [1, 0, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0],
              [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1]]

    binary_code = "101"
    first = int(number[0])

    # left
    for i in range(1, 7):
        if parity[first][i - 1] == 1:
            binary_code += o[int(number[i])]
        else:
            binary_code += e[int(number[i])]

    # separator
    binary_code += "01010"

    # right
    for i in range(8, 14):
        binary_code += r[int(number[i - 1])]

    # separator
    binary_code += "101"

    return binary_code


def wygeneruj_kod_EAN(kod):
    kod += control_digit(kod)
    binary_code = encode_to_ean13(kod)
    # print(encode_to_ean13("0987654321562"))
    turtle.setup(600, 500)
    draw_binary_barcode(binary_code, kod)

    #     2o      3o      4e      5o      1e      2e           3e        4r      5r      1r      2r      3r
    # 101 0010011 0111101 0011101 0110001 0110011 0011011 0101       0100001 0 1011100 1001110 1100110 1101100 1000010 101 1234512345123
    # 101 0010011 0111101 0011101 0110001 0110011 0011011 0101       0100001 0 1011100 1001110 1100110 1101100 1000010 101
