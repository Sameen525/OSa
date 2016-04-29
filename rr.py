count
j
n
t
f

wait=0
trt=0
at=[]
bt=[]
rt=[]
p=[]

n = int(input('Enter the total no of processes: '))
r=n
for i in range(n):
        p.append(int(input('Enter process no: ')))
        at.append(int(input("\nEnter process arrival time:\n")))
        bt.append(int(input("\nEnter process burst time:\n")))
        rt[1]=bt[i]
print("\nProcess\t\tBurst Time\tarrival time,")
for i in range(n):
       print(p[i],'\t\t',bt[i],'\t\t',at[i]) 
printf("\n\nProcess\t|Turnaround Time|Waiting Time\n\n")

   
q = int(input('Enter time quantum: '))

        bt.append(int(input("\nEnter Process Burst Time\n")))
t=0
count=0
while(r!=0):
  if(rt[count]<=q && rt[count]>0):
     
      t+=rt[count] 
      rt[count]=0
      f=1
   elif(rt[count]>0): 
     
      rt[count]-=q 
      t+=q 
    if(rt[count]==0 && f==1): 
     
      r-- 
      print(count+1,t-at[count],t-at[count]-bt[count]) 
      wait+=t-at[count]-bt[count] 
      trt+=t-at[count] 
      f=0
    
    if(count==n-1): 
      count=0 
    elif(at[count+1]<=t): 
      count++ 
    else 
      count=0

print("\nAverage Waiting Time =",wai*1.0/n); 
print("\nAvg Turnaround Time =",trt*1.0/n); 
    