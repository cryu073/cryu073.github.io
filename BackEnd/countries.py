import requests


def get_country():
    r = requests.request(method="GET",
                         #params={'name': name},
                         url='https://restcountries.com/v3.1/all'
                         )
    return r


r = get_country()
print(r.text)


