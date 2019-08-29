﻿label ch3:
    $ skip_next = "skip_to_ch4"
    scene black
    show bg black
    show me nrm at left
    with dissolve
    show jaf nrm at right
    with dissolve
    me "Are we inside the lamp now?"
    jaf "Yes."
    me "And I'm still alive?"
    jaf "Yes."
    me "Looks much larger from outside."
    jaf "..."
    me "You have some leg room in here."
    jaf "..."
    me "Doesn't smell like farts either."
    jaf "Stop with your wisecracks, we have work to do."
    jaf "You need to learn how to navigate this place when I'm not around."
    me "First question, how do I come inside in the first place."
    jaf "Excellent question, I just think of it and it happens, but you need a spell or something."
    jaf "I'll come up with something."
    jaf "But first, let me show you the different places in here."
    menu:
        "I can find my way around, let's get to something more exiting.":
            jaf "Eager to draw your sword aren't you?"
            jaf "Have a look around then meet me in my library.."
            jump ch3_1
        "Yes please, this place looks like the desert night.":
            jaf "Are you afraid of dark?"
            me "No. I'm afraid I fall into a hole in this darkness."
            jaf "Nah, you'll be fine."
            jaf "Just don't wonder too far away from the bright spots."
            jaf "Here's one."
            # save
            show bg sav
            me "Empty jars?"
            me "An obsession of yours?"
            me "What are they hanging from? I can't see the sealing."
            jaf "There's no sealing here, no walls and the thing you're walking on, isn't a floor."
            me "What!?"
            jaf "Focus Abdul!."
            jaf "Here, take this."
            $ msg.msg("Received a bag.")
            me "..."
            $ msg.msg("...of sand?")
            me "A bag of sand?"
            jaf "Sands of time, grab a handful, put in one of these jars and that moment of you will be trapped in it."
            $ msg.msg("Right, Received sands of time, a dozen handfuls.")
            jaf "That moment of you can be recovered in necessary."
            jaf "It comes handy in case you make a mistake or die."
            me "You can resurrect me?"
            jaf "Not exactly."
            jaf "You'll have to wish for it. But it's pretty difficult to wish when you're dead!"
            jaf "This is my way to walk around that problem."
            jaf "Just don't overdo it, you don't have much sand and it's not easy to obtain more of it."
            me "Alright."
            # set
            show bg sett
            me "What's this one."
            jaf "I'm not entirely sure, those seems to have some effect on the outside world."
            jaf "I don't have any use for them."
            jaf "You'll have to try them by yourself I'm afraid."
            # lib
            show bg lib
            me "You have a library in here?"
            jaf "Of course."
            me "Jafar's economy for Sultans?, Jafar's etiquettes of palace?, Jafar's guide to tapdance?"
            jaf "Not one of my best that one."
            me "Are all of these books written you you? Jafar?."
            jaf "Yes, I need to transfer my knowledge to the next generation somehow."
            jaf "You should borrow few of them sometime."
            jaf "In fact, you need to read them all, they'll help you with your quest."
            jaf "Speaking of."
            jaf "I'll keep track of your process...{nw}"
            # quest
            show bg quest
            jaf "Here."
            me "A mirror?"
            jaf "Through this mirror I can watch you outside of the lamp. Guide you and give you information."
            me "You can see me all the time?"
            jaf "What's the matter?"
            me "What about my privacy?"
            jaf "Get over yourself, I don't have time to watch you all the time. I have books to write."
            jaf "And I don't have any interest in watching you jerk off."
            jaf "I have a harem of myself."
            me "A harem? Let's go see it."
            # fight
            show bg fight
            me "Not this.{nw}"
            # gallery
            show bg gall
            me "Not this.{nw}"
            # harem
            show bg harem
            me "Ah yeeesss, you have three slave girls in here?"
            jaf "They aren't slaves, they're free."
            me "Wifes?"
            jaf "No, they're just trapped in here for some reason."
            jaf "And they seem to be happy keeping me company."
            me "ummm..."
            me "Can I? ummm... I mean... May I?"
            jaf "Fuck them? I'm not the one you should ask."
            jaf "Ask them, it's up to them to decide."
            jaf "The communication might be a problem though, I'm not sure if they can speak."
            jaf "Never heard a pip out of them."
            jaf "You might want to take a shower first, we're keeping it clean in here."
            me "A shower...? Hey, are those?"
            jaf "Yes, statues of me peeing, it seemed like a good idea at the time."
            jaf "The girls seem to like them, and I wasn't expecting any guests in here for a long time."
            jaf "Now let's go back and visit the places we skipped."
            menu:
                "Sure, I can come back later.":
                    # fight
                    show bg fight
                    jaf "Alright here is my throne. You'll be fighting the creatures I conjure in here."
                    jaf "To increase your fighting skill, and maybe my amusement."
                    jaf "You can come here and start fighting at any time."
                    jaf "Do you want to give it a try?"
                    menu:
                        "Yes":
                            jaf "Alright, here we go."
                            call ch3_fight(True)
                            show me nrm at left
                            with dissolve
                            show jaf nrm at right
                            with dissolve
                            jaf "Not bad."
                            jaf "At least, you didn't die."
                            jaf "Now."
                            jaf "I'll have to prepare something."
                            jaf "Meet me at my library when you're done."
                            hide jaf with dissolve
                            jump ch3_1
                        "Maybe later.":
                            jaf "Alright, next is the hall of memories."
                            jaf "You can revisit your proudest moments in here."
                            jaf "And that's it. I have some thinking to do. Feel free to roam around while I'm busy."
                            jaf "Meet me at my library when you're done."
                            hide jaf with dissolve
                            jump ch3_1
                "I think I'm going to take that shower you've suggested now.":
                    jaf "alright, you don't seem to be capable of thinking straight, come to me when you releaved yourself."
                    jaf "I'll think of a plan in the mean time."
                    hide jaf with dissolve
                    menu:
                        "go talk to the girls.":
                            call harem_girls
                            jump ch3_1
                        "jump right into the water.":
                            show bg cg_abdul_bathing
                            "the bathing scene is not ready"
                            menu:
                                "go talk to the girls.":
                                    call harem_girls
                                    jump ch3_1
                                "go back to Jafar.":
                                    jump ch4

label ch3_1:
    menu:
        "This part will be replaced by a proper screen, but for now have a menu."
        "Go to library.":
            jump ch4
        "Go to harem.":
            jump ch3_harem
        "Go to hall of... sands of time.":
            jump ch3_sav
        "Go to room of settings.":
            jump ch3_set
        "Go fight.":
            call ch3_fight
        "Go to the mirror room.":
            jump ch3_mirror
label ch3_harem:
    scene bg harem
    menu:
        "go talk to the girls.":
            call harem_girls
            jump ch3_1
        "jump right into the water.":
            show bg cg_abdul_bathing
            "the bathing scene is not ready"
            menu:
                "go talk to the girls.":
                    call harem_girls
                    jump ch3_1
                "go back to Jafar.":
                    jump ch4
    jump ch3_1
label ch3_sav:
    scene bg sav
    "nothing to do here."
    jump ch3_1
label ch3_set:
    scene bg sett
    "nothing to do here."
    jump ch3_1
label ch3_fight(j=False):
    window hide
    call fights([player], [enemy1])
    if j:
        return
    else:
        jump ch3_1
label ch3_mirror:
    "the quest screen is not even designed, just a test to make sure it's functional."
    show screen quests
    pause
    jump ch3_1