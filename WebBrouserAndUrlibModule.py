#WebBrowserModule And UrlibMODule

import webbrouser
import urlib

#for Webbrouser
webbrouser.open("linkname.com")

#for Urlib
p = urlib.requst.urlopen("linkname.com")
print(p)
#Checking Https Status in urlib
t = p.getcode()
