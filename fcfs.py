bt=[]
p=[]
at=[]
a=[]
p=[]
wait=0
tat=0
twait=0
sum1=0
i=0

n = int(input('Enter the total no of processes: '))
for i in range(n):
        p.append(int(input('Enter process no: ')))
        at.append(int(input("\nEnter process arrival time:\n")))
        bt.append(int(input("\nEnter Process Burst Time\n")))
print("\nProcess\t\tBurst Time\tarrival time,\twaiting_time,\tturnarount_time")
for i in range(n):
  twait+=wait
  tat=bt[i]+wait  
  print(p[i],'\t\t',bt[i],'\t\t',at[i],'\t\t',wait,'\t\t',tat)
  
  wait+=bt[i]
  
  
    
print("\n\ntotal Waiting Time:",twait)
print("\naverage Waiting Time:",twait/n)
print( "\ntotal turnArround Time:",tat/n)
print( "\nAverage turnArround Time:",tat/n)
