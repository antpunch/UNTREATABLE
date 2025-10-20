# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Dr. Mau", color="#ffffff")
define k = Character("Kebe", color="#40548c")
define n = Character("Nadia", color="#50547c")

# The game starts here.

label start:

    # initial variables
    $ kebe_condition = 3
    $ nadia_condition = 4

    play music "audio/Relax.ogg" fadein 1.0 volume 0.5
    scene office

    "As the end of another long day approaches, you prepare to end your session with your current patient."

    "Patient" "Thank you so much for your guidance, Dr. Mau. I really feel like I can overcome this life obstacle on my own now."

    c "Mrow!~"

    "Patient" "I'll be sure to follow your advice. See you at our next session!"

    "As your 6th patient of the day leaves your office, you shuffle through your {i}very{/i} important paperwork in your faux-leather binder."
    "The bill for rent is about to be due, but you also need to make sure you earn enough this month so you can finally get your paws on that limited-time premium Tuna-Tuna Can you've been dreaming about. You call for the next patient to enter."
    
    window hide dissolve

    show boi_neutral with moveinright

    window show dissolve

    "???" "..."

    c "Hsss, meow?"

    show boi_talking
    k "H-hello, Dr. Mau. I'm Kebe. Thank you for seeing me... So, I came here today because lately, I've been feeling extremely... restless, I guess?"
    k "Like, it's really hard for me to focus on anything, I have trouble sleeping, and it's like everything is out of my control. I-it's just too much."
    show boi_neutral

    c "Mrowww~"
    
    show boi_embarrassed
    k "Y-yeah, I don't really know what's causing it. My boss at work thinks I should take some time off, saying that I'm overworking myself, but I don't know how else to relax and relieve stress without overthinking all the time."
    hide boi_embarrassed

    show boi_talking
    k "I constantly try to make everything perfect, double-checking if I locked my door, checking my emails multiple times... I considered taking up a hobby, but I don't really have the time or energy for that."
        
    hide boi_talking
    show boi_neutral
    c "Purr-purr."

    show boi_talking
    k "Recently, I've also been having these headaches and muscle tension. I-I think it's all just from the stress building up. I have an inkling I might have an anxiety disorder, but I'm not sure. My friends recommended I see a therapist, so here I am."
    k "I guess I just want to find a way to feel more in control over my life without fretting over the smallest things. Do you have any suggestions, Dr. Mau?"

    menu kebe_choice_1:

        # calm approach
        "Meoooow~":
            c "Meoooow~" 
            show boi_embarrassed
            k "O-oh, that's a good idea! I-I could try some breathing exercises or meditation to help me relax when I start feeling overwhelmed."
            k "My chest does feel tight often, so maybe that could help."
            $ kebe_condition -= 1 # condition improved, kebe_condition = 2
            jump scene_kebe_2


        # berating approach
        "MRROW! Hissss!":
            c "MRROW! Hissss!" 
            show boi_anxious
            k "W-whoa, I'm sorry! I didn't mean to upset you, Dr. Mau. Please don't be mad at me."
            k "I, uh, I guess I'm just overthinking again... It's not a big deal."
            $ kebe_condition += 1 # condition worsened, kebe_condition = 4
            jump scene_kebe_2

label scene_kebe_2:
    if kebe_condition == 2:
        "Kebe seems to be feeling a bit better now."
    elif kebe_condition == 4:
        "Kebe is still feeling quite anxious."

    show boi_embarrassed
    k "I'm supposed to be meeting a friend for lunch after this session, but I don't know if I can focus on eating with all this on my mind. I don't want to ruin our time together by being distracted."
    k "D-do you have any advice for managing anxiety in social situations?"

    menu kebe_choice_2:
        # calm approach
        "Purrr~ *Head nudge*":
            c "Purrr~" 
            show boi_embarrassed
            k "T-thank you, Dr. Mau. It feels like you're telling me to just be present and reminding myself that it's okay to just exist sometimes. I think that will help me enjoy my time with my friend."
            k "I'll try to keep that in mind."
            "Kebe seems to relax a bit more and his breathing is steadier."
            $ kebe_condition -= 1 # condition improved, kebe_condition = 1
            jump scene_kebe_3


        # berating approach
        "Mrowww!":
            c "Mrowww!"
            play music "audio/Letting Go Main.ogg"
            hide boi_embarrassed
            show boi_anxious
            k "I-I'm sorry, Dr. Mau. I didn't mean to upset you again. Wait, are you... are you telling me to just push through it no matter what? And that my friend probably hates me for being like this?"
            k "M-maybe I'm just not cut out for social situations right now."
            "Kebe's eyes dart around, his hands trembling slightly."
            $ kebe_condition += 1 # condition worsened, kebe_condition = 5
            hide boi_anxious
            jump scene_kebe_4

label scene_kebe_3: # Kebe seems to be feeling a bit better now.
    show boi_neutral
    show boi_talking
    k "I-I think I can manage that. I'll try not to worry so much about things going wrong and just focus on enjoying the moment."
    c "Mrow~"
    jump calm_kebe_end

label scene_kebe_4: # Kebe is still feeling quite anxious.
    show boi_anxious
    k "I need to get out of this headspace. I'm starting to... feel a little dizzy."

    c "Mrow..."

    menu kebe_choice_4:
        "Mew-mew! MRAW!":
            c "Mew-mew! MRAW!"
            show boi_panic
            k "W-what?! Are you saying this is a sign of something much worse coming soon?! I-I can't... I can't do this... I need to leave..."
            $ kebe_condition += 1 # condition worsened, kebe_condition = 6
            k "I... I think I need to go now. I'm sorry, Dr. Mau. I'll pay on the way out..."
            hide boi_talking
            hide boi_neutral
            hide boi_anxious
            hide boi_panic with moveoutright
            "Kebe hurriedly stands up and rushes out the door, leaving his payment on your desk."
            jump scene_nadia_1

        "Meowww... Purr~":
            c "Meowww..."
            jump calm_kebe_end

label calm_kebe_end:
    show boi_embarrassed
    k "I think your presence alone makes everything feel a bit more manageable. O-okay... I think I can try to calm down. Thank you for your help, Dr. Mau."
    hide boi_embarrassed
    hide boi_anxious
    hide boi_talking
    show boi_neutral
    k "I'll be on my way now."
    window hide dissolve
    hide boi_talking
    hide boi_neutral with moveoutright
    window show
    "Kebe stands up with determination and heads towards the door, leaving his payment on your desk."
    $ kebe_condition -= 1 # condition improved, kebe_condition = 3
    stop music
    jump scene_nadia_1


label scene_nadia_1:
    play music "audio/Relax.ogg"
    "The next patient enters your office."
    show gorl_neutral with moveinright

    "Your seventh patient of the day is a young woman with short, fluffy hair and bright eyes. She looks around the room with curiosity."

    show gorl_talking
    n "Hello, Doctor. I'm Nadia. What a lovely office you have here! It's very cozy."
    hide gorl_talking
    c "Mew?"
    show gorl_talking
    n "I'm doing fine, thank you for asking. I've been looking forward to our session today. I wanted to explore some feelings I've been having lately."
    hide gorl_talking
    c "Purr-purr~"
    show gorl_talking
    n "Lately, I've been feeling a bit... lost. Like I'm not sure who I am or what I want out of life. It's like I'm just going through the motions without any real direction. I'm hoping you can help me find some motivation and clarity."

    menu nadia_choice_1:
        "Yaaawn... *Stretch*":
            c "Yaaawn..."
            show gorl_tired
            n "Oh. That was a very indifferent sound. It's like you're tired of hearing the same thing over and over again. I'm sorry to bother you if you feel that way."
            $ nadia_condition += 1
            jump nadia_scene_2

        "Mewww~!":
            c "Mewww~!"
            show gorl_happy
            n "Heh. That's a good noise. It feels like you're encouraging me to just keep trying things and see what will hit the spot."
            hide gorl_happy
            n "Not that it's a bad thing. It's just hard to do anything when you don't know what you want, you know?"
            $ nadia_condition -= 1
            jump nadia_scene_2

label nadia_scene_2:
    show gorl_tired
    n "I used to love painting, but now it just feels like a chore. No source of inspiration, no nothing. The joy is just... gone."
    show gorl_talking
    n "I'm not sure what to do about it. How can I find my passion again?"
    c "Mrow. Purrr..."

    menu nadia_choice_2:
        "Mew...":
            c "Mew..."
            "You place a comforting paw on your patient's hand."
            show gorl_happy
            n "Oh, my. You sound genuinely concerned for me. It makes me feel validated in my hopes and doubts. Maybe finding something I enjoy is something worth fighting for."
            $ nadia_condition -= 1
            jump nadia_scene_3

        "Mrrowww!!!":
            c "Mrrowww!!!"
            "You start hitting your tail on your armrest."
            play music "audio/In Legends.ogg"
            show gorl_tired
            n "That's a very impatient noise. Are you perhaps telling me to stop feeling sorry for myself and just do something even if it's pointless? That's pretty exhausting."
            $ nadia_condition += 1
            jump nadia_scene_3

label nadia_scene_3:
    show gorl_happy_talking
    n "My friends invited me out tonight, and I just can't seem to bring myself to text them back. I just want to disappear into nonexistence sometimes, you know?"
    c "Hsss..."

    menu nadia_choice_3:
        "*Wail*":
            show gorl_tired
            n "That sounds almost like pure despair. Is it truly hopeless for me? Why should I even try to do anything in my life? It all leads to nothing anyway."
            show gorl_hysterical
            n "Life is just meaningless. I don't understand why people expend so much effort chasing trivial dreams. We're all going to die the same death!"
            $ nadia_condition += 1
            jump nadia_end_scene1

        "Purrr...":
            show gorl_happy_talking
            n "I feel at peace when you speak to me. A soft, quiet affirmation. You're not judging me or demanding anything. You're just... here."
            n "Maybe just exisitng for a little while is enough."
            $ nadia_condition -= 1
            jump nadia_end_scene2

label nadia_end_scene1:
    show gorl_hysterical
    n "I'll come back here again for another session. Thank you for showing me the way! Haha..."
    hide gorl_neutral
    hide gorl_happy
    hide gorl_tired
    hide gorl_talking
    hide gorl_hysterical moveoutright
    c "Mew."
    jump ending

label nadia_end_scene2:
    show gorl_happy_talking
    n "Thank you so much, Dr. Mau. I'll see myself out."
    hide gorl_neutral
    hide gorl_happy
    hide gorl_tired
    hide gorl_talking
    hide gorl_happy_talking moveoutright
    c "Mew!"
    jump ending

label ending:
    "The clock chimes, ending your shift. It's time to check the ledger."

    if kebe_condition >= 5 and nadia_condition >= 5:
        jump good_ending
    else:
        jump bad_ending

label good_ending:
    play music "audio/Relax.ogg"
    "You successfully worsened Kebe's anxiety and deepened Nadia's depression."
    c "MRRRROW! (Happy!)"
    "The world's misery is your financial gain. A fat envelope of cash is slipped under the door. The Tuna-Tuna Can is yours."
    "GOOD ENDING: RENT PAID"
    return 
label bad_ending:
    "You failed to fully ruin your patients. Kebe is calmer, Nadia found a little hope."
    c "Mew... (Sad)"
    "Your human patients are happier, but the world of cat therapy is a cruel beast. A note is pinned to your door: 'NO MONEY. TRY HARDER TO BE A BAD INFLUENCE.'"
    "BAD ENDING: BROKE & OUT OF BUSINESS"
    return

return