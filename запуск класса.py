from KDT import AnonymousSurvey
#Определение вопроса с созданием экземпляра AnonymousSurvey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Вывод вопроса и сохранения ответа
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Вывод результата опроса
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()