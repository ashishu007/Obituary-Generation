# utility file for handling different kinds of errors in a 
# rule-based manner

import re

# correct the gender errors such as: deceased person is male but the messages contains words like "she" or "her"
def gender_errors(message, gender):

    if gender == "F":
        rep = {" his ": " her ", " he ": " she ", "He ": "She ", "His": "Her ", " His ": " Her ", " He ": " She "} 
    else:
        rep = {" her ": " his ", " she ": " he ", "She ": "He ", "Her": "His ", " Her ": " His ", " She ": " He "} 

    # use these three lines to do the replacement
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    #Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
    pattern = re.compile("|".join(rep.keys()))
    corrected_message = pattern.sub(lambda m: rep[re.escape(m.group(0))], message)

    return corrected_message

# errors such as extra full stop, 
# first letter in small caps in the start of a sentence, 
# a capital letter in between the sentence, etc.
def syntax_errors(message):
    pass
    # return corrected_message
