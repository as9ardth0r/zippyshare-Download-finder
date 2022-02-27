import urllib.request

with open('zippyshare.txt','r') as csvfile:
  for row in csvfile.readlines():
        with urllib.request.urlopen(row) as response:
            texte = response.read()
        if ("File does not exist on this server" in str(texte)):
            print(row)
        else:
            pass