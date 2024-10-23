#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
# This script is demonstrate some string methods

# For lowercasing of strings
text="1. My mum loves me so much and I love her too."
print(text.lower())

# For uppercasing of strings
message="2. Naa's favourite genre of music is Gospel"
print(message.upper())

# For replacing of strings
info="3. I've decided to follow the world all my life"
print(info.replace( 'world', 'Jesus' ))

# For Joining strings
string1=("4. Twitter's new", "news update", "are intridging.")
X = "#".join(string1)
print(X)