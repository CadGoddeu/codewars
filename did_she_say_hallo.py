import re
def validate_hello(greetings):
    lst = re.findall(r'\w+', greetings.lower())
    print(lst)
    return True if any(x for x in lst if x in ["hello", "hallo", "ciao", "salut", "hola", "ahoj", "czesc"]) else False

print(validate_hello('czesc'))