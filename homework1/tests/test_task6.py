import pytest
from src.task6 import count_words_from_file

# Verify the word count of the task6_read_me.txt
def test_word_count():
    file_name = "src/task6_read_me.txt"
    assert count_words_from_file(file_name) == 104

testdata= [
    ("Hello World!", 2),
    ("Another list of words", 4),
    ("""We the People of the United States, in Order to form a more perfect Union,
    establish Justice, insure domestic Tranquility, provide for the common defence,
    promote the general Welfare, and secure the Blessings of Liberty to ourselves
    and our Posterity, do ordain and establish this Constitution for the United 
    States of America.""", 52)
]

# Verify that the function works for other text files with parameterized cases
@pytest.mark.parametrize("file_content,expected_count", testdata)
def test_other_files(tmp_path, file_content, expected_count):
    file_path = tmp_path / "test.txt"
    file_path.write_text(file_content)
    result = count_words_from_file(file_path)
    assert result == expected_count