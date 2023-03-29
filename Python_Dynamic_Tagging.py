import requests
import base64
import xml.dom.minidom

#Create tag
username = "<your username>"
password = "<your password>"
def getToken(USERNAME,PASSWORD):
    AuthStringRaw = USERNAME+":"+PASSWORD
    base64_bytes = AuthStringRaw.encode("ascii")
    authtoken = base64.b64encode(base64_bytes)
    base64_authtoken = authtoken.decode("ascii")
    return base64_authtoken

token = getToken(username,password)
network_range = "192.168.102.0/24"

#Please note this URL points to the AU pod 
url = "https://qualysapi.qg1.apps.qualys.com.au/qps/rest/2.0/create/am/tag"
#network_range = "192.168.101.0/24"
tagTextName = "My-Third-Tag"
auth_token = token
payload = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?><ServiceRequest><data><Tag><name>"+tagTextName+"</name><ruleType>NETWORK_RANGE</ruleType><ruleText>"+network_range+"</ruleText></Tag></data></ServiceRequest>"
headers = {
  'Content-Type': 'text/xml',
  'X-Requested-With': 'QualysPostman',
  'Authorization': 'Basic ' + token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#Edit Tag 
TagID = "9431186"

url = "https://qualysapi.qg1.apps.qualys.com.au/qps/rest/2.0/update/am/tag"+"/"+TagID

tagTextName = "My-Third-Tag-updated"
network_range = "192.168.107.0/24"
payload = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?><ServiceRequest><data><Tag><name>"+tagTextName+"</name><ruleType>NETWORK_RANGE</ruleType><ruleText>"+network_range+"</ruleText></Tag></data></ServiceRequest>"
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)