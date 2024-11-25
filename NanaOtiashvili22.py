# import asyncio

# async def task_one():
#     print("Task 1 started.")
#     await asyncio.sleep(2) 
#     print("Task 1 finished.")


# async def task_two():
#     print("Task 2 started.")
#     await asyncio.sleep(5)
#     print("Task 2 finished.")


# async def main():
#     task1 = asyncio.create_task(task_one())
#     task2 = asyncio.create_task(task_two())

 
#     await task1
#     await task2

# if __name__ == "__main__":
#     asyncio.run(main())



# import asyncio
# import random

# async def random_delay_print():
#     delay = random.randint(1, 5)
#     print(f"Sleeping for {delay} seconds...")
#     await asyncio.sleep(delay)  
#     for i in range(1, 11):
#         print(i)


# async def main():
#     task1 = asyncio.create_task(random_delay_print())
#     task2 = asyncio.create_task(random_delay_print())
#     task3 = asyncio.create_task(random_delay_print())
    
 
#     await task1
#     await task2
#     await task3


# if __name__ == "__main__":
#     asyncio.run(main())





# import asyncio

# async def check_even(number):
#     await asyncio.sleep(1)  
#     return number % 2 == 0 


# async def square_if_even(number):
#     is_even = await check_even(number)
#     if is_even:
#         return number ** 2  
#     else:
#         return None  
# async def main():
#     numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]  
#     tasks = []
    
    
#     for number in numbers:
#         tasks.append(square_if_even(number))
    

#     results = await asyncio.gather(*tasks)
    
    
#     for number, result in zip(numbers, results):
#         if result is not None:
#             print(f"The square of {number} is {result}")
#         else:
#             print(f"{number} is not even, no square calculated.")


# if __name__ == "__main__":
#     asyncio.run(main())




import asyncio


async def write_to_file(filename, content):
    print(f"Task for {filename} started.")
    await asyncio.sleep(2)  

    with open(filename, 'w') as file:
        file.write(content)
    
    print(f"Task for {filename} finished.")


async def main():
    tasks = [
        write_to_file('file1.txt', 'This is the content for file 1.'),
        write_to_file('file2.txt', 'This is the content for file 2.'),
        write_to_file('file3.txt', 'This is the content for file 3.')
    ]
    
   
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
