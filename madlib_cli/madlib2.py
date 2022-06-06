def read_template(filePath):
    # return "It was a {Adjective} and {Adjective} {Noun}."
    try:
        with open(filePath,'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "You have a FileNotFoundError, the file path is invalid"



def parse_template(str):
    newStr = str.replace("{Adjective}", "{}")
    newStr2 = newStr.replace("{Noun}","{}")
    return [newStr2, ("Adjective", "Adjective", "Noun")]


def merge(str,values):
    return str.format(*values)


# text = "It was a {0} and {1} {2}.".format("dark", "stormy", "night")
# print(text)
val = ("dark", "stormy", "night")
print(merge("It was a {} and {} {}",("dark", "stormy", "night")))
