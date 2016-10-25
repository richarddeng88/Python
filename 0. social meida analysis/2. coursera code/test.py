import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')] ## i think this is http header that send out to twitter.

keyword = 'obama'
link = 'https://twitter.com/search/realtime?q='
source_code = opener.open(link + keyword+ '&src=hash&lang=en').read()
print type(source_code)
#print source_code
split = re.findall(r'<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>',source_code)
print type(split)
print split[0],'\n',split[1]