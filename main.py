from fedora.client.fas2 import AccountSystem
from fedora.client import AuthError

import getpass


print()
userName = input("Enter your Fedora Account UserName >>> ")
password = getpass.getpass("Enter your Fedora Account Password >>> ")

FAS = AccountSystem(username=userName, password=password)

try:
	people = FAS.people_by_key(fields=['username', 'email'])
	for person in people.items():
		if person[1].username == userName:
			print("Your Fedora Email is " + person[1].email)
except:
    print("Error")