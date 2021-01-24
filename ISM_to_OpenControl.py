'''
ISM_to_OpenControl.py
---------------------
Usage: 
    ISM_to_OpenControl.py
Input: 
    URL to ISM XML file
Output: 
    YAML file of format "ISM_(time)_(date).yaml" 
'''
import requests
import sys
import datetime
from bs4 import BeautifulSoup

#Get the URL
url = sys.argv[1]
r = requests.get(url)
response = requests.get(url)
#Parse the XML
tree = BeautifulSoup(response.content,'lxml-xml')
#Write it out to XML
with open('ISM_{0}.yaml'.format(datetime.datetime.now().strftime('%H%M%S_%d%m%Y')),'w') as f:
    f.write('# australian government ism\n')
    f.write('standards:\n')
    for control in tree.ISM.contents:
        if control != '\n':
            f.write('\t{0}:\n'.format(control.Identifier.contents[0]))
            f.write('\t\trevision: {0}\n'.format(control.Revision.contents[0]))
            f.write('\t\tupdated: {0}\n'.format(control.Updated.contents[0]))
            f.write('\t\tfamily: {0}\n'.format(control.Guideline.contents[0]))
            if control.OFFICIAL.contents[0] == 'Yes':
                f.write('\t\tofficial: {0}\n'.format(True))
            else:
                f.write('\t\tofficial: {0}\n'.format(False))
            if control.PROTECTED.contents[0] == 'Yes':
                f.write('\t\tprotected: {0}\n'.format(True))
            else:
                f.write('\t\tprotected: {0}\n'.format(False))
            if control.SECRET.contents[0] == 'Yes':
                f.write('\t\tsecret: {0}\n'.format(True))
            else:
                f.write('\t\tsecret: {0}\n'.format(False))
            if control.TOP_SECRET.contents[0] == 'Yes':
                f.write('\t\ttop_secret: {0}\n'.format(True))
            else:
                f.write('\t\ttop_secret: {0}\n'.format(False))
            f.write('\t\tname: {0}\n'.format(control.Topic.contents[0]))
            f.write('\t\tdescription: |-\n\t\t{0}\n'.format(control.Description.contents[0]))
