import sys
import time

print("You eagerly walk into the mansion. This was your first case as a freelance investigator. At the door you are greeted by Detective Scott")
print("Thornhill. The detective points you to the three possible suspects. The mansions maid has worked with the Smith family for a number of years ")
print("and has happily served the family. The one call doctor was called by the victims family because they feared that he was ill. The grounds ")
print("keeper and hunter has worked with the family for a number of decades. The detective has been able to narrow down the suspects down to these ")
print("three, but he hasn’t been able to find the murder weapon to convict anyone. You have been called onto the scene to find the missing murder weapon (or weapons).")


name = input("What is your name: ")
print("The detective welcomes you: Hello, "+name+"! Look around the house to find the murder weapon. We're counting on you!")

def endTalk():
    print("With all this dust in the air, you begin to sneeze and wind up tripping on a bucket. Ah, ha! It was all in front of you all along!")
    time.sleep(2)
    print("You go to talk to the detective:")
    print("So, "+name+", who dunnit? The doctor (press the 1 key), the groundskeeper (press the 2 key), or the maid (press the 3 key)?")
    user_input = input()
    if user_input == "1":
        print("The doctor arrived right when the police were called onto the scene. Since the doctor could neither confirm or deny his whereabouts ")
        print("the detective added him to the suspect list. The doctor has been with the detectives nearly the entirety of his time in the mansion ")
        print("and his medical bag had every instrument accounted for. Finally realizing his error in hiring you, the detective kicks you out the ")
        print("house and threatens to arrest you for wasting his time.")
        print("")
        print("YOU LOSE!")
    elif user_input == "2":
        print("The groundskeeper had been at one of the neighbor’s houses at the time of the murder. During your investigation the neighbor confirmed ")
        print("the groundskeepers alibi. The groundskeeper does go hunting, but the missing rifle was taken by the Smith family when they went on their ")
        print("annually family hunting trip. The detective realizing how inexperienced and unreliable you are kicks you out of the house without paying ")
        print("for your services.")
        print("")
        print("YOU LOSE!")
    elif user_input == "3":
        print ("Once you accuse the maid she breaks down and admits to everything. The victim had been telling his family that she had been stealing ")
        print("money and jewelry. In actuality it had been the victim stealing his families things to pay off his gambling debts. The maid was fearful ")
        print("of losing her job so she decided to eliminate the problem.")
        print("")
        print ("The maid had been putting cleaning products inside of the victims food. The cleaning products caused the victim to vomit blood. ")
        print("The victim and his family thought that he was just very sick. The victim died of poisoning. To throw off the detectives the maid ")
        print("shot the victim with one of the rifles in the family's attic, and she stabbed the victim with a scapple like object.")
        print("")
        print("YOU WIN!")

print("Start with the kitchen (press the 1 key) or living room (press the 2 key): ")
user_input = input()
if user_input == "1":
    print("You enter the kitchen, but it doesn't smell like warm cookies like you were hoping...")

    print("Look around (press the 1 key) or have a snack? (press the 2 key)")
    user_input = input()
    if user_input == "1":
        print("You decide to take a very detailed looked through the kitchen. As you slowly look through the kitchen you notice the kitchen  ")
        print("sink is filled to the brim with dishes. The maid could have easily clean the dishes after dinner before the victim’s death.")

        print("Look for stains (press the 1 key) or leave kitchen (press the 2 key)?")
        user_input = input()
        if user_input == "1":
            print("You didn't find anything, got bored, and gave up.")
            time.sleep(2)
            sys.exit(0)

        elif user_input == "2":
            print("You walk out the kitchen into the victims office. You notice that medical supplies are scattered ")
            print(" across the desk. For some reason you get a feeling that some of the supplies are missing.")

            print("Look further (press the 1 key) or accuse the doctor (press the 2 key)?")
            user_input = input()
            if user_input == "1":
                print("You approach the table and see it was just first aid supplies...")
                endTalk()

            elif user_input == "2":
                print("The doctor arrived right when the police were called onto the scene. Since the doctor could neither confirm  ")
                print("or deny his whereabouts the detective added him to the suspect list. The doctor has been with the detectives  ")
                print("nearly the entirety of his time in the mansion and his medical bag had every instrument accounted for. Finally  ")
                print("realizing his error in hiring you, the detective kicks you out the house and threatens to arrest you for wasting his time.")
                time.sleep(2)
                sys.exit(0)

    elif user_input == "2":
        print("You haven’t eaten since the night before. You skipped breakfast. You scarf down the warm cookies and raid the  ")
        print("fridge for what little food was left in. When you finish eating you notice that you are feeling really sick.  ")
        print("You have no choice but to excuse yourself and go home.")
        time.sleep(2)
        sys.exit(0)
elif user_input == "2":
    print("You enter the living room, but it seems a bit messy...")
    print("Check behind furniture (press the 1 key) or take a nap (press the 2 key)?")
    user_input = input()
    if user_input == "1":
        print("You decide to take a through look through the living room. In your search you find a book that you have been  ")
        print("scoughering the earth for. Forgetting the entire reason why you were in the mansion, you take the book and head home.")
        time.sleep(2)
        sys.exit(0)

    elif user_input == "2":
        print("You wake up 20 minutes later after that good power nap.")
        print("Doze off again (press the 1 key) or watch TV (press the 2 key)?")
        user_input = input()
        if user_input == "1":
            print("Your slumber was disturbed by the detective clumsily knocking over a lamp in the next room.  ")
            print("Still feeling tired you decide to sleep for a few more minutes. As you try and adjust yourself ")
            print(" a little more comfortably you see that one of the hunting rifles on the wall were missing.  ")
            print("One of the suspects is a hunter.")

            print("Look further (press 1 key) or accuse the groundskeeper (press 2 key)? ")
            user_input = input()
            if user_input == "1":
                print("You investigate and see a calendar hanging on the wall. Someone had planned a hunting trip for today.")
                endTalk()

            elif user_input == "2":
                print("The groundskeeper had been at one of the neighbor’s houses at the time of the murder.  ")
                print("During your investigation the neighbor confirmed the groundskeepers alibi. The groundskeeper ")
                print(" does go hunting, but the missing rifle was taken by the Smith family when they went on ")
                print(" their annually family hunting trip. The detective realizing how inexperienced and unreliable ")
                print(" you are kicks you out of the house without paying for your services.")
                time.sleep(2)
                sys.exit(0)


        elif user_input == "2":
            print("When you wake up you decide to take a quick look through tv channels. As you’re scrolling you ")
            print(" notice that there is an marathon of your favorite tv show. Forgetting about the case you spend ")
            print(" the entirety of your time watching the show until you were kicked out by the detective.")
            time.sleep(2)
            sys.exit(0)
