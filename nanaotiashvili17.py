# class Node:
#     def __init__(self, data=None):
#         self.data = data # node-ში მონაცემების შენახვა
#         self.next = None


# class LinkedList: # lass LinkedList შექმნა, რომელიც წარმოადგენს სიაში მონაცემების შენახვას და მარტვას
#     def __init__(self):
#         self.head = None

#     def append(self, data): # ელემენტის დამატება სიის ბოლოში
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return

#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next

#         last_node.next = new_node
 
#     def remove_at(self, index): # ელემენტის წაშლა მოცემული ინდექსის მიხედვით
#         if index < 0 or self.head is None: # თუ ინდექსი უარყოფითი ან სია ცარიელია
#             return

#         if index == 0:  # თუ უნდა წავშალოთ პირველი ელემენტი
#             self.head = self.head.next 
#             return

#         current_node = self.head
#         current_position = 0

#         while current_node.next and current_position < index - 1:  # ვეძებთ  რომელი უნდა წავშალოთ
#             current_node = current_node.next
#             current_position += 1

#         if current_node.next:
#             current_node.next = current_node.next.next

#     def display(self):  # დაბეჭდვის, გამოსახვის ლოგიკა
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=' -> ') # დაბეჭდოს 1 ხაზზე
#             current_node = current_node.next

#         print()


# linked_list = LinkedList() # შეიქმნება ახალი სია

# linked_list.append(50)  # 0
# linked_list.append(15)  # 1
# linked_list.append(20)  # 2
# linked_list.append(11)  # 3
# linked_list.append(5)  # 4
# linked_list.append(25)  # 5

# linked_list.display()
# linked_list.remove_at(2)
# linked_list.display()
# linked_list.remove_at(2)
# linked_list.display()
# linked_list.remove_at(0)
# linked_list.display()
# linked_list.remove_at(2)
# linked_list.display()




# class Node: # Node კლასის შექმნა
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None


# class Stack: # Stack კლასის შექმნა
#     def __init__(self):
#         self.top_node = None
#         self.length = 0

#     def empty(self): # მეთოდით ვიგებტ ცარიელია ტუ არა
#         return self.length == 0

#     def size(self):  # დაააბრუნებს სიგრძეს
#         return self.length

#     def push(self, data): # ელემენტის დამატება
#         new_node = Node(data)
#         new_node.next = self.top_node # ყველაზე ზედა ელემენტი
#         self.top_node = new_node
#         self.length += 1

#     def pop(self): # ელემენტის ამოღება 
#         if not self.empty():
#             popped_item = self.top_node.data 
#             self.top_node = self.top_node.next
#             self.length -= 1
#             return popped_item
#         else:
#             raise IndexError("Stack is empty")



# stack = Stack() # Stack ობიექტი

# print(stack.empty()) # ტუ ცარიელია დაბეჭდავს true
# print(stack.length) # დაბეჭდავს სიგრძეს

# stack.push(200) # დაამატებს ბოლოში ელემენტებს
# stack.push(50)
# stack.push(75)
# stack.push(25)
# stack.push(30)

# print(stack.empty())
# print(stack.length)

# print(stack.pop())
# print(stack.empty())
# print(stack.length)
# print(stack.pop())
# print(stack.length)
# print(stack.pop())
# print(stack.length)
# print(stack.pop())
# print(stack.length)
# print(stack.pop())
# print(stack.empty())
# print(stack.length)
# print(stack.pop())




class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_value(self, value):

        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current_node = self.head  
        while current_node.next: 
            if current_node.next.data == value: 
                current_node.next = current_node.next.next  
                return
            current_node = current_node.next  

   
    def insert_at(self, index, data):
   
        if index < 0:
            raise IndexError("Index cannot be negative")

        new_node = Node(data) 
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_position = 0

        
        while current_node and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node is None:
            raise IndexError("Index out of range")  

        new_node.next = current_node.next
        current_node.next = new_node

    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print()


linked_list = LinkedList()


linked_list.insert_at(0, 10)  
linked_list.insert_at(1, 20)  
linked_list.insert_at(1, 15)  
linked_list.insert_at(0, 5)   


linked_list.display()


linked_list.remove_value(15)  


linked_list.display() 


linked_list.remove_value(5)  


linked_list.display()  
