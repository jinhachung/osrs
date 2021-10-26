import os
import requests
from datetime import date

def find_starting_integer_in_string(chunk):
    digit = 0
    for letter in chunk:
        if letter.isnumeric():
            digit += 1
        else:
            break
    if not chunk[0].isnumeric():
        return 0
    return int(chunk[0:digit])

def main():
    # get date
    today = date.today()
    print("Downloading request items' information on: {}".format(today))

    # make directory for date
    #path = os.path.join(os.getcwd(), str(today))
    #os.mkdir(path)

    # get items to search
    #items = ["ghrazi_rapier", "sanguinesti_staff#Uncharged"]
    f = open("items_of_interest.txt", "r")
    items = [line.strip() for line in f.readlines()]
    f.close()

    # download item info
    for item in items:
        # get link / url
        url = "https://oldschool.runescape.wiki/w/{}".format(item)
        r = requests.get(url, allow_redirects=True)

        # save content with name
        #open("{}/{}.info".format(path, item), "wb").write(r.content)
        temp = open(str(today), "wb")
        temp.write(r.content)
        temp.close()
        temp = open(str(today), "r")
        value = 1000
        for line in temp.readlines():
            if "data-val-each=" in line:
                chunks = line.split("data-val-each=\"")
                for chunk in chunks[1:]:
                    value = find_starting_integer_in_string(chunk)
                    if value != 0:
                        break
                if value != 0:
                    break
        print("{} is worth {:,}gp".format(item, value))
        temp.close()
    os.remove(str(today))

if __name__ == "__main__":
    main()
