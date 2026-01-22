print('Hello world')
print("*"*20)
x = 9
n = 8
course = "hello \"world"
print(course.title())

n=False

for num in range(3):
    print('Antempt',num +1)
    if n :
        print('successful')
        break
else:
    print('Antempt 3 reached failed')

for p in range(6):
    print(p* '*')

for x in range(5):
    for y in range(3):
        print(f"({x} {y})")

count=0
sum=0
for number in range(1,10):
    if number %2 ==0:
        count +=1
        sum = sum + number
        print(number)
print(f"We have {count} numbers of even sum is {sum}")


# Two Sum
class solution:
    def twosum(self, nums, target):
        n= len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
         
    

# Best Time to Buy and Sell Stock
class profite:
    def maxprofite(self,prices):
        min_price=float('inf')
        max_profite=0

        for price in prices:
            min_price=min(min_price,price)
            max_profite=max(max_profite,price - min_price)
        return max_profite
    

#Intersection of Two Arrays
class insertion:
    def twoarray(self,num1:list[int],num2:list[int]):
        return list(set(num1) & set(num2))


#Remove Element
class element:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0

        for num in nums:
            if num !=val:
                nums[k]=num
                k +=1
        return k



class triangle:
    def generate(self, numRows):
        triangle=[]
        for i in range(numRows):
            row=[1] * (i + 1)
            for j in range(1,i):
                row[j]=triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle




class sum:
    def triangularSum(self, nums: list[int]) -> int:

        while len(nums)>1:
            nums=[(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
        return nums[0]
    

class currentnumber:
    def smallerNumbersThanCurrent(self, nums):
        s=sorted(nums)
        return [s.index(x) for x in nums]
    


# -------- Test the function --------
if __name__ == "__main__":

## Two Sum
    sol = solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twosum(nums, target))

## Best Time to Buy and Sell Stock
    sol1=profite()
    num=[3,5,6,3,1,7]
    print(sol1.maxprofite(num))

##Intersection of Two Arrays
    sol2=insertion()
    num1=[2,4,5,6,7,8]
    num2=[2,0,9,8]
    print(sol2.twoarray(num1,num2))

#Remove Element
    sol3=element()
    numbers=[2,4,1,6,5]
    val=3
    print(sol3.removeElement(numbers,val))


    sol4=triangle()
    Rows=5
    print(sol4.generate(Rows))


    sol5=sum()
    arr=[1,2,3,4,5]
    print(sol5.triangularSum(arr))



    sol6=currentnumber()
    arr=[8,1,2,2,3]
    print(sol6.smallerNumbersThanCurrent(arr))


