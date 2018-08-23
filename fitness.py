from Frequency import english_frequency, count_occurences, count_total

english_2words = ['OF', 'TO', 'IN', 'IS', 'IT']
english_3words = ['THE', 'AND', 'FOR', 'WAS', 'HIS']
double_letters = ['L', 'E', 'S', 'O', 'T']


#The coeffecient of determination, or r^2
def frequency_cod(text):
    occurences = count_occurences(text)
    total = count_total(occurences, [])



def text_fitness(text):
    fitness = 0
    for word in english_2words + english_3words:
        fitness += text.count(word)
    return fitness/len(text)

