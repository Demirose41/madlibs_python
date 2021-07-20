## Order of prompts - PERSON - PLACE - TIME - ADJECTIVE - THING - PEOPLE - VERB - THING
order = ["PERSON","PLACE","TIME","ADJECTIVE","THING","PEOPLE","VERB","THING"]
choices = []
with open("story.txt","r") as myfile :
    story = myfile.read().replace("/n", " ")

    #story = story.replace("MADLIB", "PERSON",1)
    #print (story.count("MADLIB"))

while len(choices) < 8 :
    choices.append(input(f"ENTER A {order[len(choices)]} :"))

print(choices)
choices = list(choices)
print(choices)


while story.count("MADLIB") > 0 :
    count = abs(story.count("MADLIB")-8)
    story = story.replace("MADLIB", f"{str(choices[count])}" ,1)
print (story)

