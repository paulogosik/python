import urllib.request


def verifyWebSite(site):
    try:
        urllib.request.urlopen(site)
    except Exception as e:
        print(f'\033[31mThis website is inaccessible right now.\nError: {e}\033[m')
    else:
        print(f"\033[32mThis website is working normally.\033[m")


verifyWebSite('https://www.pudim.com.br')
