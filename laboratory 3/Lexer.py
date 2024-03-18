import enum


class Token(enum.Enum):
    EOF = -1
    DEF = -2
    EXTERN = -3
    IDENTIFIER = -4
    NUMBER = -5
    OPERATOR = -6

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.pos = 0
        self.current_char = self.input_text[self.pos]
        self.operators = {'+', '-', '*', '/'}

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.input_text):
            self.current_char = None
        else:
            self.current_char = self.input_text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def get_number(self):
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return float(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha() or self.current_char == '_':
                return Token.IDENTIFIER, self.get_identifier()

            if self.current_char.isdigit() or self.current_char == '.':
                return Token.NUMBER, self.get_number()

            if self.current_char in self.operators:
                operator = self.current_char
                self.advance()
                return Token.OPERATOR, operator

            if self.current_char == '#':
                while self.current_char is not None and self.current_char != '\n':
                    self.advance()
                continue

            if self.current_char == '=':
                self.advance()
                return Token.DEF, '='

            if self.current_char == '?':
                self.advance()
                return Token.EXTERN, '?'

            # Skip invalid characters
            self.advance()

        return Token.EOF, None

# Example usage:
text = """
def fib(x)
  if x < 3 then
    1
  else
    fib(x-1)+fib(x-2)

# This expression will compute the 40th number.
fib(40)
"""
lexer = Lexer(text)
while True:
    token, value = lexer.get_next_token()
    if token == Token.EOF:
        break
    print(token, value)
