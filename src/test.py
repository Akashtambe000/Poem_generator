def split_lyrics_file(text_file):
	text = open(text_file, encoding='utf-8').read()
	text = text.split("\n")
	while "" in text:
		text.remove("")
	return text


def syllables(line):
    count = 0
    for word in line.split(" "):
        vowels = 'aeiouy'
        word = word.lower().strip(".:;?!")
        if word[0] in vowels:
            count +=1
        for index in range(1,len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count +=1
        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count+=1
        if count == 0:
            count +=1
    return count


text_file = "_final_poem_ml_scrap.txt"
bars = split_lyrics_file(text_file)
i = 1
for line in bars:
    print(i,line.split(" "))
    count = syllables(line)
    i += 1 