import time
def fibonacci():

     numbers = []

     while True:

         if len(numbers) < 2:
             numbers.append(1)
         else:
             numbers.append(sum(numbers))
             numbers.pop(0)
         time.sleep(5)
         yield numbers[-1]


for i in fibonacci():
    print(str(i)+",")