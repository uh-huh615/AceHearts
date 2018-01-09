# Declare characters used by this game.
define alex = Character('Alex', color="#014420")

#Define other variables here

# The game starts here.
label start:

    # Start by playing some music.
    # play music  #place holder

    scene bg lecturehall #place holder
    with fade

    "I wake up slowly, wondering why I didn't remember to close the blinds."
    
    "Shit, what time is it?! My alarm didn't go off!"
    
    "Why did no one wake me up. Oh no, i'm going to be late to sch---"

    "Wait,{p=1.0} no,{p=1.0} it's summer vacation.\n Phew, thought I was going to be in a lot of trouble"

    menu:

        "As I realize this, I decide to..."

        "Go back to sleep, might as well sleep in, it's summer!":

            jump sleep

        "Stay up, i'm up any way, may be able to do something useful.":

            jump wake


label sleep:

    alex "Well, I might as well get some more sleep. I don't have anything really to do anyway."

    alex "I mean, it's summer vacation. The perfect opportunity to sleep in. No school, no work, just me and my bed."

    jump scene_103

label wake:
    
    alex "I am already awake, I guess I might as well make the best of it!"

    #add more here

    jump scene_103

label scene_103:

    scene bg club #place holder
    with fade

    alex "place holder" #added to make the code execute
