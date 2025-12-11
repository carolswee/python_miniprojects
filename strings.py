# strings
from collections import Counter

hobby=input('Please write about your hobby:')
letter_count=len(hobby.replace(' ',''))
print(letter_count)

reverse_sentence=hobby[::-1]
print(reverse_sentence)

word_count=len(hobby.split())
print(word_count)

letter_counts=Counter(hobby.split())
max_letter_count=letter_counts.most_common(1)
print('most repeated word:',(max_letter_count))
