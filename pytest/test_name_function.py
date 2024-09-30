from name_function import get_fromatted_name

def test_first_last_name():
    ## do names like John Doe work?
    formatted_name = get_fromatted_name('john', 'doe')
    assert formatted_name == 'John Doe'

def test_first_last_middle_name():
    formatted_name = get_fromatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'



    