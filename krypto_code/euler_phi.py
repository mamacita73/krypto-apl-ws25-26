

def euler_phi(n):
  if n<1: return None
  res=1
  for i in range(2,n):
     tmp_suc = True
     for j in range(2,i+1):
          if n%j==0 and i%j==0:
             tmp_suc = False
             break
     if tmp_suc:
         res = res+1
  return res
