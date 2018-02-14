from restcountries import RestCountryApiV2 as rc
countries_list = rc.get_all();

for c in countries_list:
    print (c.name,"-",c.capital,"-",end="")

    for curr in c.currencies:
        code, name, symbol = curr.items()
        print(code, name, symbol, end="")
    print()