import sys
from cmislib import CmisClient

username, password = sys.argv[-2:]
client = CmisClient('https://sp13.bemopro.com/xmldirector/_vti_bin/cmis/rest?getRepositories', username, password)
print client.defaultRepository
