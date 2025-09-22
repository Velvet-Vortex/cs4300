from src.task5 import fav_books, student_data

class TestList:
    # Verify that the list is of type list
    def test_list_data_type(self):
        assert isinstance(fav_books, list)
    
    # Verify all the contents are tuples
    def test_list_content_type(self):
        assert all(isinstance(book, tuple) for book in fav_books)

    # Check an item in the list content 
    def test_list_content(self):
        assert ("Algorithms to Live By", "Brian Christian and Tom Griffiths") in fav_books
    
    # Check the list can be slices properly
    def test_list_slicing(self):
        sliced_list = fav_books[0:3]
        expected_output = [('1984', 'George Orwell'), ('Algorithms to Live By', 'Brian Christian and Tom Griffiths'), ('Paper Towns', 'John Green')]
        assert sliced_list == expected_output

    # Verify the list length
    def test_list_length(self):
        assert len(fav_books) == 5

class TestDictionary:
    # Verify that the dictionary is of type dictionary
    def test_dict_data_type(self):
        assert isinstance(student_data, dict)

    # Verify the keys of the dictionary have the right content
    def test_dict_keys(self):
        expected_students = {"Avalee Cruz", "Isabel Rivera", "Jackson Seales", "Addy Rohr", "Senna Smoak", "John Smith"}
        assert set(student_data.keys()) == expected_students

    # Verify the values of the dictionary have the right content
    def test_dict_values(self):
        expected_ids = {"0000", "0101", "3005", "2004", "0123", "1968"}
        assert set(student_data.values()) == expected_ids

    # Verify the dictionary length
    def test_dict_length(self):
        assert len(student_data) == 6

    # Verify the dictionary update operation
    def test_dict_update(self):
        student_data.update({"New Student": "2005"})
        assert "New Student" in student_data.keys() and "2005" in student_data.values()