import scanner


if __name__ == '__main__':
    input_str = input("Podaj wyrażenie: ")
    S = scanner.Scanner()
    tokens = S.scanner(input_str)
    for token in tokens:
        print(token)


