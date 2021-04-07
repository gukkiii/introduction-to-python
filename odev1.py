
liste1=[0,1,2,3,4,5,6,7,8,9]
liste2=[]
liste3=[]
liste2.extend(liste1)

for i in range(len(liste2)):
    if i<5:
        liste3.append(liste2[i])
        
    elif i>=5 and i<=9:
        liste3.insert(i-5,liste2[i])
        

print("|{:^100}|".format("ÖDEVİN SONUCU"))
print(liste3)


