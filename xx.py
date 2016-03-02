import sys
import urllib2
from ntlm import HTTPNtlmAuthHandler

user = sys.argv[-2]
password = sys.argv[-1]
url =  'https://sp13.bemopro.com/xmldirector/_vti_bin/cmis/rest?getRepositories'

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, user, password)
# create the NTLM authentication handler
auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

# create and install the opener
opener = urllib2.build_opener(auth_NTLM)
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
print response.getcode()
print(response.read())
