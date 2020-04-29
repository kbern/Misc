# Kate Bernstein
# CS 111

import math


def clean_text(txt):
    txt = txt.lower()
    txt = txt.replace('.','')
    txt = txt.replace(',','')
    txt = txt.replace('?','')
    txt = txt.replace('!','')
    txt = txt.replace(';','')
    return txt


def sample_file_write(filename):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.

    
        
def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)




def stem(s):
    if s[-1] == 's' and len(s) > 4:
        s = s[:-1]              #plural cases                                                 
    if s[-3:] == 'ing' and len(s) > 5:
        if s[-4] == s[-5]:
            if s[-4] == '1':
                s = s[:-3]      #cases such as 'killing'
            else:
                s = s[:-4]      #cases such as 'stemming'
        else:
            s = s[:-3]          #cases such as 'playing'
    elif s[-3] == 'ier' and len(s) > 4:
        s = s[:-3] + 'y'        #cases such as 'partier'
    elif s[-2:] == 'er' and len(s) > 4:
        if s[-3] == s[-4]:      
            s = s[:-3]          #cases such as 'spammer'
        else:
            s = s[:-2]          #cases such as 'reader'
    elif s[-3:] == 'ies' and len(s) > 5:
        s = s[:-3] + 'y'        #cases such as 'parties'
                    


def compare_dictionaries(d1, d2):
    score = 0
    total = 0

    for i in d1:
        total += d1[i]
    for j in d1:
        if j in d2:
            score += d2[j]*math.log(d1[j]/total)
        else:
            score += d2[j]*math.log(0.5/total)
        return score
    
        
class TextModel:

    def __init__(self, model_name):
        self.name = model_name
        self.words = {}
        self.word_lengths = {}

    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths:  ' + str(len(self.word_lengths))   
        return s

    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model.
        """
        word_list = clean_text(s)
        word_list = word_list.split(' ')


        # Template for updating the words dictionary.
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            
                    
        for p in word_list:
            if len(p) not in self.word_lengths:
                self.word_lengths[len(p)] = 1
            else:
                self.word_lengths[len(p)] += 1
                
        for g in word_list:
            if len(g) not in self.stems:
                self.stems[len(g)] = 1
            else:
                self.stems[len(g)] += 1
                
        for f in word_list:
            if len(f) not in self.sentence_lengths:
                self.sentence_lengths[len(f)] = 1
            else:
                self.sentence_lengths[len(f)] += 1
                
        for h in word_list:
            if len(h) not in self.word_frequencies:
                self.word_frequencies[len(h)] = 1
            else:
                self.word_frequencies[len(h)] += 1
            

    def add_file(self, filename):
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        self.add_string(f)

    def save_model(self):
        d = self.words
        f = open(self.name + '_' + 'words', 'w')
        f.write(str(d)) 
        f.close()
        
        g = self.word_lengths
        h = open(self.name + '_' + 'word_lengths', 'w')
        h.write(str(g))
        h.close()

        a = self.stems
        b = open(self.name + '_' + 'stems', 'w')
        b.write(str(a))
        b.close()

        c = self.sentence_lengths
        e = open(self.name + '_' + 'sentence_lengths', 'w')
        e.write(str(c))
        e.close()

        m = self.word_frequencies
        l = open(self.name + '_' + 'word_frequencies', 'w')
        l.write(str(m))
        l.close()


    def read_model(self):

        f = open(self.name + '_' + 'words', 'r')    # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        d = dict(eval(d_str))      # Convert the string to a dictionary.
        self.words = d
        
        g = open(self.name + '_' + 'word_lengths', 'r')    # Open for reading.
        h_str = g.read()           # Read in a string that represents a dict.
        g.close()

        h = dict(eval(h_str))
        self.word_lengths = h

        a = open(self.name + '_' + 'stems', 'r')    # Open for reading.
        b_str = a.read()           # Read in a string that represents a dict.
        a.close()

        b = dict(eval(b_str))
        self.stems = b

        c = open(self.name + '_' + 'sentence_lengths', 'r')    # Open for reading.
        e_str = c.read()           # Read in a string that represents a dict.
        c.close()

        e = dict(eval(e_str))
        self.sentence_lengths = e

        m = open(self.name + '_' + 'word_frequencies', 'r')    # Open for reading.
        l_str = m.read()           # Read in a string that represents a dict.
        m.close()

        l = dict(eval(l_str))
        self.word_lengths = l

        s = 'text model name: ' + self.name + '\n'
        s += 'number of words: ' + str(len(self.words)) + '\n'
        s += 'number of wordlengths: ' + str(len(self.word_lengths)) + '\n'
        s += 'number of stems: ' + str(len(self.stems)) + '\n'
        s += 'number of sentencelengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += 'number of wordfrequencies: ' + str(len(self.word_frequencies)) 




    def __init__(self, model_name):
        self.stems = {}
        self.sentence_lengths = {}
        self.word_frequncies = {}


    def add_string(self,s):

        sentences = s.replace('?','.')
        sentences = sentences.replace('!','.')
        sentences = sentences.split('.')
    
                                                 
        for a in range(len(sentences)):
            if sentences[a] != '':
                j = sentences[a].split(' ')
            if len(j) not in self.sentence_lengths:
                self.sentence_lengths[len(j)] = 1
            else:
                self.sentence_lengths[len(j)] += 1
                                                 

        common_word = ['the','be','to','of','and','a','in','that','have','i','it','for',
                     'not','on','with','he','as','you','do','at','this','but',
                   'his','by','from','they','we','say','her','she']

        word_list = clean_text(s)
        word_list = word_list.split(' ')

        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1

        for p in word_list:
            if len(p) not in self.word_lengths:
                self.word_lengths[len(p)] = 1
            else:
                self.word_lengths[len(p)] += 1


        for j in words_lengths:
            j = stem(j)
            if j not in self.stems:
                self.stems[j] = 1
            else:
                self.stems[j] += 1

        for h in word_list:
            if h in common_words:
                if h not in self.common:
                    self.common[h] = 1
                else:
                    self.common[h] += 1


    def similarity_scores(self, other):
        list = []


        word_score = compare_dictionaries(other.words, self.words)
        list.append(word_score)
        word_lengths_score = compare_dictionaries(other.words_lengths, self.words_lengths)
        list.append(word_score)               
        word_list_score = compare_dictionaries(other.words_list, self.words_list)
        list.append(word_score)
        stems_score = compare_dictionaries(other.stems, self.stems)
        list.append(word_score)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        list.append(word_score)
        word_frequencies = compare_dictionaries(other.word_frequencies,self.word_frequencies)           
        list.append(word_score)                                                
        return list


    def classify(self, source1, source2):
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ', source1.name, scores1)
        print('scores for ', source2.name, scores2)
        for i in range(len(scores1)):
            sum1 += source1(i)
        for j in range(len(scores2)):
            sum2 += source1(j)                                            
        if sum1 > sum2:
            print('mystery is more likely to have come from ' ,source1.name)
        else:
            print('mystery is more likely to have come from ' ,source2.name)
                
                                    
        
def run_tests():
    source1 = TextModel('rowling')
    source1.add_file('rowling_source_text.txt')

    source2 = TextModel('shakespeare')
    source2.add_file('shakespeare_source_text.txt')

    new1 = TextModel('wr100')
    new1.add_file('wr100_source_text.txt')
    new1.classify(source1, source2)

    new1 = TextModel('other_rowling_chapter')
    new1.add_file('other_rowling_chapter_source_text.txt')
    new1.classify(source1, source2)

    new1 = TextModel('other_shakespeare')
    new1.add_file('other_shakespeare.txt')
    new1.classify(source1, source2)

    new1 = TextModel('The_Great_Gatsby')
    new1.add_file('The_Great_Gatsby.txt')
    new1.classify(source1, source2)
    

    

            
