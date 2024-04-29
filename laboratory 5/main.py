import chomskyNormalForm
if __name__ == '__main__':
    V_n = {"S", "A", "B", "C"}
    V_t = {"a", "d"}
    S = "S"
    P = {
        "S": {"dB", "A"},
        "A": {"d", "dS", "aAdAB"},
        "B": {"epsilon", "aS", "A", "a"},
        "C": {"Aa"}
    }

    # Instance of Grammar Class with uppercase notation of Non-Terminal Terms
    print("\nGenerate Grammar: ")
    variant = chomskyNormalForm.ChomskyNormalForm(V_n, V_t, P, S)

    print("Printing Grammar: ", end="")
    variant.print_variables()

    # Check the Grammar type from Laboratory Work 5
    print("Check Type of Grammar:")
    variant.check_type_grammar()

    CNF_Grammar = variant.convert_to_Chomsky_Normal_Form()