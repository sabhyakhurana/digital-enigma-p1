import random

websites = [
    "http://www.randomwebsite1.com",
    "http://www.randomwebsite2.net",
    "http://www.randomwebsite3.org",
    "http://www.randomwebsite4.info",
    "http://www.randomwebsite5.co",
    "http://www.randomwebsite6.io",
    "http://www.randomwebsite7.biz",
    "http://www.randomwebsite8.us",
    "http://www.randomwebsite9.eu",
    "http://www.randomwebsite10.me",
    "http://www.randomwebsite11.online",
    "http://www.randomwebsite12.website",
    "http://www.randomwebsite13.space",
    "http://www.randomwebsite14.tv",
    "http://www.randomwebsite15.xyz",
    "http://www.randomwebsite16.blog",
    "http://www.randomwebsite17.news",
    "http://www.randomwebsite18.tech",
    "http://www.randomwebsite19.store",
    "http://www.randomwebsite20.shop",
    "http://www.randomwebsite21.design",
    "http://www.randomwebsite22.app",
    "http://www.randomwebsite23.dev",
    "http://www.randomwebsite24.co.uk",
    "http://www.randomwebsite25.ca",
    "http://www.randomwebsite26.au",
    "http://www.randomwebsite27.de",
    "http://www.randomwebsite28.fr",
    "http://www.randomwebsite29.es",
    "http://www.randomwebsite30.it",
    "http://www.randomwebsite31.br",
    "http://www.randomwebsite32.jp",
    "http://www.randomwebsite33.cn",
    "http://www.randomwebsite34.ru",
    "http://www.randomwebsite35.kr",
    "http://www.randomwebsite36.in",
    "http://www.randomwebsite37.mx",
    "http://www.randomwebsite38.ar",
    "http://www.randomwebsite39.id",
    "http://www.randomwebsite40.tr",
    "http://www.randomwebsite41.pl",
    "http://www.randomwebsite42.nl",
    "http://www.randomwebsite43.se",
    "http://www.randomwebsite44.ch",
    "http://www.randomwebsite45.at",
    "http://www.randomwebsite46.no",
    "http://www.randomwebsite47.dk",
    "http://www.randomwebsite48.fi",
    "http://www.randomwebsite49.be",
    "http://www.randomwebsite50.pt"
]

source_websites = [
    "http://www.randomsource1.com",
    "http://www.randomsource2.net",
    "http://www.randomsource3.tv",
    "http://www.randomsource4.gov",
    "http://www.randomsource5.org",
    "http://www.randomsource6.io",
    "http://www.randomsource7.md",
    "http://www.randomsource8.nic",
    "http://www.randomsource9.in",
    "http://www.randomsource10.be"
]

for i in range (0,5):
    with open("data"+str(i+1)+".txt", 'w') as file:
        random_number = random.randint(200, 401)
        for j in range(1, random_number):
            websites_to_print = random.randint(3,10)
            random_elements = random.sample(websites, websites_to_print)
            concatenated_string = " ".join(random_elements)
            print(str(j)+". The source " + random.choice(source_websites)+ " gives the following links originating from the website "+ random.choice(websites) +" : "+ concatenated_string, file = file)
