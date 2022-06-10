import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[1:31mO site não está funcionando.\033[m')
else:
    print('O site está funcionando')
