"""
1. Clear the story of punctuation.
2. Create var story_words: list with words from story
3. Create var story_list: list with sentences from story
4. 2 vars that has Number of elements in story_words & story_list
5. Create var full_text_list: list and save there story_title and story_title
6. Select 3 list methods and use them with story_words
"""

story_title = 'THE BOY WHO LIVED'
story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were \
        proud to say that they were perfectly normal, thank \
        you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t \
        hold with such nonsense. \
        Mr. Dursley was the director of a fi rm called Grunnings, which \
        made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin \
        and blonde and had nearly twice the usual amount of neck, which \
        came in very useful as she spent so much of her time craning over \
        garden fences, spying on the neighbors. The Dursleys had a small \
        son called Dudley and in their opinion there was no fi ner boy \
        anywhere."

# 1
one_line = "".join([x for x in story if x.isalpha() or x.isspace() or x == "\n"])
story = one_line.replace("Mr", "Mr.").replace("Mrs", "Mrs.")
while "  " in story:
	story = story.replace("  ", " ")
print(story)

# 2
story_words = story.split(" ")

# 3 - Unreachable
story_list = list()

# 4 - 50 Ok / 50 Unreachable
words_number = len(story_words)

# 5 - Unreachable

# 6 - Waiting to clarify the task, not shore that's what was meant

# 7 - Done
res = story_words.pop(0)
story_words.append(res)
story_words.clear()