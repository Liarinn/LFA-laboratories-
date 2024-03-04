class FiniteAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'}
        self.alph = {'a', 'b', 'c'}
        self.transitions = {
            'q0': {'a': 'q1'},
            'q1': {'b': {'q2', 'q3'}}, # Multiple destinations represented as a set
            'q2': {'c': 'q0'},
            'q3': {'a': 'q4', 'b': 'q0'},
        }
        self.start = {'q0'}
        self.end = {'q4'}

    def convert_to_regular_grammar(self):
        # Convert the finite automaton to a regular grammar
        grammar = {}
        for state in self.states:
            rules = []
            for symbol in self.alph:
                destinations = self.transitions.get(state, {}).get(symbol)
                if destinations:
                    if isinstance(destinations, set):
                        # If there are multiple destinations, generate a rule for each destination
                        for destination in destinations:
                            if destination in self.end:
                                rules.append(symbol)
                            else:
                                rules.append(f"{symbol}{destination}")
                    else:
                        if destinations in self.end:
                            rules.append(symbol)
                        else:
                            rules.append(f"{symbol}{destinations}")
            grammar[state] = rules
        return grammar

    def check_if_deterministic(self):
        # Check if the finite automaton is deterministic
        for transitions in self.transitions.values():
            for destinations in transitions.values():
                if isinstance(destinations, set) and len(destinations) > 1:
                    return False  # Non-deterministic if any symbol leads to more than one state
        return True

f = FiniteAutomaton()
grammar = f.convert_to_regular_grammar()

for state, rules in grammar.items():
    if rules:
        print(f"{state} -> {' | '.join(rules)}")


if(f.check_if_deterministic()):
    print("The FA is deterministic")
else:
    print("The FA is non-deterministic.")

