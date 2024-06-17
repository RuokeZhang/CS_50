#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    res=True
    if not 2<=len(s)<=6:
        res=False
        return res
    if not (s[0].isalpha()and s[1].isalpha()):
        res=False
    if not s.isalnum():
        res=False
    for c in s:
        if c.isdigit():
            if c=='0':
                return False
            else:
                break
    flag=False
    for c in s:
        if c.isdigit():
            flag=True
        if c.isalpha() and flag:
            res=False
    return res

main()