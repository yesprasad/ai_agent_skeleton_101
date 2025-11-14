'''
a simple rule based function that says what type is the input. for now it is crude.
we shall make a classifier later on using NLP or other text matchers

we shall handle the below intents for now - 
question 
summarize
compare
suggest

'''

import re

def classify_intent(user_input: str) -> str:
    user_input = user_input.strip().lower()
    
    if re.search(r"\bwhat|how|when|does|is|are|can\b", user_input):
        return 'question'
    elif 'summarize' in user_input:
        return 'summarize'
    elif 'compare' in user_input or 'difference' in user_input:
        return 'compare'
    elif 'suggest' in user_input or 'recommend' in user_input or 'thoughts' in user_input or 'advise' in user_input:
        return 'suggest'
    else:
        return 'unknown' 

print(classify_intent("Suggest something for stress"))