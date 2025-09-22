"""
Task 6: File Handling and Metaprogramming
Create two new files named task6.py and task6_read_me.txt. Then write a program inside
task6.py of that reads task6_read_me.txt and counts the number of words in it. Include
pytest test cases that verify the word count for each text file.
"""

def count_words_from_file(file_path):
    """
    Counts the number of words in a text file
    
    Args:
        file_path: string containing the path of the file to read

    Returns:
        an integer representing the total word count
    """
    with open(file_path, "r") as f:
        total_words = 0
        for line in f:
            total_words += len(line.split())
        return total_words

if __name__ == '__main__':
    file_path = "src/task6_read_me.txt"
    total_words = count_words_from_file(file_path)
    print("The total word count is", total_words)