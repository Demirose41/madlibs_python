## Order of prompts - PERSON - PLACE - TIME - ADJECTIVE - THING - PEOPLE - VERB - THING
order = ["PERSON","PLACE","TIME","ADJECTIVE","THING","PEOPLE","VERB","THING"]
choices = []
with open("story.txt","r") as myfile :
    story = myfile.read().replace("/n", " ")

    #story = story.replace("MADLIB", "PERSON",1)
    #print (story.count("MADLIB"))

choices.append(input(f"ENTER A {order[0]} :"))

print(choices[0])




#   while story.count("MADLIB") > 0 :
#       story = story.replace("MADLIB", "PERSON",1)
#       print (story.count("MADLIB"))
#       print (story)