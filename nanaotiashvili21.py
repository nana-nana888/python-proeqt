# import json
# import threading


# def parse_json(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             data = json.load(file)
#             print(f"Contents of {file_name}:")
#             print(json.dumps(data, indent=4))  
#             print("\n")
#     except Exception as e:
#         print(f"Error reading {file_name}: {e}")


# def main():
    
#     files = ['choice1.json', 'choice2.json', 'choice3.json']
    
#     threads = []
#     for file in files:
#         thread = threading.Thread(target=parse_json, args=(file,))
#         threads.append(thread)
#         thread.start()  
    
#     for thread in threads:
#         thread.join()

# if __name__ == "__main__":
#     main()





import threading
import queue

def check_even(queue):
   
    thread_name = threading.current_thread().name
    try:
        while not queue.empty():
            number = queue.get()
            is_even = number % 2 == 0
            print(f"{thread_name} - Number: {number}, Even: {is_even}")
            queue.task_done()
    except Exception as e:
        print(f"Error in {thread_name}: {e}")

def main():
    q = queue.Queue()
    numbers = [10, 15, 20, 25, 30, 35]  

    for number in numbers:
        q.put(number)

    threads = []
    for i in range(3):
        thread = threading.Thread(target=check_even, args=(q,), name=f"Thread-{i+1}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All tasks have been completed.")

if __name__ == "__main__":
    main()
