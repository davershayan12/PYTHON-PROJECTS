'''4.	Write a user-defined function called describe_city() that accepts the name of a cityand its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.'''
def describe_city(city,country='Pakistan'):
    print(f'{city} is in {country}')

describe_city('karachi')
describe_city('lahore') 
describe_city('Sydney')   