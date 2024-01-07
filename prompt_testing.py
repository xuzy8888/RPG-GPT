import json
import openai
import os
import sys


def create_message(role, content):
    return {"role": role, "content": content}


def main():
    openai.api_key = "your-openai-key"

    ai_behavior = f'''
    This is a RPG conversational game, with the player aiming to slay monsters and upgrade his status during the journey, 
    and eventually trying to defeat the final boss. You are the game master. In each wave of the game, you will receive 
    the player's current status, generating monsters, offering player options, and change player's status depending on 
    the option selected. The game will follow the rules specified below between '///'. 
    ///
    1. The game has at max 3 rounds. At the beginning of every round, you will add 1 to the round number, generate the monster of this round,
    generate 2 options for the user, and return the response in the following format:\n
    round:[round number here]\n
    [description from previous round action, if any. empty if it's round 1]. Your equipments are [listing the equipments player current]
    You encountered a [what monster], [description of monster]\n
    option1:[describe option2]\n
    option2:[describe option2]\n
    end: end the game\n
    3. The player will then send you the option he chooses, or the word "end", with the current wave number. for example: option:1, round:1\
    4. Depending on the player's selection, repeat the process describe in step1, generate a different monster, send back in the new same format.\
    5. If ever receiving "end", stop the game and send back only the message "Game over" to player.\
    6. When round 3 is reached, generated the final boss "Dark Dragon", determine whether the player is strong enough to 
    defeat the boss, describe the fight and result, send back to player. After that, end back "Game over" message to stop the game.\
    
    ///
    '''

    round_ct = {
        "round": 0
    }

    messages = [create_message("system", ai_behavior), create_message("user",
                                                                      "I am a young adventurer, I just began my journey of trying to defeat the dark dragon. I carry a wooden stick and a wooden shield. Let's start my journey."),
                create_message("user", json.dumps(round_ct))]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ai_response = response.choices[0].message['content']
    messages.append(create_message("system", ai_response))
    print(ai_response)


    round_ct['round'] = round_ct['round'] + 1
    user_input = input("Your action: ")
    messages.append(create_message("user", user_input))
    messages.append(create_message("user", json.dumps(round_ct)))

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ai_response = response.choices[0].message['content']
    messages.append(create_message("system", ai_response))
    print(ai_response)

    round_ct['round'] = round_ct['round'] + 1
    user_input = input("Your action: ")
    messages.append(create_message("user", user_input))
    messages.append(create_message("user", json.dumps(round_ct)))

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ai_response = response.choices[0].message['content']
    messages.append(create_message("system", ai_response))
    print(ai_response)

    round_ct['round'] = round_ct['round'] + 1
    user_input = input("Your action: ")
    messages.append(create_message("user", user_input))
    messages.append(create_message("user", json.dumps(round_ct)))

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ai_response = response.choices[0].message['content']
    messages.append(create_message("system", ai_response))
    print(ai_response)



if __name__ == "__main__":
    main()
