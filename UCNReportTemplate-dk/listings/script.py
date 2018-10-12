def test(test):
    return test*2
    
def tokenize(text):
    'Accept a string, return list of words without punctuation or stopwords'

    # lowercase everything
    text = text.lower()
    
    # remove punctuation (\W matches any non-alphanumeric character)
    text = re.sub("\W", " ", text)
    
    # return list of words, without stopwords 
    droplist = stopwords.words('english')
    
    return [word for word in text.split() if word not in droplist]