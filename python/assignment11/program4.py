import pandas as pd

# Example DataFrame representing the next 10 days
data = {
    "John": [True, False, True, False, False, True, False, False, True, False],
    "Judy": [False, True, True, False, False, False, True, False, False, True]
}
schedule = pd.DataFrame(data)
print(schedule)
#print(len(schedule))
days_til_party = []
for i in range(len(schedule)):
    for j in range(i, len(schedule)):
        if schedule["John"][j] and schedule["Judy"][j]:
            days_til_party.append(j - i)
            break
    else: 
        days_til_party.append(None)

schedule["days_til_party"] = days_til_party

print(schedule)