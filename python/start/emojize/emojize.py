import emoji

sentence=input("Input: ")

output=emoji.emojize(sentence,language='alias')

print("Output: "+output)