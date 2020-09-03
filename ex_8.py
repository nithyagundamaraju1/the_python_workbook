wid=75
giz=112
w=int(input("Enter the number of widgets: "))
g=int(input("Enter the number of gizmos: "))
tot_wt= float(((wid*w)+(giz*g))/1000)
print("Total Order Weight: "+"{:.2f}".format(tot_wt)+"kgs")
