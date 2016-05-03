sum=0
time=0
twait=0
ttat=0
at=[]
bt=[]
wait=[]
p=[]
tat=[]
ft=[]
bt1=[]
n = int(input('Enter the total no of processes: '))

for i in range(n):
        p.append(int(input('Enter process no: ')))
        at.append(int(input("\nEnter process arrival time:\n")))
        bt.append(int(input("\nEnter process burst time:\n")))
        bt1.append(bt[i])
        sum+=bt[i]
        ft.append(0)
        wait.append(0)
        tat.append(0)
print("\nProcess\t\tBurst Time\tarrival time,")
for i in range(n):
       print(p[i],'\t\t',bt[i],'\t\t',at[i]) 

q = int(input('Enter time quantum: '))
time=at[0]


a=0
while(sum>0):
       if(bt1[a]<q and bt1[a]!=0 and at[a]<=time):
          sum-=bt1[a]
          time+=bt1[a]
          ft[a]=time
          bt1[a]=0
          
       elif(bt1[a]>=q and at[a]<=time):
           bt1[a]=bt1[a]-q
           sum-=q
           time+=q
       if a==n-1:
                a=0
       else:
               a=a+1

i=0

print("\n\nProcess\tBurst Time\tarrival time\tTurnaround Time\tWaiting Time\n")
for i in range(n):
    wait[i]=ft[i]-at[i]-bt[i]
    tat[i]= ft[i]- at[i]    
    print(p[i],'\t\t',bt[i],'\t\t',at[i],'\t\t',tat[i],'\t\t',wait[i])    

i=0
for i in range(n):
    twait+=wait[i]
    ttat+=tat[i]


print("\nWaiting Time =",twait);
print("\nAverage Waiting Time =",twait/n); 
print("\n Turnaround Time =",ttat); 
print("\nAvg Turnaround Time =",ttat/n); 
        
a
