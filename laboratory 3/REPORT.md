THEORY:

The term lexer comes from lexical analysis which, in turn, represents the process of extracting lexical tokens from a string of characters. There are several alternative names for the mechanism called lexer, for example tokenizer or scanner. The lexical analysis is one of the first stages used in a compiler/interpreter when dealing with programming, markup or other types of languages.     The tokens are identified based on some rules of the language and the products that the lexer gives are called lexemes. So basically the lexer is a stream of lexemes. Now in case it is not clear what's the difference between lexemes and tokens, there is a big one. The lexeme is just the byproduct of splitting based on delimiters, for example spaces, but the tokens give names or categories to each lexeme. So the tokens don't retain necessarily the actual value of the lexeme, but rather the type of it and maybe some metadata.

Lexer:
A lexer, short for lexical analyzer, is a fundamental component of a compiler or interpreter that breaks down the input source code into smaller, meaningful units called tokens. These tokens are the building blocks for the subsequent stages of the compilation process. The lexer operates by scanning the input character stream and recognizing patterns defined by a set of rules, typically specified using regular expressions or finite automata. Each token represents a category of lexical element such as keywords, identifiers, literals, and punctuation symbols. By separating the input into tokens, the lexer simplifies the task of parsing and analyzing the source code, enabling further processing by the compiler or interpreter.
The concept of lexical analysis dates back to the early development of programming languages in the 1950s and 1960s. Initially, programmers wrote code directly in machine language, which consisted of binary instructions understood by computers. However, as programming languages evolved to be more human-readable and expressive, the need arose for tools to translate these high-level languages into machine code.

One of the earliest examples of lexical analysis can be found in the development of FORTRAN (Formula Translation) in the late 1950s. The FORTRAN compiler employed a simple lexical analyzer to recognize keywords, identifiers, and literals in the source code. This approach laid the groundwork for subsequent compiler design principles, including the separation of lexical analysis from syntax analysis.

In the 1960s, as programming languages continued to proliferate, researchers and language designers began to formalize the concepts of lexical analysis and develop more sophisticated techniques for tokenizing source code. Donald Knuth's work on lexical scanning algorithms and regular expressions, documented in his seminal book "The Art of Computer Programming," greatly influenced the field.

The development of lex and yacc tools in the 1970s further advanced lexical analysis and parsing. Lex, a lexical analyzer generator, allowed programmers to specify token recognition rules using regular expressions, while yacc (Yet Another Compiler Compiler) provided a framework for generating parsers based on context-free grammars. These tools became foundational in compiler construction and greatly facilitated the development of new programming languages.

Since then, lexical analysis techniques have continued to evolve alongside advancements in compiler theory, programming language design, and automation tools. Modern lexers employ a variety of algorithms and optimizations to efficiently tokenize complex programming languages, making them an essential component of compiler and interpreter implementations across diverse software development domains.


\
OBJECTIVES:

1.Understand what lexical analysis [1] is.
2.Get familiar with the inner workings of a lexer/scanner/tokenizer.
3.Implement a sample lexer and show how it works.


\
IMPLEMENTATION:

This code defines a lexer, a tool commonly used in compilers or interpreters to break down source code into smaller components called tokens. Tokens represent the smallest units of meaning in a programming language. 

The lexer reads through a given input text character by character. It recognizes different types of tokens such as identifiers (names of variables or functions), numbers (integer or floating-point), operators (like '+', '-', '*', '/'), and special tokens like 'DEF' for defining functions and 'EXTERN' for declaring external functions. It skips over whitespace and comments denoted by '#' until a newline character. It also handles some basic syntax like recognizing assignment '=' and question mark '?'. The lexer iterates through the input text, extracting tokens and their corresponding values, and returns them one by one until reaching the end of the input (EOF - End of File). 

 The lexer includes error handling by skipping over invalid characters encountered in the input text. If the lexer encounters a character that does not fit any recognized token category, it simply advances to the next character and continues the tokenization process. This robust error handling ensures that the lexer can gracefully handle unexpected input without crashing, maintaining the integrity of the token stream. By providing a foundation for understanding the structure and meaning of source code, the lexer serves as a fundamental building block in the process of parsing and interpreting programming languages, facilitating the analysis and execution of code by higher-level components such as parsers and interpreters.

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
Enums are used to create symbolic names (members) bound to unique, constant values.

```
class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.pos = 0
        self.current_char = self.input_text[self.pos]
        self.operators = {'+', '-', '*', '/'}

```
The `Lexer` class is responsible for breaking down the input text into tokens.
This class represents the lexical analyzer responsible for tokenizing input text. It has methods to initialize the lexer (__init__), advance to the next character in the input (advance), skip whitespace (skip_whitespace), extract identifiers (get_identifier), extract numbers (get_number), and get the next token (get_next_token).
```
    def advance(self):
        self.pos += 1
        if self.pos >= len(self.input_text):
            self.current_char = None
        else:
            self.current_char = self.input_text[self.pos]

```
The `advance` method moves the lexer position forward by one character in the input text.
This class represents the lexical analyzer responsible for tokenizing input text. It has methods to initialize the lexer (__init__), advance to the next character in the input (advance), skip whitespace (skip_whitespace), extract identifiers (get_identifier), extract numbers (get_number), and get the next token (get_next_token).


The `skip_whitespace` method skips over any whitespace characters (spaces, tabs, newlines) until it encounters a nonwhitespace character.


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
It iterates through the input text character by character, recognizing and returning tokens based on the character's properties. It handles whitespace, identifiers, numbers, operators, comments (lines starting with #), and special tokens like DEF and EXTERN.

\
CONCLUSION:

In conclusion, the lexer implemented here effectively breaks down input text into tokens, facilitating the parsing process in language processing tasks. By categorizing characters into tokens such as identifiers, numbers, operators, and keywords, the lexer lays the foundation for syntactic analysis and subsequent interpretation or compilation. Through methods like `get_next_token`, it systematically iterates through the input text, identifying each token type and extracting relevant information. Additionally, the lexer employs methods like `skip_whitespace` to handle whitespace characters and `advance` to progress through the input text character by character, ensuring thorough and accurate tokenization.

Overall, the lexer plays a crucial role in language processing pipelines, serving as the initial stage in transforming raw text into structured data for further analysis or execution. Its ability to recognize and categorize tokens enables efficient parsing and subsequent semantic analysis, contributing to the development of robust compilers, interpreters, and other language processing tools. With a well-designed lexer like the one made by me, language processing tasks can proceed smoothly, paving the way for the effective implementation of various programming languages and domain-specific languages.


