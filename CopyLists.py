# household ages 

ages = [27, 27, 5, 4, 1]

#take a copy of the list - but this must be a standalone copy and not amend orginal ages list 

ages_copy = list(ages)

# Prove this by amending ages_copy and ages stays same 

del ages_copy[3:]

print(ages)
print(ages_copy)
