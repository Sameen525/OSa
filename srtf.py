bt=[]
at=[]
sum=0
smallest=0
sumt=0
sumw=0
i=1
j=1
p=[]
t=0
n=int(input("Enter number of Process : "))
for i in range(n):
   p.append(int(input("Enter process no :")))
   at.append(int(input("Enter arrival time of process :")))
   bt.append(int(input("Enter burst time of process :")))
   sum+=bt[i]

   



for t in range(sum):
     smallest=9
     for i in xrange(n):
       if(at[i]<t& bt[i]>0 & bt[i]<bt[smallest]):
         bt[i]=smalllest
print ("process ", "arrival time", '\t', "burst time")
for i in range(n):
   print(p[i],'\t\t', at[i],'\t\t', bt[i],'\n')
print (smallest+1,"\t","\t",t-at[smallest],"\t","\t",t+bt[smallest]-at[smallest])
sumt+=t+bt[smallest]-at[smallest]
sumw+=t-at[smallest]
t+=bt[smallest]
bt[smallest]=0

print ("\nAverage waiting time = ",sumw*1.0/n)
print ("Average Turnaround time = ",sumt*1.0/n)
 
