import os

# The built-in JSON library let's us write Python dictionaries directly to JSON objects in external files.
# The other option is to use the Pickle library.
import json

import sys

from datetime import datetime

guide_count = 0
study_terms = []

def print_header():
    print("**********************************")
    print("Welcome to the Study Guide Program")
    print("**********************************")

def read_guide(filename):
    pass

#TODO: Handle JSON filetype when reading JSON files.
def print_guide(guide):

    '''
    :param guide: A LIST of DICTIONARIES containing terms.
    :return:
    '''
    for term in guide:
        for k, v in term.items():
            print(f'{k}: {v}')

def check_filename(filename='study_guide'):
    '''

    :param filename: DEFAULT argument of 'study_guide'
    :return: Returns either the 'study_guide' filename, or 'study_guide_X' where X is the number of guides that
    have been saved thus far
    '''
    if os.path.exists(filename):
        global guide_count
        filename = f'{filename}_{guide_count}'

        guide_count += 1

        return filename
    else:
        return filename

def write_guide(filename, guide):
    with open(f'{filename}.txt', 'w') as f:
        f.write(json.dumps(guide))

def add_entry():
    '''
    :return: Returns a DICTIONARY representing some programming term.
    '''
    while True:
        print("Adding an entry: \n")
        term = input("What is the term?: ")
        defin = input(f"What is the definition of {term}?: ")
        fund = input(f"What is the fundamental associated with {term}, or leave blank: ")
        added_on = datetime.now()
        new_entry = {
            'Term': term,
            'Definition': defin,
            'Fundamentals': fund,
            # We use strftime() here, because JSON can't write regular datetime objects.  It needs a string.
            'added_on': datetime.strftime(added_on, '%B %d, %Y')
        }
        print_entry(new_entry)
        cmd = input("\nLook good? [Y] to confirm, [N] to edit: ")
        if cmd.lower == 'y':
            break

    return new_entry


def print_entry(term):
    '''
    :param term: A single term in a DICTIONARY.
    :return:
    '''
    for k, v in term.items():
        print(f'{k}: {v}')
    print()

#TODO: Implement search by term.
def search_guide():
    pass

def main():
    print_header()
    while True:
        user_cmd = input("\n[A]dd study guide entry \n[S]ave the current guide \n[V]iew an existing guide \n"
                         "or E[x]it the Program: ")

        if user_cmd.lower() == 'a':
            user_entry = add_entry()
            study_terms.append(user_entry)

            print("The currently active guide is: ")
            print_guide(study_terms)

        elif user_cmd.lower() == 's':
            correct_filename = check_filename()
            write_guide(correct_filename, study_terms)

        elif user_cmd.lower() == 'v':
            user_guide_filename = input("What is the filename of the guide you are trying to view?: ")
            user_guide = read_guide(user_guide_filename)
            print_guide(user_guide)

        elif user_cmd.lower() == 'x':
            sys.exit()



        #TODO: View existing guides
        #TODO: Update existing guides
        #TODO: Search for a term


main()
