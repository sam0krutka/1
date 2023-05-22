strings = ["bella", "label", "roller"]
common_letters = set(strings[0])
for string in strings[1:]:
    common_letters = common_letters.intersection(set(string))
print(list(common_letters))