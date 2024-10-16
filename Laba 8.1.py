string1 = input("Введіть перший рядок: ")
string2 = input("Введіть другий рядок: ")
set1 = set(string1)
set2 = set(string2)
common_chars = set1 & set2
if common_chars:
    print("Символи, які зустрічаються в обох рядках:", ''.join(common_chars))
else:
    print("Немає спільних символів у обох рядках.")