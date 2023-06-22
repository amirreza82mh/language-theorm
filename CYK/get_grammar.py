def read_grammar(filename):
    with open('grammar.txt', 'r') as f:
        lines = f.readlines()
    Variables = lines[0].strip().split(': ')[1].split(', ')
    Terminals = lines[1].strip().split(': ')[1].split(', ')
    Start_Variable = lines[2].strip().split(': ')[1]
    rules = {}
    for line in lines[4:]:
        lhs, rhs = line.strip().split(', ')
        if lhs not in rules:
            rules[lhs] = []
        rules[lhs].append(rhs)
    return Variables, Terminals, Start_Variable, rules