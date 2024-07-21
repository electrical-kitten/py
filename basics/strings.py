# language = '      python '

## remove whitespaces

# strip = language.rstrip()
# strip = language.lstrip()
# strip = language.strip()

# print(strip)

## remove prefixes

url = 'https://nostarch.com'
url_nopre = url.removeprefix('https://')

print(url_nopre)