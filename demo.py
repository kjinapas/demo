sample_text = input("enter your input: ")
def checkstr(x):
    try:
        float(x)
        return print('The type is not a string')
    except ValueError:
        return print('The type is a string')
checkstr(sample_text)