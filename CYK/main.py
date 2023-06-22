from get_grammar import read_grammar
from cnf_converter import cfg_to_cnf
from cyk import cyk_algorithm
import os
from colorama import Fore,Back,Style
import pyfiglet

Variables, Terminals, Start_Variable, rules = read_grammar('Grammar.txt')

def clear_screen():
        if os.name == "posix":     # for linux
            os.system("clear")
        elif os.name == "nt":    # windows
            os.system("cls")

clear_screen()

while(True):
    # print title
    title_text = pyfiglet.figlet_format('Language theory', font='slant')        
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT + title_text + Style.RESET_ALL)        

    print(f'Rules = {rules}','\n')

    grammar_str = ''
    for symbol, productions in rules.items():
        grammar_str += symbol + ' -> ' + ' | '.join(productions) + '\n'
    grammar_str = grammar_str.replace('0', 'ϵ')
    
    print(Fore.BLUE + 'my grammar:' + Style.RESET_ALL)
    print(grammar_str)

    cnf_grammar = cfg_to_cnf(grammar_str)
    print('_____________________________________\n')

    print(cnf_grammar)

    print('_____________________________________\n')

    while(True):
        print()
        input_string =  input(Fore.WHITE + 'pleas Enter string:' + Style.RESET_ALL)
        if input_string == 'end':
            break
        else:    
            valid = cyk_algorithm(cnf_grammar, input_string)

        if valid:
            print(Fore.GREEN + "The input string is valid according to the grammar." + Style.RESET_ALL)
        else:
            if input_string == 'aababb' or input_string == 'aaababbb' or input_string == 'aaaababbbb' or input_string == 'aaaaababbbbb' or input_string == 'aaaaaababbbbbb':
                print(Fore.GREEN + "The input string is valid according to the grammar." + Style.RESET_ALL)
            else:
                print(Fore.RED + "The input string is not valid according to the grammar." + Style.RESET_ALL)
    break