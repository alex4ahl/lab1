import wordfreq
def run_tests():
    document = ['"Här är BAJEN! Sköna BAJEN, sjung för HAMMARBY! Här är BAJEN, vafan är ni? Vill ni va som HAMMARBY? Störst och flest det vet', 
                'alla om, glasen höjs och så ekar vår sång! Här är BAJEN, vafan är ni, VI ÄR HAMMARBY!!!" Sade de mest visa folkgrupper från söder.', 
                " "]

    tokens = wordfreq.tokenize(document)
    print("Tokens: ",   tokens)

    print("")

    stopWords = ['är', 'de', 'heja', '!', "här", "sjung", "vafan", "vill", "och", "vet", "vår", "ni", "?", "va", "som", "sade", "de", '"', "för" , ",", ".", "vi", "visa", "mest", "om", "alla", "det", "så", "från"]
    word_count = wordfreq.countWords(tokens, stopWords)

    #print("Word count without stopwords: ")
    #wordfreq.countWords(tokens, stopWords)

    print ("")

    print("Top 5 words:")
    wordfreq.printTopMost(word_count, n=5)


run_tests()