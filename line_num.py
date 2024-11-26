import os

def count_lines_in_file(file_path):
    total_lines = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('<!--'):
                total_lines += 1
    return total_lines

def count_lines_in_directory(directory_path):
    total_lines = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html') or file.endswith('.py'):
                file_path = os.path.join(root, file)
                total_lines += count_lines_in_file(file_path)
                print(f"Processed: {file_path}") 
    return total_lines

folder_path = '/mnt/e/实验3_221240068_周凡淇/task_list1'
total = count_lines_in_directory(folder_path)

print(f"Total lines of code in .html and .py files: {total}")
