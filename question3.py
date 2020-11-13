places_list = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
f = open("file_question.txt", "w")
for i in places_list:
    # print(i)
    f.write(i)
    f.write("\n")
f.close()
        
