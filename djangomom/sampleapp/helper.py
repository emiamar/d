def classify(string):
    output_list = string.split(" ")
    output = list()
    for word in output_list:
        output += word.capitalize()
    return output
