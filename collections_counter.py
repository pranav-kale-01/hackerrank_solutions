from collections import Counter

x = int(input())
shoe_sizes = input().split(" ") 
no_customers = int(input())
counter = Counter(shoe_sizes)
l = []
money_earned = 0

for i in range(no_customers):
    size_desired, price_paying = input().split(" ")
    if( counter[size_desired] > 0 ):
        money_earned += int(price_paying)
        counter[size_desired] = int( counter[size_desired] ) -1
        
print( money_earned )