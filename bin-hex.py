print("Welcome to the Binary/Hexadecimal Converter App!")
print
full_range= int(input("Compute binary and hexadecimal values upt the following decimal number: "))

range_ = list(range(1,full_range+1))

print("Generating lists....complete!")

print("\n\n")

print("Using slices, we will now show a portion of each list.")
portion_start =int(input("what decimal number would you like to start at: "))
portion_end = int(input("what decimal number would you like to stop at: "))
sliced_list = list(range(portion_start, portion_end+1))
print("Decimal values from",portion_start,"to", portion_end)
for n in range(len(sliced_list)):
    print(sliced_list[n])

print("Binary value from",portion_start,"to",portion_end)

for n in range(len(sliced_list)):
    print(bin(sliced_list[n]))

print("")

print("Hexadecimal values from",portion_start,"to", portion_end)

for n in range(len(sliced_list)):
    print(hex(sliced_list[n]))

print("\n\n\n")

input("Press Enter to see all values from 1 to "+str(full_range))

print("Decimal-------Binary---------Hexadecimal")
print("------------------------------------------------------")
print("\n\n")

bin_=[]
hex_=[]

for c in range(1,full_range+1):
    bin_.append(bin(c))
    hex_.append(hex(c))

for d,b,h in zip(range_,bin_,hex_):
    print(d,"\t\t"+b,"\t\t"+h)