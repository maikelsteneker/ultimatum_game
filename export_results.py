from django.core.management import setup_environ
from django.forms.models import model_to_dict

from ultimatum_game import settings
setup_environ(settings)

from game.models import *
import csv
import operator

filename = 'output.csv' # the output file
blacklist = {'4b058c485b5911e397370050562b0074', 'a541dbe45b5911e397370050562b0074', '569120c25de311e397370050562b0074', '9aa2453a635511e397370050562b0074',} # blacklisted mturk keys that should not be exported
int_vars = {'age', 'hours_a_day_you_spend_behind_a_computer',} # variables to treat as integer
renamed_vars = {#'id': 'round',
                'time_elapsed': 'round_time',} # renamed variables
# An entry x:y in this dictionary will rename the key (column) x to y.
# We rename id to round, since it's not clear what the id refers to.
# We rename time_elapsed for similar reasons; it's not clear that this refers to the time of a single round.

table = []
rounds = (r for r in Round.objects.all() if r.player.mturk_key != '0' and r.player.mturk_key not in blacklist) # all the players that finished the questionnaire
rounds = sorted(rounds, key=operator.attrgetter('datetime')) # sort by datetime
player_round = {p: 0 for p in Player.objects.all()} # dictionary that looks at how many rounds we already saw so far for each player

for r in rounds:
    dict = model_to_dict(r) # form a dictionary from the information in the round object
    #r_id = dict['id'] # temporarily store the round id in case an update replaces it
    dict.update(model_to_dict(r.player)) # add information from the player to the dict
    #dict['id'] = r_id # restore the round id value
    for q in Question.objects.all():
        dict[q.text] = Answer.objects.get(question=q, player=r.player).option.text # use the question text as a key and the chosen option text as a value
    for key in renamed_vars:
        old = key
        new = renamed_vars[key]
        dict[new] = dict.pop(old) # rename key old to new
    for key in int_vars:
        try:
            dict[key] = int(dict[key])
        except ValueError:
            dict.pop(key, None)
    player_round[r.player] += 1
    dict['round_number'] = player_round[r.player]
    table.append(dict)

question_keys = sorted(table[0].keys())[0:38] # very ugly way to select just the questions; we want those last in the keys list
keys = ['player', 'round_number', 'opponent', 'opponent_kind', 'accepted', 'amount_offered', 'is_intentional', 'start_time', 'instructions_time', 'round_time', 'questionnaire_time', 'age', 'hours_a_day_you_spend_behind_a_computer', 'nationality',] # the keys, in order, that will be used in the csv file
keys.extend(question_keys)
# Export dictionary to csv.
f = open(filename, 'wb')
dict_writer = csv.DictWriter(f, keys, extrasaction='ignore')
dict_writer.writer.writerow(keys)
dict_writer.writerows(table)
f.close()
