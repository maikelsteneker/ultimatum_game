from django.core.management import setup_environ

from ultimatum_game import settings
setup_environ(settings)
from game.models import *

Question.objects.all().delete()
Option.objects.all().delete()

#q = Question(text='test question')
#q.save()
#o = Option(question=q, text='test answer')
#o.save()

def add(questions, options):
    for question in questions:
        q = Question(text=question)
        q.save()
        for option in options:
            o = Option(question=q, text=option)
            o.save()

first_batch_questions = ['Overall, do you believe the opponents you encountered were capable of feeling emotions?', 'Overall, do you believe the opponents you encountered were capable of having intentions?', 'Overall, do you believe the opponents you encountered have consciousness?', 'Overall, do you believe the opponents you encountered have minds of their own?', 'Overall, do you believe the opponents you encountered have free will?',]

first_batch_options = ['Extremely disagree', 'Moderately disagree', 'Slightly disagree', 'Neither disagree nor agree', 'Slightly agree', 'Moderately agree', 'Extremely agree']

add(first_batch_questions, first_batch_options)

second_batch_questions = ['The opponents understand a language', 'The opponents understand the moral dilemma.', 'The opponents recognize others\' emotions.', 'The opponents are ambitious.', 'The opponents are purposeful.', 'The opponents can feel unhappy about the dilemma.', 'The opponents are aware of its physical environment.', 'The opponents are aware of themselves.', 'The opponents can estimate distances.', 'The opponents can anticipate events in its physical environment.', 'The opponents can be angry.', 'The opponents can understand others\' emotions.', 'The opponents can walk.', 'The opponents can pick up objects.', 'The opponents can perceive objects.', 'The opponents can talk.', 'The opponents can solve riddles.', 'The opponents can do math.', 'The opponents can jump.',]

second_batch_options = ['Agree', 'Disagree']

add(second_batch_questions, second_batch_options)

third_batch_questions = ['Overall, what is your attitude toward the opponents you encountered in this study?', 'Overall, how likeable did you find your opponents?', 'Overall, how attractive did you find the pictures of your opponents?', 'Overall, to what extent did you feel opponents 1 to 4 were responsible for the offers they made?', 'Overall, to what extent did you feel opponents 5 to 8 were responsible for the offers they made?', 'How noticeable were the differences between the opponents you encountered?',]

#TODO: replace by sensible options for each question
third_batch_options = [['Q1O1', 'Q1O2'],
                       ['Q2O1', 'Q2O2'],
                       ['etc'],
                       ['etc'],
                       ['etc'],
                       ['etc'],
                      ]

for x in range(len(third_batch_questions)):
    add(third_batch_questions[x:x+1], third_batch_options[x])

fourth_batch_questions = ['Do you feel like your knowledge of the opponents\' appearance influenced your decisions in the game?', 'How motivated were you to earn as many Money Units as possible in the game?', 'Do you feel like emotions or other non-financial motivations influence your decisions in the game?',]

#TODO: replace by sensible options for each question
fourth_batch_options = [['Q1O1', 'Q1O2'],
                       ['Q2O1', 'Q2O2'],
                       ['etc'],
                      ]

for x in range(len(fourth_batch_questions)):
    add(fourth_batch_questions[x:x+1], fourth_batch_options[x])

fifth_batch_questions = ['On average, how many hours a day do you spend interacting with devices such as PC\'s, laptops, tablets and smart phones?', 'Do you have any personal experience with robots (including e.g. robotic toys like Furby and robotic appliances like vacuum cleaners or lawn mowers)?', 'The game you played in this experiment is called the \'Ultimatum Game\'. Had you ever heard of or played this game before?','Please indicate your gender.','Please indicate your age.','Please indicate your nationality.', 'Please indicate how religious you are.', 'Please indicate how spiritual you are.']

#TODO: replace by sensible options for each question
fifth_batch_options = [['Q1O1', 'Q1O2'],
                       ['Q2O1', 'Q2O2'],
                       ['etc'],
                       ['etc'],
                       ['etc'],
                       ['etc'],
                       ['etc'],
                       ['etc'],
                      ]

for x in range(len(fifth_batch_questions)):
    add(fifth_batch_questions[x:x+1], fifth_batch_options[x])
