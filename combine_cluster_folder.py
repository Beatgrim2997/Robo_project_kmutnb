import os

folder_numbers = 10

for i in range(folder_numbers):
    for j in os.listdir("./pre_process_photos/unknown/" + str(i)):
        os.rename("./pre_process_photos/unknown/" + str(i)+"/" +
                  str(j), "./pre_process_photos/unknown/"+str(j))
    os.rmdir("./pre_process_photos/unknown/" + str(i))
