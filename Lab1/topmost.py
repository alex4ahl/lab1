import wordfreq
import sys
import re
import urllib.request

#"https://www.gutenberg.org/cache/epub/164/pg164.txt" = sys.arg[2]

response = urllib.request.urlopen('https://www.gutenberg.org/cache/epub/164/pg164.txt')
lines = response.read().decode("utf8").splitlines()

article1 = open('article2.txt', encoding = 'utf-8')
contents_article1 = article1.read()
article_into_list = re.sub(r'\n', ' ',  contents_article1).strip().split(".") # För att nyttja strip() använde jag mig av modulen re.sub() som erbjuder 
# att man kan ha större överblick över ersättning av mönster i en sträng, de är tre huvudsakliga arg: 
# 1: Mönstret du vill ersätta, 2: Ersättningssträngen (vad du skall ersätta (1) med) och 3: Namnet på den sträng som detta skall verka på. 
#Sedan läggs .strip() vilket var obligatoriskt i labben, denna gör så att (' ', det 2:a argumentet i re.sub()) strippas ur strängen för att
#till sist nyttja .split(".") vilket gör att strängen "splittas" vid varje uppkommande '.'. Exempelvis: text = "Hej. Jag heter Alex. Alex Ahl." 
# \n sentance = text.split('.') \n print(sentance). Detta kommer att ge output: ['Hej', ' Jag heter Alex', ' Alex Ahl', '']

article1.close()

eng_stopWords = open('eng_stopwords.txt')
contents_eng_stopWords = eng_stopWords.read()
stopWords_into_list =re.sub(r'\n', ' ',  contents_eng_stopWords).strip().split(".")
eng_stopWords.close

def main():
    tokens = wordfreq.tokenize(article_into_list)
    #print("Tokens: ",   tokens)
    current_stopwords = wordfreq.tokenize(stopWords_into_list)
    #print("Current stopwords: ", current_stopwords)
    word_count = wordfreq.countWords(tokens, current_stopwords)

    n = int(input("Enter an integer of the amount of top most 'n' words: "))
    print("Top "+str(n)+" words:")
    wordfreq.printTopMost(word_count, n)

main()
