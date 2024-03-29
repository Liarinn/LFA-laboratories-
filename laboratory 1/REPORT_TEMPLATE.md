Theory:

------

|||Background Theory|||

As a crucial foundation for our project, we delve into the fundamental concepts of formal languages, 
grammars, and finite automata. These concepts are essential in understanding the underlying structure 
and functionality of our language processing system.

|||Formal Languages|||

Formal languages serve as the backbone of communication systems, providing a structured framework for conveying information. At their core, formal languages consist of three key components:

- Alphabet: This represents the set of valid characters or symbols that form the building blocks of our language.

- Vocabulary: The vocabulary encompasses the collection of valid words or strings that can be constructed using symbols from the alphabet.

- Grammar: Grammars define the rules and constraints governing the formation of valid strings within the language. These rules dictate how symbols from the alphabet can be combined to generate meaningful expressions.

|||Grammars|||

Grammars play a pivotal role in shaping the structure of formal languages by providing a systematic method for string generation. Our project focuses on implementing grammars, which comprise several essential elements:

- Terminals: These are symbols drawn from the alphabet, representing the basic units of our language.

- Non-terminals: Non-terminal symbols serve as placeholders for sequences of terminals and other non-terminals, allowing for recursive definition of language constructs.

- Production Rules: Production rules define the transformation of non-terminal symbols into sequences of terminals and non-terminals. These rules form the backbone of our grammar, guiding the generation of valid strings within the language.

|||Finite Automata|||

Finite automata serve as computational models capable of recognizing patterns within input sequences. This theoretical framework is integral to our project, offering insights into the computational complexity of language processing tasks. Key components of finite automata include:

- States: These represent distinct configurations or states of the automaton during computation.

- Transitions: Transitions define the movement of the automaton from one state to another in response to input symbols.

- Accept States: Accept states designate the final states of the automaton, indicating successful recognition of input strings.

|||Project Implementation|||

Armed with a solid understanding of formal languages, grammars, and finite automata, we embark on the implementation of our language processing system. By leveraging these theoretical concepts, we aim to build a robust framework capable of generating valid strings and performing language recognition tasks.

------------------------

Objectives:

a. Implement a type/class for your grammar;

b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;

c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;

d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;

------------------------

Results:

ba

bddddba

acdddbddbdbdbdbddba

acddbdba

aca

String 'error':    False

String 'ba':    True

String 'aca':    True

String 'abbddba':    False

![img_1.png](img_1.png)

------------------------

Conclusions:

In this laboratory, I immersed myself in the realms of formal languages and automata 
theory, gaining insights into finite automata and grammars. Exploring conversion methods and implementation techniques 
in Python, I solidified my understanding of these fundamental concepts. 
Through practical exercises, I deepened my understanding of underlying algorithms and 
gained flexibility in designing classes and methods for representing grammars and 
automata. Armed with this knowledge, I am better prepared for further exploration into advanced topics in formal language theory.