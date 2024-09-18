from collections import Counter

sample_string = 'reuiertyukjmnbvdaagfgvxwd'
char_count=Counter(sample_string)

repeated_char = {char:count for char,count in char_count.items() if count>1}
print("Repeated charcters and theri counts:",repeated_char)