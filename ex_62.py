op=[4.95,9.95,14.95,19.95,24.95]
l=len(op)

print('Original|  Discount\t|  New Price|')
print('------------------------------------------')


for i in range(0,l):
    org=op[i]
    disc= 0.06*org
    new=org-disc 
    print(f"{org:.02f} \t|\t {disc:.02f}\t|\t{new:.02f}") 
    