# # N1
# with open('test.txt', 'w') as file:
#     for i in range(1, 1001):
#         file.write(f"{i}\n")

# with open('test.txt', 'r') as file:
#     lines = file.readlines()
#     line_count = len(lines)

# print(f": {line_count}")

# #N2
# file_name = 'text_number.txt'
# with open(file_name, 'w') as file:
#     for i in range(1, 21): 
#         if i == 2:
#             file.write("second line\n")
#         elif i == 8:
#             file.write("eight line\n")
#         elif i == 10:
#             file.write("tenth line\n")
#         elif i == 13:
#             file.write("thirteen line\n")
#         elif i == 17:
#             file.write("seventeen line\n")
#         else:
#             file.write(f"{i} - other line\n")

# print(file_name)

 # N3

file_name1 = 'file1.txt'
file_name2 = 'file2.txt'
merged_file_name = 'merged_file.txt'


with open(file_name1 , 'w') as file1, open(file_name2 , 'w') as file2:
    file1.write("first file text.\n")
    file1.write("first file text2.\n") 
    file2.write("second file text.\n")
    file2.write("second file text2.\n") 

with open(file_name1 , 'r') as file1, open(file_name2 , 'r') as file2:
    file1_content = file1.readlines()
    file2_content = file2.readlines()

with open(merged_file_name, 'w') as merged_file:
    merged_file.writelines(file1_content)
    merged_file.writelines(file2_content)

with open(merged_file_name, 'r') as merged_file:
    merged_content = merged_file.read()

print("marged files:")
print(merged_content)
