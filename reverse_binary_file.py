def reverse_binary_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    
    # Reverse the content
    reversed_content = content[::-1]

    with open(output_file, 'wb') as f:
        f.write(reversed_content)

input_file = 'test.jpg'
output_file = 'reference_file.jpg'

reverse_binary_file(input_file, output_file)

print("Binary file content reversed successfully.")
