from city_functions import get_city_country

def test_city_country():
    formated_city_country_string = get_city_country('santiago', 'chilie')
    assert formated_city_country_string == 'Santiago, Chilie'

