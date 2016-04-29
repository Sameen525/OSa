bt=[]
p=[]
at=[]
a=[]
p=[]
wait=0
await=0
sum1=0
i=0

n = int(input('Enter the total no of processes: '))
for i in range(n):
        p.append(int(input('Enter process no: ')))
        at.append(int(input("\nEnter process arrival time:\n")))
        bt.append(int(input("\nEnter Process Burst Time\n")))
print("\nProcess\t\tBurst Time\tarrival time,")
for i in range(n):
  print(p[i],'\t\t',bt[i],'\t\t',at[i])   
for i in range(n):
    p[i]=sum1
    sum1=sum1+bt[i]
    wait=wait+sum1-i
  
    
print("\n\ntotal Waiting Time:",wait)
print( "\nAverage waiting Time:",wait/n)
