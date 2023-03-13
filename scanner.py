from Token import Token


class Scanner:
    possible_tokens: list[Token] = ['(', ')', '+', '-', '*', '/']

    def scanner(self, input_string: str) -> list[Token]:
        outcome = []
        id = 0
        position = 0
        input_string = input_string.replace(' ', '')
        while len(input_string) > 0:
            token = self.scan(input_string, id, position)
            position += len(token.value)
            outcome.append(token)
            input_string = input_string[len(token.value):]
            id += 1
        return outcome

    def scan(self, input_string: str, id: int, position: int) -> Token:
        if input_string[0] in self.possible_tokens:
            return Token(id, input_string[0])
        if input_string[0].isnumeric():
            var = ''
            while len(input_string) > 0 and input_string[0].isnumeric():
                var += input_string[0]
                input_string = input_string[1:]
            return Token(id, var)
        else:
            raise Exception(f'Unexpected character: {input_string[0]} at position {position}')

