import sys

def moon_weight(weight, plus, year):
    for x in range(0,year):
        print("Year %d : %2.2f  Weight is %2.2f" % (x + 1, weight * 0.165, weight))
        weight = weight + plus

print("First weight?")
weight = float(sys.stdin.readline())
print("Plus?")
plus = float(sys.stdin.readline())
print("Year?")
year = int(sys.stdin.readline())
print("\n")
        
moon_weight(weight, plus, year)
