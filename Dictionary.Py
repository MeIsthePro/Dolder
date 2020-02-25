# imports
import sys
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
print(sys.version)


# saves

# print(bs)
# bs.find("input", {"name": "override_query"})["value"] = 'Hello'
# print(bs.find("input", {"name": "override_query"})["value"])
# print(html.read())

#####################################################################################################################################################################################4
print("Connecting to server...")
Request("https://www.dictionary.com/")
time.sleep(0)
print("Connected to server")


print("Dictionary V1.2")
print("TO quit, say quit---\n\n\n\n\n\n\n")

while 1:

    word = input("What word would you like to find?  ").strip().lower()

    if word == "quit---":
        print("quitting program...")
        break
        
    try:


        open_ = Request("https://www.dictionary.com/browse/" + word + "?s=ts")

        html = urlopen(open_)

        bs = BeautifulSoup(html.read(), "html.parser")

        defs = bs.find_all("span", {"class": "one-click-content css-1p89gle e1q3nk1v4"})

    except Exception as Handled: 

        print(f"No word found for {word}. Error code 404")
    
        continue
        

    for def_ in reversed(defs):
        print(def_.text)
    print("\n\n\n\n\n")

