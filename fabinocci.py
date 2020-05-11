print("Welcome to fabinocci series app.")

range_ = int(input("Enter a number upto which you want fibinocci series: "))

a =1
b=0
list_ =[1,1]

for c in range(0,range_):
    num = list_[c]+list_[c+1]
    list_.append(num)
for v in list_[:range_]:
    print(v)

print("The corresponding Golden Ratio values are:")
golden_ratio =[1,1]
for c in range(0,range_):
    num = float(list_[c+1]/list_[c])
    golden_ratio.append(num)
for v in golden_ratio[2:range_+1]:
    print(v)

print("The ratio of consecutive fibonacci terms approaches phi:",str(round(golden_ratio[-1],3)),"...")