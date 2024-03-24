print("\n1. Product Review Analysis\n")
""""
Task 1: Keyword Highlighter
Write a program that searches through a series of product reviews for keywords
such as "good", "excellent", "bad", "poor", and "average". 
Print out each review with the keywords in uppercase so they stand out.
"""
def uppercase_keywords(review):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    cap_keywords = [keyword[0].upper()+keyword[1:len(keyword)] for keyword in keywords]
    for keyword in keywords + cap_keywords:
        review = review.replace(keyword, keyword.upper())
    return review

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it.",
    "TEST: Bad. Good. Excellent"
]
for review in reviews:
    print(uppercase_keywords(review))

print("\nTask 2: Sentiment Tally\n")
"""
Develop a function that tallies the number of positive and negative words in each review. 
Use a predefined list of positive and negative words to check against. 
The function should return the count of positive and negative words for each review.
"""
def sentiment_tally(review):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    pos_cnt = neg_cnt = 0

    for word in review.split():
        word = word.lower().strip(".")
        if word in positive_words:
            pos_cnt += 1
        if word in negative_words:
            neg_cnt += 1
    return pos_cnt, neg_cnt

for review in reviews:
    pos_words, neg_words = sentiment_tally(review)
    print("Review:", review)
    print(" - Positive Words:", pos_words," | Negative Words:", neg_words,"\n")

print("\nTask 3: Review Summary\n")
"""
Implement a script that takes the first 30 characters of a review and appends "…" 
to create a summary. Ensure that the summary does not cut off in the middle of a word.
"""
def summarize(review, max_length=30):
    words = review.split()
    summary = []
    for word in words:
        if len(" ".join(summary + [word])) <= max_length:
            summary.append(word)
        else:
            break
    return " ".join(summary) + "..."

for review in reviews:
    print(summarize(review))
print()