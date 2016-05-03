bt=[]
wt=[]
p=[]
wait=0
twait=0
at=[]
i=1
j=1
p=[]
n = int(input('Enter the total no of processes: '))

for i in range(n):
       p.append(int(input('Enter process no\n ')))
       at.append(int(input('Enter arrival time:\n ')))   
       bt.append(int(input("\nEnter Burst Time:\n")))

print("\nProcess\t\tBurst Time\tarrival Time")
for i in range(n):
    
    print (p[i],'\t\t',bt[i],'\t\t',at[i])       
  

 
 
for i in range(n):
    
    for j  in range(n):
       
         if(bt[i]<bt[j]):
           
           temp=bt[i]
           bt[i]=bt[j]
           bt[j]=temp
 
           temp=at[i]
           at[i]=at[j]
           at[j]=temp
          
print("\n\nProcess\t\tBurst Time\tarrival Time")
for i in range(n):
    
    print (p[i],'\t\t',bt[i],'\t\t',at[i])       
            

print("\nProcess\tBurst Time\tWaiting Time\tarrival Time\ttat-time")
for i in range(n):
  twait+=wait
  tat=bt[i]+wait  
  print(p[i],'\t\t',bt[i],'\t\t',wait,'\t\t',at[i],'\t\t',tat)
  
  wait+=bt[i]
     
     
 
   
 

 
print("\n\nWaiting Time=",wait)
print("\nAverage waiting Time=",wait/n)
