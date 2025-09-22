# Test the output is "Hello, World!"
def test_print_hello_world(capsys):
    import src.task1
    output, err = capsys.readouterr()
    assert output == "Hello, World!\n"