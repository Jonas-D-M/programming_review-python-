from models.Bier import Bier


list_bieren = Bier.inlezen_bieren()

for i in list_bieren:
    print(i)

print(len(list_bieren))

