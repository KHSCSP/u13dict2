data = 'utilitatiscausaamicitiaestquaesitaloremipsumdolorsitametconsecteturadipiscingelitcollatioigituristatenihiliuvathonestaoratiosocraticaplatonisetiamprimuminnostranepotestateestquidmeminerimusduoregesconstructiointerretequidsietiamiucundamemoriaestpraeteritorummalorumsiquideminquittolleremsedrelinquoannisipopularifamaquamquamidquidemlicebitiisexistimarequilegerintsummumavobisbonumvoluptasdiciturathocineomreferttamenquomodoquidsequaturquidrepugnetvidentiamidipsumabsurdummaximummalumneglegi'
alpha = 'abcdefghijklmnopqrstuvwxyz'
counts = []
for letter in alpha:
  counts.append((letter, data.count(letter)))
print("\nhere's the list of tuples for the counts:")
print(counts)



counts = {}
for letter in alpha:
  counts[letter] = data.count(letter)
print("\nhere's the dictionary of counts:")
print(counts)


print("the largest count:", max(counts.values()))



most_val = 0
most_key = ''

for k, v in counts.items():
  if v > most_val:
    most_val = v
    most_key = k

print("max key:", most_key)
print("max value:", most_val)

