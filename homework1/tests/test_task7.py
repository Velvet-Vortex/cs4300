from src.task7 import get_text_sentiment

# Verify that with positive language, there is positive polarity
def test_positive_text(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "I really like Colorado Springs and think it's an amazing place to live.")
    get_text_sentiment()
    out, err = capsys.readouterr()
    assert "The text is POSITIVE" in out

# Verify that with negative language, there is negative polarity
def test_negative_text(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "Traffic was horrible this morning and Colorado drivers drive me insane.")
    get_text_sentiment()
    out, err = capsys.readouterr()
    assert "The text is NEGATIVE" in out

# Verify neutral statements return neutral
def test_neutral_text(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "A cat is an animal")
    get_text_sentiment()
    out, err = capsys.readouterr()
    assert "The text is NEUTRAL" in out
