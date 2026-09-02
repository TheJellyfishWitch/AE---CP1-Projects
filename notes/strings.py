# AE | Strings Notes

# any characters or symbols that are put together in quotation marks

name = "Addie" # <- string
age = "15" # <- string, cannnot do math with
print(age + "2") # <- prints 15 and 2 together = 152, cacaination

age_hehe = 15 # <- not string

print(age+name) # <- no spaces between strings, would have to canatate a space in
print(name + " " + age)

# can also use single quotes, escape char \
first = '\they, it\'s okay \nI "forgive you"'
print(first)

print(name * 4)
print("-" * 30)


sentance = "the quick brown fox jumps over the lazy dog"
          # ^ "t" is zero
print(sentance)
print(sentance.find("w"))
print(sentance.find("t"))
print(sentance.find("jumps"))
print(sentance[20:26]) # <- does not include the end point
print(sentance[10:15])

word = "jumps"
start = sentance.find(word)
length = len(word)
print(sentance[start:start+length])
