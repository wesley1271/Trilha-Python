# Formata automaticamente as cidades e o país unindo as duas strings recebidas (Title Case).
def city_country(city,country):
    """Exibe sua cidade e país"""
    cityCountry = f"{city}, {country}"
    return cityCountry.title()
cidadepaís = city_country('mogi', 'brasil') 
print(f"{cidadepaís}")
cidadepaís = city_country('braz cubas', 'brasil') 
print(f"{cidadepaís}")
cidadepaís = city_country('sao miguel', 'brasil') 
print(f"{cidadepaís}")

