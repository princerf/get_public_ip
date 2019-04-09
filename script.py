import urllib

url = 'http://icanhazip.com'

myip = urllib.urlopen(url).read()

if __name__ == '__main__':
    print myip
