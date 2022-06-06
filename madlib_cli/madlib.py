#Print the welcoming message
print("Welcome to the madlib Terminal Game, we will take some words from you and combine it with some from our side, This is really funny you should give it a try!!")

def read_template(filePath):
    # it should return the content of the template file
    try:
        with open(filePath,'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "You have a FileNotFoundError, the file path is invalid"


def parse_template(str):

    words_to_replace = {'{Adjective}': '{}',
                        '{A First Name}': '{}',
                        '{Large Animal}': '{}',
                        '{Small Animal}': '{}',
                        "{A Girl's Name}": "{}",
                        '{Number}':'{}',
                        '{Past Tense Verb}':'{}',
                        "{First Name's}": "{}",
                        "{Number 1-50}": "{}",
                        '{Plural Noun}': '{}'}

        # Iterate over all key-value pairs in dictionary
    for key, value in words_to_replace.items():
        # Replace key character with value character in string
        str = str.replace(key, value)

    # return [str,("Adjective", "Adjective", "A_First_Name", "Adjective","Adjective", "Plural Noun", "Large Animal", "Small Animal", "A Girl's Name", "Adjective", "Plural Noun", "Adjective", "Plural Noun", "Number 1-50", "First Name's", "Number", "Plural Noun", "Number", "Plural Noun")]
    return str



def merge(str,values):
    with open("../assets/solvedTemplateFile",'w') as file:
        file.write(str.format(*values))
    return str.format(*values)


#I've added this method only for testing the merge, because creating a file is not testable
def merge_for_test(str,values):
    return str.format(*values)



#Running the files
inputs = []
input1Adjective = input("Type an adjective: ")
inputs.append(input1Adjective)

input2Adjective = input("Type an adjective: ")
inputs.append(input2Adjective)

input3A_First_Name = input("Type a First name: ")
inputs.append(input3A_First_Name)

input4PastTenseVerb = input("Type a Past Tense Verb: ")
inputs.append(input4PastTenseVerb)

input5aFirstName = input("Type a First Name: ")
inputs.append(input5aFirstName)

input6Adjective = input("Type an Adjective: ")
inputs.append(input6Adjective)

input7Adjective = input("Type an Adjective: ")
inputs.append(input7Adjective)

input8pluralNoun = input("Type a Plural Noun: ")
inputs.append(input8pluralNoun)

input9largeAnimal = input("Type a Large Animal: ")
inputs.append(input9largeAnimal)

input10smallAnimal = input("Type a Small Animal: ")
inputs.append(input10smallAnimal)

input11aGirlName = input("Type a Girl's Name: ")
inputs.append(input11aGirlName)

input12Advective = input("Type an Adjective: ")
inputs.append(input12Advective)

input13pluralNoun = input("Type a Plural Noun: ")
inputs.append(input13pluralNoun)

input14Adjective = input("Type an Adjective: ")
inputs.append(input14Adjective)

input15pluralNoun = input("Type a Plural Noun: ")
inputs.append(input15pluralNoun)

input16number1_50 = input("Type a Number between 1 and 50: ")
inputs.append(input16number1_50)

input17firstName = input("Type a First Name: ")
inputs.append(input17firstName)

input18number = input("Type a Number: ")
inputs.append(input18number)

input19pluralNoun = input("Type a Plural Noun: ")
inputs.append(input19pluralNoun)

input20number = input("Type a Number: ")
inputs.append(input20number)

input21pluralNoun = input("Type a Plural Noun: ")
inputs.append(input21pluralNoun)


print(merge(parse_template(read_template("../assets/templateFile.txt")),inputs))

