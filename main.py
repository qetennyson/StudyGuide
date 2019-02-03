# from program_data import study_guide
from datetime import datetime

study_terms = []

# prebuilt_guide = study_guide

def print_header():
    print("**********************************")
    print("Welcome to the Study Guide Program")
    print("**********************************")

def get_guide_file(filename):
    try:
        guide = open(filename, 'r')
    except FileNotFoundError:
        print("That file does not exist.")
    except IOError:
        print("That file may exist, but there was a problem opening it.")
    else:
        guide_data = guide.read()
        return guide_data


def print_guide(guide):
    for term in guide:
        for k, v in term.items():
            print(f'{k}: {v}')

def get_user_search():
    pass

def search_guide():
    pass

def add_entry():
    while True:
        print("Adding an entry: ")
        term = input("What is the term?: ")
        defin = input(f"What is the definition of {term}?: ")
        fund = input(f"What is the fundamental associated with {term}, or leave blank: ")
        added_on = datetime.now().date()
        new_entry = {
            'Term': term,
            'Definition': defin,
            'Fundamentals': fund,
            'added_on': added_on
        }
        print(new_entry)
        cmd = input("Look good? [Y] to confirm, [N] to edit?: ")
        if cmd.lower == 'y':
            break

        return new_entry


def print_entry(term):
    pass

def main():
    print_header()
    user_cmd = input("[A] a study guide entry, [V]iew an existing guide, or E[x]it the program: ")
    if user_cmd.lower() == 'a':
        user_entry = add_entry()
        study_terms.append(user_entry)
        print_guide(study_terms)


    # user_guide_name = input("Enter the name of your study guide, or type 'default' to see the prebuilt guide: ")
    # if user_guide_name != 'default':
    #     guide_data = get_guide_file(user_guide_name)
    # else:
    #     guide_data = get_guide_file(prebuilt_guide)
    #
    # print_guide(guide_data)
    # search_term = get_user_search()
    # search_result = search_guide(search_term)


main()
