def matricalation(ID):
    sum =0
    for x in ID:
        sum += int(x)
    return sum


amer_ID = input("Enter your matriculation number here ")
nawar_ID = input("Enter your matriculation number here")
sum2 = matricalation(nawar_ID)
sum1 = matricalation(amer_ID)
print(sum1/sum2)

# Could you please commit you edit?