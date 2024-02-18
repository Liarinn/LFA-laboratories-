from grammar import Grammar

grammar = Grammar()

fa = grammar.to_finite_automaton()

tt = ["aba", "aca", "terra", "acddbdddbdddbdba"]
i=0
print("Generated strings based on the language:")
for i in range(5):
    print(grammar.word_generation())
print("")
for s in tt:
    print(f"String '{s}':    {fa.accepted_states(s)}")
