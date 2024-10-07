def solve_riddle(riddle):
    print("Rätsel:", riddle['question'])
    answer = input("Deine Antwort: ").strip()
    return answer.lower() == riddle['answer'].lower()

def end_game():
    print("Du hast gewonnen!")
    quit()

def move_player(current_room, direction, rooms):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("Du kannst nicht in diese Richtung!")
        return current_room