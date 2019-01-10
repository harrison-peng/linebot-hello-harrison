import db as db

def start_game(user_id):
    db.insert_game(user_id)

def check_is_playing_game(user_id):
    return db.user_play_game(user_id)

def check_number(user_id, first, second, third, fourth):
    count_A = 0
    count_B = 0
    answer_list = list(db.get_game_answer(user_id))
    db.add_game_count(user_id)

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

    if count_A == 4:
        count = db.get_game_count(user_id)
        db.set_game_play_false(user_id)
        if count < 10:
            return '恭喜答對囉!!!! 總共只花了%d次呢！真厲害:D' % count
        elif count >= 10 and count < 20:
            return '恭喜答對囉!!!! 總共花了%d次呢！還不錯~下次再加油哦:)' % count
        else:
            return '恭喜答對囉!!!! 總共花了%d次，可以再多努力哦><' % count
    else:
        return '%dA%dB' % (count_A, count_B)

def finish_game(user_id):
    db.set_game_play_false(user_id)
    
def give_up_game(user_id):
    answer = db.get_game_answer(user_id)
    db.set_game_play_false(user_id)
    return '答案是「%s」哦!下次再加油吧~~' % answer
