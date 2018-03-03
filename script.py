import webbrowser
import urllib2
import re
import detectlanguage

detectlanguage.configuration.api_key = "098dcb3d19d786ca1bdb9f6a48e990d7"

def filter_sub (x):
    x = re.sub(" \[New Entry\]", "",  x)
    x = re.sub(" \[New", "",  x)
    return x

website = "http://vitanclub.us"
url = website + "/cauta/kiss-fm.html"
# webbrowser.open("http://vitanclub.us/cauta/kiss-fm.html")

html = urllib2.urlopen(url)
response = html.read()

links = [x.split('\'')[1] for x in response.split() if "Fresh" in x and "href" in x]


def get_link(link):
    url = website + link
    html = urllib2.urlopen(url)
    response = html.read().split('\n')
    idx_list = [idx + 1 for idx, x in enumerate(response) if 'br/' in x]
    entries = [response[x][4:-6] for x in idx_list[1:-1]]
    entries_filt = map(filter_sub, entries)
    return entries_filt

get_link(links[25])

# import langdetect
# print langdetect.detect('War and Peace')
# print langdetect.detect('Le-am spus si fetelor')
# print langdetect.detect_langs('Yalla')

# # use detectlanguage, better
# print detectlanguage.detect('War and Peace')
# print detectlanguage.detect('Le-am spus si fetelor')
# print detectlanguage.detect('Yalla')
# print detectlanguage.detect("Buenos dias señor")






text_file = open("Output.txt", "w")
text_file.write(response)
text_file.close()
