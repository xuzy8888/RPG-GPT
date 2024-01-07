For traditional RPG games, players will control its character in pre-designed scenes and walk through pre-populated events. With the growth of the game industry, RPG games have grown to develop various branches that adopted different modern technologies. For example, rogue-like game is a style of role-playing game traditionally characterized by procedurally generated levels, turn-based gameplay, and high fantasy narrative. With the introduction of generative AI, I believe that the randomness and quality of those games will be further enhanced, given language model like Chat GPT are good at generate innovative fantasy game stage without demanding heavy coding tasks, and the process of user interacting with AI chatbots perfectly matches the turn-based nature of such game.  
Tech Stack:  
Python OpenAI API langchain  
Developing Path:  
Step 1: Sketching the Game  
This is a completely design task without much coding and Generative AI taking parts. I wrote a script of the game, classifying which information should be provided as user input, which information should be generated by the AI model. The intention here is to make use of Generative AI as much as possible, therefore as less code running and local data storing as possible.  
Step 2: Game Prompt  
After mapping out the game, I wrote a prompt for the game setting and rule. The initial version of the prompt has been recorded in the prompt_testing.py. The prompt was used for testing the access to ChatGPT 3.5 turbo model and other relative settings (python libraries, syntax of functions) by running 3 rounds of a command line game.  
Step 3: Prompt Engineering  
Following the guideline from ChatGPT prompt engineering lesson and referencing online resources of other game play prompt, I have revised the game prompt to the current version. The prompt is in revised_prompt.pdf, which itself can be used to input into chatbots like ChatGPT to start a playable conversational game.  
Prompt Engineering Lesson:  
https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/1/introduction  
ChatGPT game prompt:  
 
 https://www.reddit.com/r/OpenAI/comments/zdndxt/chatgpt_text_based_adventure/?rdt=36410  
The prompt engineering strategies I used were the following:  
Ask for output in a specified format  
I asked the language model to formulate the options every time, ensuring the decision point is clear and easy to understand. Example:  
```  
You will give three options.  
(A) option text  
(B) option text  
(C) option text  
```  
Ask the model to check whether conditions are satisfied  
Other than the structured response, I asked the model to make sure each piece of the response did answer certain questions that give the player sufficient information. Example:  
```  
explain the result of the battle given the player used the selected option, and the updated context in 3 sentences. First, what the player chooses to perform. Next, how the selected action affects the monster, was it a win or loss? Third, what is the change to the character, for example additional item dropped, weapon damaged, leveling up, or even nothing?  
```  
“Few Shot” Prompting  
For the option text, I gave the language model some examples to indicate that the option context should be creative and relative to the current context. Example:  
```  
More examples. If we are facing the rock golem, and the player is holding a water gem earned after defeating slime, one of the option contexts could be throwing the water gem to the rock golem to destroy the golem instantly.  
```  
Specifying the Steps  
The game prompt in general, it follows a “first...then...after that, then...” format. Example:  
```  
First, you will...  
After the player responds,...  
Then, in two sentences, ....  
```  
Iterations  
The prompt was tested for multiple runs, each time if some of the instructions lead to unwanted output it will be modified to make sure the GPT eventually generates a steady game process. I also incorporated several phrases from the online resources to make the narration more vivid. Example:  
````  
Do not proceed until you have the answer -> Do not proceed until play has responded  
      
 Never break the fourth wall. Don't mention that we're playing a game. Only break character if you are facilitating a game action.  
```  
The resulted command line RPG_GPT is saved in the file named rpg_gpt_v1.py
  
Step 4 LangChain Integration  
At this point, the language model remembering the previous context between different user inputs by concatenate all the previous messages to the prompt:  
Referencing this online recourse:  
https://github.com/Azure/openai-samples/blob/main/Basic_Samples/Chat/chatGPT_managing_c onversation.ipynb  
In order to figure out the number of tokens used using this approach, I used the tiktoken library and defined a helper function to monitor the number of tokens as the message expands. The added method is in v1_token_ct.py.  
 Below is my observation:  
 messages.append(create_message("system", ai_response))  
 messages.append(create_message("user", user_input))  
       
According to the above, the number of tokens nearly doubled by the end of the game. In order to find a way to store the memory more efficiently, I was thinking of trying out the memory implemented with langchain.  
The new version of rpg_gpt with the integration of langchain template and memory is saved into rpg_gpt_v2.py. It’s worth mentioning that the current responding speed is much faster than the previous version.  
Step 5 GUI Interface  
Referencing the online resource, I wrapped my GPT with a graphic UI implemented with python tkinter. The source code is stored in rpg_gpt_v3.py. The result was below:  
 Reference:  
https://github.com/mracko/FirstContactGPT/blob/main/README.md  
