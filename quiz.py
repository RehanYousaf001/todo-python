import json

with open('quiz.json', 'r') as file:
    content = file.read()
    # print(content)

json_data = json.loads(content)
# print(json_data)
answer_data = []
for item in json_data:
    print(item['question_text'])
    for i, alternative in enumerate(item['alternatives']):
        print(i + 1, '-', alternative)

    answer = int(input('Select the correct answer: '))
    if answer == item['correct_answer']:
        answer_data.append(True)
    else:
        answer_data.append(False)

if all(answer_data):
    print('Correct answer')
else:
    print('Incorrect answer')

