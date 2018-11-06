import sys
def print_star(n):
    print(("*"*n).center(50))
#a = int(input("请输入："))
#print(print_star(a),end = '')
#print_star(a+1) 
lines = int(sys.argv[1])
for i in range(1, 2*lines,2):
  print_star(i)	
