from game_utils import solve_riddle, end_game, move_player

def greeting():
    print("Willkommen! Du kannst dich mit den Befehlen 'Norden, Süden, Westen, Osten' bewegen.\nDu wirst auch auf Rätsel stoßen!")

def main():
    greeting()
    rooms = [
    {'name': 'Entrance',
         'description': 'Du wachst in einem dunklen Raum auf.',
         'riddle': {
             'question': 'Was wird bis zum maximalen Volumen gefüllt und bleibt doch leer?',
             'answer': 'Luftballon'
         },
         'Norden': 1},
        
        {'name': 'GreatHall',
         'description': 'Du stehst in einer großen Halle und siehst überall interessante Dinge.',
         'riddle': {
             'question': 'Was ist so zerbrechlich, dass selbst das Aussprechen der gesuchten Sache, diese komplett zerstören würde?',
             'answer': 'Die Stille'
         },
         'Süden': 0, 'Osten': 2},
        
        {'name': 'Library',
         'description': 'Du bist in einer alten Bibliothek voller verstaubter Bücher.',
         'riddle': {
             'question': 'Ich habe Schlüssel, aber keine Türen. Ich habe Platz, aber keine Räume. Du kannst mich betreten, aber nicht hinausgehen. Was bin ich?',
             'answer': 'Eine Tastatur'
         },
         'Westen': 1, 'Osten': 3},
        
        {'name': 'Garden',
         'description': 'Du stehst in einem wunderschönen Garten mit bunten Blumen.',
         'riddle': {
             'question': 'Ich lebe, ohne zu atmen, kühle ohne zu frieren, trinke ohne zu durstig zu sein, und esse, ohne hungrig zu sein. Was bin ich?',
             'answer': 'Feuer'
         },
         'Westen': 2, 'Norden': 4},
        
        {'name': 'Tower',
         'description': 'Du bist in einem hohen Turm mit Aussicht auf das gesamte Königreich.',
         'riddle': {
             'question': 'Ich werde von vielen benutzt, aber keiner hält mich fest. Was bin ich?',
             'answer': 'Ein Name'
         },
         'Süden': 3, 'Osten': 5},
        
        {'name': 'Armory',
         'description': 'Du befindest dich in einer alten Waffenkammer voller Rüstungen und Schwerter.',
         'riddle': {
             'question': 'Ich bin immer hungrig, muss ständig gefüttert werden. Alles, was ich berühre, wird rot. Was bin ich?',
             'answer': 'Feuer'
         },
         'Westen': 4, 'Norden': 6},
        
        {'name': 'Dungeon',
         'description': 'Du bist in einem dunklen Kerker.',
         'riddle': {
             'question': 'Ich bin nicht lebendig, aber ich wachse. Ich habe keine Lungen, aber ich atme. Was bin ich?',
             'answer': 'Ein Schatten'
         },
         'Süden': 5, 'Osten': 7},
        
        {'name': 'TreasureRoom',
         'description': 'Du stehst vor einem glänzenden Schatzraum voller Gold und Edelsteine.',
         'riddle': {
             'question': 'Was gehört dir, aber wird fast immer von anderen benutzt?',
             'answer': 'Dein Name'
         },
         'Westen': 6, 'Norden': 8},
        
        {'name': 'KingsHall',
         'description': 'Du bist in der Halle des Königs gelandet. Löse das letzte Rätsel!',
         'riddle': {
             'question': 'Ich kann gebrochen werden, ohne dass mich jemand berührt oder dass ich überhaupt anwesend bin! Und doch kann mich jeder geben! Was bin ich?',
             'answer': 'Ein Versprechen'
         },
         'Süden': 7}
    ]
    current_room = 0
    while current_room < len(rooms):
        print(f"Du bist im Raum: {rooms[current_room]['name']}")
        print(rooms[current_room]['description'])

        if solve_riddle(rooms[current_room]['riddle']):
            print("Richtig! Du darfst weitergehen.\n")
        else:
            print("Falsch! Versuche es erneut!")
            continue

        direction = input("In welche Richtung möchtest du gehen? (Norden, Süden, Westen, Osten): ").strip().capitalize()
        current_room = move_player(current_room, direction, rooms)

    end_game()


if __name__ == '__main__':
    main()
    
