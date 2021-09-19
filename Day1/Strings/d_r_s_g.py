class drsg:
    def digit_range_sum_generator(self,a,n):
        list1 = []
        sum = 0
        for i in range(1,n+1):
            num = int(i*str(a))
            sum=sum+num
            list1.append(num)
            
        print(list1)
        print(sum)

obj = drsg()
x = int(input("Enter a number: "))
n = int(input("Enter n value: "))
obj.digit_range_sum_generator(x,n)