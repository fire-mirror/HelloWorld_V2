def ascii(ascii_list):
    string = ""
    for code in ascii_list:
        string += chr(code)
    return string


hello_world_ascii = [72, 101, 108, 108, 111, 87, 111, 114, 108, 100]
print(ascii(hello_world_ascii))
