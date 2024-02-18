class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        # Initialize the Finite Automaton
        self.states = states  # Set of states
        self.alphabet = alphabet  # Alphabet
        self.transitions = transitions  # Transition function
        self.start_state = start_state  # Start state
        self.accept_states = accept_states  # Accept states

    def accepted_states(self, input_string):
        # Check if the input string is accepted by the automaton
        current_states = {self.start_state}  # Set current states to start state
        for char in input_string:
            input_symbol = str(char)
            next_states = self.find_next_states(current_states, input_symbol)  # Find next states for each current state
            if not next_states:
                return False  # If there are no next states, reject the input
            current_states = next_states  # Update current states to next states
        return any(state in self.accept_states for state in current_states)  # Check if any current state is an accept state

    def find_next_states(self, current_states, input_symbol):
        # Find the next states given the current states and input symbol
        next_states = set()
        for state in current_states:
            next_states.update(self.find_transitions(state, input_symbol))  # Find transitions for each current state
        return next_states  # Return the set of next states

    def find_transitions(self, current_state, input_symbol):
        # Find transitions for a given current state and input symbol
        return {transition['dest'] for transition in self.transitions
                if transition['src'] == current_state and transition['char'] == input_symbol}  # Return the set of destination states for matching transitions
