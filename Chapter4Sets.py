def inputStr():
    str1 = input("Enter the first string: ")
    str2 = input('Enter the second string' '\n(Some characters must be common in the first string): ')
    return str1, str2
def uncommonConcat(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common = list(set1 & set2)
    result = [cha for cha in str1 if cha not in common] + [cha for cha in str2 if cha not in common]
    print(''.join(result))
str1, str2 = inputStr()
uncommonConcat(str1, str2)