from city_functions import get_city_country

def test_city_country():
    city_country_string = get_city_country('santiago', 'chilie')
    assert city_country_string == 'Santiago, Chilie'

def test_city_country_population():
    city_country_population_string = get_city_country('santiago', 'chilie', 5000000) 
    assert city_country_population_string == 'Santiago, Chilie - Population 5000000'