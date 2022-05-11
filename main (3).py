# Goldbach's conjecture 

n = int(input("enter the number:"))
def Goldbach(n):
  def prime(n):
    c=0
    for i in range(1,n+1):
      if n%i==0:
        c+=1
    if c==2:
      return True
    else:
      return False
  p=[]
  for i in range(n):
    if prime(i):
      p.append(i)
  print("list of prime number:\n",p)
  L=[]
  for i in range(len(p)):
    for j in range(i,len(p)):
      if p[i]+p[j]==n:
        L.append((p[i],p[j]))

  return L

print("pairs are:\n",sorted(Goldbach(n)))
        
      