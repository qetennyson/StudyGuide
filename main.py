def print_header():
    pass

def get_guide_file():
    pass

def print_guide():
    pass

def get_user_search():
    pass

def search_guide():
    pass

def add_entry():
    pass

def delete_entry():
    pass

def print_entry():
    pass

def main():
    print_header()
    guide = get_guide_file()
    print_guide()
    search_term = get_user_search()
    search_result = search_guide(search_term)
    print_entry(search_result)