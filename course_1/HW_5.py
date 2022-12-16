"""
This task is very weird, because many tasks are unreachable. Couch doesn't want to change it.
Hardcode.

1. Clear the story of punctuation.
2. Create var story_words: list with words from story
3. Create var story_list: list with sentences from story
4. 2 vars that has Number of elements in story_words & story_list
5. Add story_title to story_list and save it to new var full_text_list
6. Select 3 list methods and use them with story_words
"""

story_title = 'THE BOY WHO LIVED'
story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were \
        proud to say that they were perfectly normal, thank \
        you very much. They were the last people you’d expect to be involved in anything strange or mysterious, \
        because they just didn’t hold with such nonsense. \
        Mr. Dursley was the director of a fi rm called Grunnings, which \
        made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. \
        Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which \
        came in very useful as she spent so much of her time craning over \
        garden fences, spying on the neighbors. The Dursleys had a small \
        son called Dudley and in their opinion there was no fi ner boy \
        anywhere."


def punctuation_handler(text, dict_) -> str:
	"""Returns back required symbols and deletes unnecessary"""
	for k, v in dict_.items():
			text = text.replace(k, v)
	return text



def delete_punctuation(text: str) -> str:
	return "".join([x for x in text if x.isalpha() or x.isspace()])


delete_dot = {
	"Mrs. ": "Mrs ",
	"Mr. ": "Mr "
}


return_dot = {
	"Mrs ": "Mrs. ",
	"Mr ": "Mr. "
}

# 0 - Delete unnecessary spaces
while "  " in story:
	story = story.replace("  ", " ")

# 1
one_line = delete_punctuation(story)
story_no_punctuation = punctuation_handler(one_line, return_dot)
print(story_no_punctuation)

# 2
story_words = story_no_punctuation.split(" ")
print(story_words)

# 3
raw_story = punctuation_handler(story, delete_dot)		# delete DOTs from Mr & Mrs
story_list_punctuation = raw_story.split(".")			# split by dot
story_list_no_punctuation = [delete_punctuation(x.strip()) for x in story_list_punctuation if x]	# remove punctuation
story_list = [punctuation_handler(x, return_dot) for x in story_list_no_punctuation]		 # return DOTs to Mr and Mrs
print(story_list)										# Done

# 4
number_of_words = len(story_words)
number_of_sentences = len(story_list)
print(number_of_words, number_of_sentences, sep=" - ")

# 5
story_list.append(story_title)			# add
full_text_list = story_list.copy()		# save to new var

# 6
without_upper = full_text_list.pop()	# delete title

# 7 - Done
res = story_words.pop(0)
story_words.append(res)
story_words.clear()