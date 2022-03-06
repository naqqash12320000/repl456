import re


import re

str = f"My name is Muhammad Zaeem Nasir #general and i went to Muslim School %sdkl;jasdf sadsa"

# if the Excat match is found
if re.search(r"#generasl", str):
    print("Found")
else:
    print("Not Found")
