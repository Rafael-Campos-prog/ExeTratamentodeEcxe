import urllib.request

try:
    site = urllib.request.urlopen('https://www.jw.org/pt/')
except:
    print('\033[7;31;43mERRO:Talvez a sua internet esteja desligada.\033[m')
else:
    print('\033[0;30;46mEste computador está acessando o site JW.ORG\033[m')
