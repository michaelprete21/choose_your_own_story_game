
print(""""
WARRIORS QUEST: Choose your own story




 _         | |
| | _______| |---------------------------------------------
|:-)_______|==[]============================================>
|_|        | |---------------------------------------------/
           |_|

 _         | |
| | _______| |---------------------------------------------
|:-)_______|==[]============================================>
|_|        | |---------------------------------------------
           |_|


 _         | |
| | _______| |---------------------------------------------
|:-)_______|==[]============================================>
|_|        | |---------------------------------------------
           |_|



""")

print("Welcome to Warriors Quest: Choose your own story!")
print("Your mission is to explore the wilds and acquire treasure.")

while True:

    decision = input("A group of bandits have stolen from the nearby \n"
                       "villagers, and you have accepted a quest to acquire a \n"
                       "widows stolen belongings. While tracking the bandits "
                     "you\n come accross two paths that they may have taken. "
                     "On "
                     "the\n right, is a large cave and on the left is a old "
                     "rickety bridge. Do you turn left or right?\n").lower()

    if decision == 'left':
        print("You make your way on to the rickety old bridge. While halfway\n "
              "over the bridge you hear a loud crack as the ropes holding\n "
              "the bridge up snap.  You plummet to your death. Game over.\n ")
        cont = input("Would you like to try again? yes or no\n").lower()
        if cont == "yes":
            print("\n")
            continue
        else:
            break
    else:
        decision = input("With your torch lit you go deeper and deeper into "
                         "the cave. After several minutes of traversing the "
                         "cave you come upon a large underground pool of "
                         "water. Do you swim or wait by the pool.")
        if decision == 'swim':
            print("You set your torch on the bank of the lake, and slowly "
                  "wade into the deep and cool water. You begin to "
                  "swim, squinting your eyes in the inky darkness. You feel "
                  "something brush against your leg. Assuming it must be a "
                  "small fish or your own imagination, you continue onwards. "
                  "After a few minutes you feel a sharp pain in your side. "
                  "You realize your are being bitten by a large beast. Before you "
                  "can react you are drug down into the water. You struggle "
                  "but you are unable to free yourself. You are never seen "
                  "again. Game over.")
            cont = input("Would you like to try again? yes or no\n").lower()
            if cont == "yes":
                print("\n")
                continue
            else:
                break
        else:
            decision = input("After waiting for a few minutes you hear the "
                             "sound of voices across the lake. You quietly "
                             "douse your flame and wait in the shadows. \n "
                             "After a few minutes a boat comes into view lit "
                             "by a torch. There are several bandits on the "
                             "boat. \n Do you attack the bandits, or seek to "
                             "hide in the shadows? Attack or hide?").lower()
            if decision == "attack":
                cont = input("You draw your sword and let out a loud roar. You "
                      "charge towards the group of bandits and slip on a\n "
                      "small rock. You fall flat on your face, and the "
                      "bandits make quick work of you. \n Would you like to "
                      "coninue? Yes or no?").lower()
                if cont == 'yes':
                    print("\n")
                    continue
                else:
                    break
            else:
                decision = input("You wait quietly in the shadows for the " \
                                "group to pass. After the group passes you go \n"
                                 "the boat and slowly paddle your way " \
                                "out\n into the waters. After a few minutes, you come to the \n"
                                "other side of the lake. There are three treasure chests " \
                                "before you. One blue, one red, and one yellow. What do you "
                                "\n choose, red, white or yellow?").lower()
                if decision == 'red':
                    print("The chest is a trap. It explodes and you die. Game over."
                          "\n Would you like to coninue? Yes or no?")
                    break

                elif decision == 'blue':
                    print("The chest is a trip. It explodes and you die. "
                              "Game over.")
                    break
                else:
                    print("You have chosen the right chest. You acquire "
                              "the villagers belongings, make your way back "
                              "across the lake, and return to the village to "
                              "be declared a hero.")
                    break










