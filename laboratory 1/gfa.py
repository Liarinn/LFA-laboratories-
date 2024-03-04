from grammar import Grammar

grammar = Grammar()

fa = grammar.to_finite_automaton()

tt = ["ba", "aba", "aca", "terra", "acddbdddbdddbdba", "ba", "baba"]
i=0
print("Generated strings based on the language:")
for i in range(5):
    print(i+1, "  ", grammar.word_generation())
print("")
for s in tt:
    print(f"String '{s}':    {fa.accepted_states(s)}")
