import random
from adjectives import adjectives
from nouns import nouns
def username_gen(words):
  describerandom = random.randint(1,len(adjectives))
  thingrandom = random.randint(1, len(nouns))
  adjective_index = adjectives[describerandom]
  noun_index = nouns[thingrandom]
  randint = random.randint(1,1000)
  password = str(adjective_index) + str(noun_index) + str(randint) 
  print(password)

username_gen(['apple', 'banana', 'cranberry', 'doorknob', 'elephant'])
