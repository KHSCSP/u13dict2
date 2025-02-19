data = 'utilitatiscausaamicitiaestquaesitaloremipsumdolorsitametconsecteturadipiscingelitcollatioigituristatenihiliuvathonestaoratiosocraticaplatonisetiamprimuminnostranepotestateestquidmeminerimusduoregesconstructiointerretequidsietiamiucundamemoriaestpraeteritorummalorumsiquideminquittolleremsedrelinquoannisipopularifamaquamquamidquidemlicebitiisexistimarequilegerintsummumavobisbonumvoluptasdiciturathocineomreferttamenquomodoquidsequaturquidrepugnetvidentiamidipsumabsurdummaximummalumneglegi'
alpha = 'abcdefghijklmnopqrstuvwxyz'

# making a list of tuples
ans = []
for letter in alpha:
    temp = "TODO"
    ans.append(temp)
print("\nhere's the list of tuples for the counts:")
print(ans)



# making a dictionary of key : value pairs
ans = {}
for letter in alpha:
    temp = {"TODO":"TODO"}
    ans.update(temp)
    # or through value assignment
    # counts[letter] = data.count(letter)
print("\nhere's the dictionary of counts:")
print(ans)

print("the largest count:", max(ans.values()))
# but what key does it belong to??


# finding the largest
most_val = 0
most_key = ''

for k, v in ans.items():
    pass



print("max key:", most_key)
print("max value:", most_val)

