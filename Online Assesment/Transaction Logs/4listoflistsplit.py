items = ['99 77 44']
logs = [["88 99 200"], ["88 99 300"], ["99 32 100"], ["12 12 15"]] 
individual_items = []

for log in logs:
    #print(log)
    for lo in log:
        individual_items.extend(lo.split()) # this is an alternative way to make evey list of list items in one list
                                            # making its properties blend to the individual block of data to manipulate it.
print(individual_items)