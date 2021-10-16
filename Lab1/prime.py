import multiprocessing
import threading 
import queue

a=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    temp = int(input("Enter number:"))
    num = a.append(temp)

def check_prime(num):
     if num in [0,1]:
          pass
     else:
          x=0
          for j in range(2,num):

               if num%j==0:
                    x+=1
                    if x>0:return False
          return True

def threader():
     while True:
          value=q.get()
          result=check_prime(value)

          if result == True:
              print(value, "is prime")
          else :
              print(value, "is not prime")
          q.task_done()


q=queue.Queue()
for x in range(30):
     t=threading.Thread(target=threader)
    
     t.start()

for value in a:
     q.put(value)
q.join() 
print('There are ', threading.active_count(), 'thread(s) running by now')