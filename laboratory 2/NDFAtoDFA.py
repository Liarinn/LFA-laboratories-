class NDFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alph = {'a', 'b', 'c'}
        self.transitions = {
            'q0': {'a': {'q1'}},
            'q1': {'b': {'q2', 'q3'}}, 
            'q2': {'c': {'q0'}},
            'q3': {'a': {'q4'}, 'b': {'q0'}},
            'q4': {}
        }
        self.start_state = 'q0'
        self.end_state = {'q4'}


class DFA:
    def __init__(self):
        self.states = set()
        self.alph = set()
        self.transitions = {}
        self.start_state = None
        self.end_state = set()

    def transformation(self, ndfa):
        self.alph = ndfa.alph
        unprocessed_states = [frozenset([ndfa.start_state])]
        self.start_state = frozenset([ndfa.start_state])

        while unprocessed_states:
            current_state = unprocessed_states.pop()
            if current_state not in self.states:
                self.states.add(current_state)
                for input_symbol in ndfa.alph:
                    next_state = frozenset(
                        [s for state in current_state for s in ndfa.transitions.get(state, {}).get(input_symbol, [])])
                    if next_state:
                        self.transitions[current_state, input_symbol] = next_state
                        unprocessed_states.append(next_state)

        self.end_state = {state for state in self.states if ndfa.end_state.intersection(state)}

    def results(self):
        # Convert frozenset to set for printing
        states = {tuple(state) for state in self.states}
        transitions = {((tuple(state), input_symbol), tuple(next_state)) for (state, input_symbol), next_state in
                       self.transitions.items()}
        start_state = tuple(self.start_state)
        end_state = {tuple(state) for state in self.end_state}

        print("\nDFA")
        print("States:", states)
        print("Transitions")
        for (state, input_symbol), next_state in transitions:
            print(f"{state} --({input_symbol})--> {next_state}")
        print("Start State:", start_state)
        print("End State:", end_state)


ndfa = NDFA()
dfa = DFA()
dfa.transformation(ndfa)
dfa.results()

