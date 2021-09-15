import pandas as pd

tags = pd.read_csv('tags.csv')

categories = ['HardwareAndSoftware', 'Hobbies', 'Furnurure',
              'Shops', 'Food', 'Restaraunts', 'Transactions',
              'Transportation', 'Entertainment', 'TaxesAndFines',
              'Services', 'Subscriptions', 'Hotels', 'MoneySaveAndInvesting',
              'Education', 'Clothes', 'Health', 'Auto']

ans = ['' for _ in range(len(tags.tags))]
tags['Markdown'] = ans
#
# for i, tag in enumerate(tags.tags):
#     print(f'\n======== {tag} ========')
#     for i in range(len(categories)):
#         print(f'{i + 1}){categories[i]}')
#     print('0)Other')
#
#     while True:
#         try:
#             n = int(input())
#             if n > len(categories):
#                 print('Wrong nnumber')
#             else:
#                 break
#         except Exception as e:
#             print(e.args)
#
#     if n == 0:
#         print('Enter new category:')
#         new_category = input()
#         categories.append(new_category)
#         ans.append(categories[-1])
#         tags.loc[i, 'Markdown'] = categories[-1]
#
#     ans.append(categories[n - 1])
#     tags.loc[i, 'Markdown'] = categories[n - 1]
#
#
# tags['Markdown'] = ans
# tags.to_csv('tags.csv')
#
# tags = pd.read_csv('tags.csv')
# print(tags['Markdown'])

answers = []

last_idx = 12

with open('output.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if not (')' in line):
            if line != '':
                if line[0].isdigit():
                    answers.append(line)

print(len(answers))

markdown = []

for answer in answers:
    try:
        answer = int(answer)
        if answer == 0:
            md = categories[last_idx]
            last_idx += 1
        else:
            md = categories[answer - 1]

        markdown.append(md)
    except Exception as e:
        print(e.args)

print(markdown)

tags['Markdown'] = markdown
tags.to_csv('tags.csv')