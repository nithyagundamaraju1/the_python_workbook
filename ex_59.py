import re
lic=input("Enter license plate:")
lic=lic.upper()
if re.match(r"^[A-Z]{3}[0-9]{3}$",lic):
    print(f"{lic} is valid for old licences")
elif re.match(r"^[0-9]{4}[A-Z]{3}$",lic):
    print(f"{lic} is valid for new licences")
else:
    print("Not valid for either style of license plate")