def get_city_country(city_name, country_name, population=''):

    if population:
        formated_city_country = f"{city_name}, {country_name} - population {population}"
    else:
        formated_city_country = f"{city_name}, {country_name}"

    return formated_city_country.title()