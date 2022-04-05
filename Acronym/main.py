get = str(input("Enter a Phrase to get an acronym: "))
word = get.split()
new_word = " "
for x in word:
    new_word = new_word+str(x[0]).upper()
print("Your Acronym is "+ new_word)