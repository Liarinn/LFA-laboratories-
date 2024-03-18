THEORY:

The term lexer comes from lexical analysis which, in turn, represents the process of extracting lexical tokens from a string of characters. There are several alternative names for the mechanism called lexer, for example tokenizer or scanner. The lexical analysis is one of the first stages used in a compiler/interpreter when dealing with programming, markup or other types of languages.     The tokens are identified based on some rules of the language and the products that the lexer gives are called lexemes. So basically the lexer is a stream of lexemes. Now in case it is not clear what's the difference between lexemes and tokens, there is a big one. The lexeme is just the byproduct of splitting based on delimiters, for example spaces, but the tokens give names or categories to each lexeme. So the tokens don't retain necessarily the actual value of the lexeme, but rather the type of it and maybe some metadata.


OBJECTIVES:

1.Understand what lexical analysis [1] is.
2.Get familiar with the inner workings of a lexer/scanner/tokenizer.
3.Implement a sample lexer and show how it works.

IMPLEMENTATION:

```
class Token(enum.Enum):
    EOF = -1
    DEF = -2
    EXTERN = -3
    IDENTIFIER = -4
    NUMBER = -5
    OPERATOR = -6
```
This enum defines the different types of tokens that the lexer can recognize. Each token type is represented by an integer value.

```
class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.pos = 0
        self.current_char = self.input_text[self.pos]
        self.operators = {'+', '-', '*', '/'}

```
The `Lexer` class is responsible for breaking down the input text into tokens.

```
    def advance(self):
        self.pos += 1
        if self.pos >= len(self.input_text):
            self.current_char = None
        else:
            self.current_char = self.input_text[self.pos]

```
The `advance` method moves the lexer position forward by one character in the input text.
```
def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

```
The `skip_whitespace` method skips over any whitespace characters (spaces, tabs, newlines) until it encounters a nonwhitespace character.
```
    def get_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result
```

This method extracts an identifier token from the input text. It starts reading characters from the current position until it encounters a nonalphanumeric character or an underscore.
```
    def get_number(self):
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return float(result)
       
```
This method extracts a numeric token from the input text. It starts reading characters from the current position until it encounters a nondigit character or a period (for floatingpoint numbers).


```
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha() or self.current_char == '_':
                return Token.IDENTIFIER, self.get_identifier()

```
This method is the main function of the lexer. It iterates over the input text character by character, identifying and extracting tokens. It first skips over any whitespace.
Then, it checks if the current character represents an identifier, a number, a comment, or an operator. If it encounters an unknown character, it simply skips over it.
Finally, it returns the next token found in the input text.



