import db as db

def start_game(user_id):
    db.insert_game(user_id)

def check_is_playing_game(user_id):
    return db.user_play_game(user_id)

def check_number(user_id, first, second, third, fourth):
    count_A = 0
    count_B = 0
    answer_list = db.get_game_answer(user_id).split('')

    if first == answer_list[0]:
        count_A += 1
    elif first in answer_list:
        count_B += 1
    if second == answer_list[1]:
        count_A += 1
    elif second in answer_list:
        count_B += 1
    if third == answer_list[2]:
        count_A += 1
    elif third in answer_list:
        count_B += 1
    if fourth == answer_list[3]:
        count_A += 1
    elif fourth in answer_list:
        count_B += 1

    return '%dA%dB' % (count_A, count_B)
