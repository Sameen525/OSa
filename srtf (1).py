at=[]
bt=[]
bt1=[]
twait=0
tat=0
n=int(input("Enter number of Process : "))
i=0
while i<n:
	print("enter for process:",i+1) 
	at.append(int(input("Enter arrival time of process :")))
	bt.append(int(input("Enter arrival time of process :")))
	bt1.append(bt[i])
	i+=1

print("\nProcess\t\tBurst Time\tarrival time,")
for i in range(n):
       print(p[i],'\t\t',bt[i],'\t\t',at[i])

print ("\n\nProcess\tTurnaround Time\t Waiting Time\n")

t=0;r=0;j=i   	
while r!=n:
        smallest=j
        i=0
        while i<n:
                if at[i]<=t and bt1[i]<bt1[smallest] and bt1[i]>0:
                        smallest=i
                        i+=1
                        bt1[smallest]-=1
                        if bt1[smallest]==0:
                                r+=1
                                ft=time+1
                                print(smallest+1,"\t",ft-at[smallest],"\t","\t",ft-bt1[smallest]-at[smallest])
                                twait+=ft-bt1[smallest]-at[smallest]
                                tat+=ft-at[smallest]
                        t+=1
print ("\nAverage waiting time = ",twait/n)
print ("Average Turnaround time = ",tat/5)
 
