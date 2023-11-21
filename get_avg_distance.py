def read_text_file_and_calculate_average(file_path):
    # Initialize a list to store lists from the text file
    all_lists = []

    # Read the text file
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Convert each element to a float and add it to the corresponding list
            current_list = [float(value.strip('[],')) for value in line.split()]
            all_lists.append(current_list)

    # Transpose the lists to group elements by their index
    transposed_lists = zip(*all_lists)

    # Calculate the average for each index across all lists
    avg_list = [sum(values) / len(values) for values in transposed_lists]
    str_list = [str(element) for element in avg_list]

    # Join the list elements into a single string
    list_string = ' '.join(str_list)

    with open ("avg_distance.txt", "w") as file:
         file.write(list_string)
         file.close()
    return avg_list
	
# Replace 'your_file.txt' with the path to your text file
file_path = 'Distance.txt'
average_list = read_text_file_and_calculate_average(file_path)

# Print the average list
print(f'Average list: {average_list}')
