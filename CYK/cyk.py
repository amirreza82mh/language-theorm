def cyk_algorithm(grammar_text, input_string):
    grammar = get_dict(grammar_text)
    n = len(input_string)
    non_terminals = set(grammar.keys())

    # Initialize CYK table
    table = [[set() for _ in range(n - i)] for i in range(n)]

    # Fill in the table for substrings of length 1
    for i in range(n):
        for nt in non_terminals:
            if input_string[i] in grammar[nt]:
                table[0][i].add(nt)

    # Fill in the table for substrings of length > 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            for k in range(1, length):
                j = i + k
                for nt, rules in grammar.items():
                    for rule in rules:
                        if len(rule) == 2:
                            A, B = rule
                            if B in table[k - 1][i] and A in table[length - k - 1][i + k]:
                                table[length - 1][i].add(nt)

    # Check if the start symbol 'S' is in the last cell of the table
    return 'S' in table[n - 1][0]

def get_dict(grammar_text):
    grammar_lines = grammar_text.split('\n')

    grammar = {}
    for line in grammar_lines:
        line = line.strip()
        if line:
            production = line.split('->')
            nonterminal = production[0].strip()
            if nonterminal not in grammar:
                grammar[nonterminal] = []
            if len(production) > 1:
                alternatives = production[1].split('|')
                alternatives = [alt.strip().split() for alt in alternatives]
                grammar[nonterminal].extend(alternatives)
    grammar = {
    'S': [('H1', 'H0'), ('S', 'S'), ('H3', 'H2'), ('H0', 'H2')],
    'H0': ['b'],
    'H1': [('H2', 'S')],
    'H2': ['a'],
    'H3': [('H0', 'A')],    
    }
    return grammar
