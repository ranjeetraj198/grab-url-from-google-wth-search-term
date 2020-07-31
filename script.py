try:
    from googlesearch import search
except ImportError:
    print("Oops! module named 'google' not found")

# to search
query = "hindi shayari"
arr = []
for item in search(query, tld="co.in", num=10, start=10, stop=20, pause=2):
    arr.append(item)
    # print(item)

print(arr)



'''
FIRST INSTALL GOOGLESEARCH PACKAGE

query = keyword that you want to search on google
tld = domain extension of search engine, you can use country code like in
        mine case i am from india and i have  used .in at end for better result
num = total number of url that you want to get
start = starting position of url
stop = ending position of url
pause = time break for next url to extract

'''
