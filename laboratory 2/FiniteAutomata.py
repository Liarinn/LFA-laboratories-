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

    def chomsky_hierarchy_classification(self):
        regular = True
        context_free = True
        context_sensitive = True
        for state, rules in self.convert_to_regular_grammar().items():
            for rule in rules:
                # Check if any rule contains more than two symbols or a terminal symbol alone
                if len(rule) > 2 or len(rule) == 1:
                    regular = False
                    context_free = False
                    context_sensitive = False
                    break
                elif len(rule) == 2:
                    if not rule[0].isupper() or not rule[1].isupper():
                        context_free = False
                        context_sensitive = False
                        break
                else:
                    if not rule.isupper():
                        context_sensitive = False
                        break
            if not regular and not context_free and not context_sensitive:
                break

        if context_sensitive:
            return "Type 0 Grammar"
        elif context_free:
            return "Type 1 Grammar"
        elif regular:
            return "Type 3 Grammar"
        else:
            return "Type 2 Grammar"

f = FiniteAutomaton()

grammar = f.convert_to_regular_grammar()
print("Chomsky Hierarchy Classification:", f.chomsky_hierarchy_classification())

for state, rules in grammar.items():
    if rules:
        print(f"{state} -> {' | '.join(rules)}")


if(f.check_if_deterministic()):
    print("The FA is deterministic")
else:
    print("The FA is non-deterministic.")

