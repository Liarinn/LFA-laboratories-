import random
from finiteAutomaton import FiniteAutomaton

class Grammar:
    def __init__(self):
        # Initialize the grammar variables
        self.S = "S"  # Start symbol
        self.P = {  # Production rules
            "S": ["aB", "bD"],
            "B": ["cD"],
            "D": ["dQ", "a"],
            "Q": ["bD", "dQ"]
        }
        self.Vt = ["a", "b", "c", "d"]  # Terminal symbols
        self.Vn = ["S", "B", "D", "Q"]  # Non-terminal symbols

    def word_generation(self):
        # Generate a word using leftmost derivation
        def leftmost_derivation(string):
            if all(char in self.Vt for char in string):  # If all characters are terminal symbols
                return string
            for i, char in enumerate(string):
                if char in self.Vn:  # If the character is a non-terminal symbol
                    production = random.choice(self.P[char])  # Choose a random production for the symbol
                    new_string = string[:i] + production + string[i + 1:]  # Apply the production
                    return leftmost_derivation(new_string)  # Recursively apply leftmost derivation
            return string

        return leftmost_derivation(self.S)  # Start leftmost derivation from the start symbol

    def to_finite_automaton(self):
        # Convert the grammar to a finite automaton
        alphabet = list(self.Vt)  # Alphabet consists of terminal symbols
        states = list(self.Vn)  # States consist of non-terminal symbols
        states.append("end")  # Add an end state
        start_state = self.S  # Start state is the start symbol
        accept_state = "end"  # Accept state is the end state

        transitions = []
        # Generate transitions for each production rule
        for left_side, right_sides in self.P.items():
            for right_side in right_sides:
                if len(right_side) == 1 and right_side in self.Vt:
                    # If the right side is a terminal symbol, transition to the accept state
                    transitions.append({'src': left_side, 'char': right_side, 'dest': accept_state})
                elif len(right_side) > 1:
                    # If the right side is a sequence of symbols, transition accordingly
                    transitions.append({'src': left_side, 'char': right_side[0], 'dest': right_side[1]})

        return FiniteAutomaton(states, alphabet, transitions, start_state, accept_state)  # Return the finite automaton
