def tokenize(lines):
    words = []
    
    for line in lines:
        start = 0
        while start < len(line):

            while start < len(line) and line[start].isspace(): # För att bli av med blanksteg
                start += 1
            
            if start >= len(line):
                break
            
            if line[start].isalpha(): # Kontroll om det är ett ord
                end = start
                while end < len(line) and line[end].isalpha():
                    end += 1
                words.append(line[start:end].lower())
                start = end 

            #Får se om jag behåller elif nedan...
            #elif line[start].isdigit() or line[start] == ',':  # kontrollera om det är en siffra med en symbol, t.ex 500,000 som inte menas som '500', ',' och 000, utan detta skall betyda 500000
              #  end = start
              #  while end < len(line) and (line[end].isdigit() or line[end] == ','):
              #      end += 1
              #  number = line[start:end].replace(',', '') # tar bort kommatecknen för att siffran skall stämma
              #  words.append(number)  # Lägger till den nya siffran
              #  start = end

            elif line[start].isdigit(): #Kontroll om det är en siffra
                end = start
                while end < len(line) and line[end].isdigit():
                    end += 1
                words.append(line[start:end])
                start = end
            
            else: #Om varken en siffra eller ord är det en symbol
                words.append(line[start])
                start += 1
   # wordsLenght = len(words)
    #for i in range(wordsLenght):
    #    word = words[i]
    #    print (word)
    return words


def countWords(words, stopWords):
    frequencies = {}

    # Loopa genom alla word[] i words-listan
    for word in words:  # word är nu en sträng och inte en lista
        if word not in stopWords and word.isalpha():
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1

    wordLenght = len(words)
    #for word, count in list(frequencies.items())[:wordLenght]: #frequencies.items() gör så att vi får
    # tillgång till både keys (words) och dess valör (counts) i en dictionary, då kan man göra att den 
    # printar dictionaryn mycke finare!
        #print(f'Word: {word}'.ljust(20) + f'Times used: {count}'.rjust(5))
                
    return frequencies

def printTopMost(frequencies, n):
    sorted_words = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    
    for word, count in sorted_words[:n]:
        print(f'{word}:'.ljust(20) + f'{count}'.rjust(5))
    return sorted_words