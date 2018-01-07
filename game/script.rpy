# Declare characters used by this game.
define a = Character('Alex', color="#28cd71")

#Define other variables here

# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus" #place holder

    scene bg lecturehall #place holder
    with fade

    "I wake up slowly, before jolting forward in my bed."

    a "My alarm didn't go off! Oh no, i'm going to be late to sch---"

    a "Wait, no, it's summer vacation. Phew, thought I was going to be in a lot of trouble"

    menu:

        "As I realize this, I decide to..."

        "Go back to sleep, might as well sleep in, it's summer!":

            jump sleep

        "Stay up, i'm up any way, may be able to do something useful.":

            jump wake


label sleep:

    a "Well, I might as well get some more sleep. I don't have anything really to do anyway."

    a "I mean, it's summer vacation. The perfect opportunity to sleep in. No school, no work, just me and my bed."

    jump scene_103

label wake:
    
    a "I am already awake, I guess I might as well make the best of it!"

    #add more here

    jump scene_103

label scene_103:

    scene bg club #place holder
    with fade

    a "place holder" #added to make the code execute
