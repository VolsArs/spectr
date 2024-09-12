def create_file():
    file_handler = open("binary_file.bin", "wb")
    file_handler.write(b"  \n")
    file_handler.close()


def count_simbols() -> int:
    file_handler = open("binary_file.bin", "rb")
    data_byte = file_handler.read(1)
    simbols = 0
    while data_byte:
        data_byte = file_handler.read(1)
        simbols += 1
    file_handler.close()
    return simbols


def count_words() -> int:
    file_handler = open("binary_file.bin", "rb")
    data_byte = file_handler.read()
    text = data_byte.decode()
    text.strip()
    words = text.split()
    num_words = len(words)
    return num_words


def count_lines() -> int:
    file_handler = open("binary_file.bin", "rb")
    data_byte = file_handler.read()
    text = data_byte.decode()
    lines = text.count('\n')
    return lines


if __name__ == '__main__':
    create_file()
    print(count_simbols())
    print(count_words())
    print(count_lines())