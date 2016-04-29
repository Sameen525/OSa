bt=[]
p=[]
wt=[]
at=[]
i=1
j=1
pos=0
total=0
pos
p=[]
n = int(input('Enter the total no of processes: '))

for i in range(n):
       p.append(int(input('Enter process no\n ')))
       at.append(int(input('Enter arrival time:\n ')))   
       bt.append(int(input("\nEnter Burst Time:\n")))
  

j=1 
  
for i in range(n):
    pos=i
    for j  in range(n):
       
         if(bt[j]<bt[pos]):
           pos=j
           temp=bt[i]
           bt[i]=bt[pos]
           bt[pos]=temp
 
           temp=at[i]
           at[i]=at[pos]
           at[pos]=temp
   
 
wt.append(0)           
    

for i in range(n):
     wt.append(0)
     for j in range(i):
        wt[i]+=bt[j]
 
        total+=wt[i]
    
 
   
 
print("\nProcess\t\tBurst Time\tWaiting Time\tarrival Time")
for i in range(n):
    
    print (p[i],'\t\t',at[i],'\t\t',bt[i], '\t\t',wt[i])
    
 
print("\n\nWaiting Time=%f",total)
print("\nAverage waiting Time=%f\n",total/n)
