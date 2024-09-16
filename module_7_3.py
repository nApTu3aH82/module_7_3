import io
from pprint import pprint


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        char_list = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for file_name in self.file_names:
            with open(file_name) as file:
                str_for_wrt = ''
                for line in file:
                    new_string = ''
                    line = line.lower()
                    for char in line:
                        if char not in char_list:
                            new_string += char
                    str_for_wrt += new_string + ' '
                str_for_wrt = str_for_wrt.split()
                # print(str_for_wrt)
                all_words[f'{file_name}'] = str_for_wrt
        return all_words

    def find(self, word):
        self.word = word
        all_words2 = finder2.get_all_words()
        find_list = {}
        for file_name, file_text in all_words2.items():
            count = 0
            word_bool = False
            for find_word in file_text:
                if word.lower() != find_word.lower():
                    count += 1
                else:
                    count += 1
                    word_bool = True
                    break
            if word_bool == True:
                find_list[f'{file_name}'] = count
        if find_list != {}:
            return find_list
        else:
            return "Искомый текст не найден"

    def count(self, word):
        self.word = word
        all_words2 = finder2.get_all_words()
        count_word = {}
        for file_name, file_text in all_words2.items():
            count = 0
            for find_word in file_text:
                if word.lower() == find_word.lower():
                    count += 1
            count_word[f'{file_name}'] = count
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
