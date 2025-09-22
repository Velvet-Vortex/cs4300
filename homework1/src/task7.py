"""
Task 7: Package Management in DevEdu
Use pip package manager to add a Python package of your choice to your project (e.g., requests,
numpy, matplotlib). Create a new file named task7.py and write a Python script that demonstrates
how to use the chosen package to perform a specific task or function. Implement pytest test cases
to verify the correctness of your code when using the package
"""

from textblob import TextBlob

def get_text_sentiment():
    """
    Uses textblob to find the polarity of an inputted text
    """

    # Get the sentiment analysis from TextBlob
    text = input("Enter the text to analyze its sentiment: ")
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    print("\nPolarity:", polarity)
    
    # Determine whether the polarity is positive and negative, then print the results
    if (polarity > 0):
        print("The text is POSITIVE\n")
    elif (polarity < 0):
        print("The text is NEGATIVE\n")
    else:
        print("The text is NEUTRAL\n")

if __name__ == '__main__':
    get_text_sentiment()