import time
import csv

data = [["D", "0", "High", "Incomplete"], ["C", "2", "Low", "Incomplete"], ["B", "5", "Medium", "Incomplete"],
        ["A", "4", "High", "Incomplete"]]
def sort_test_function():
    """"""
    with open("file.txt", "w") as file:
        file.write("D")

    time.sleep(4)

    with open("file.txt", "r+") as file:
        confirmation = file.read()
        if confirmation == "Received":
            delimiter = ","
            with open("file.txt", "w") as file:
                for row in data:
                    line = delimiter.join(row) + "\n"
                    file.write(line)

    time.sleep(10)

    todo_list = []  # storage for delimited txt file --> list[list[str]]
    with open("file.txt", "r") as r_file:
        task = r_file.readlines()
        mylist = []
        for y in [x.split(',') for x in task]:
            for z in y:
                mylist.append(z.replace('\n', ''))
        for i in range(0, len(mylist), 4):
            todo_list.append(mylist[i:i + 4])
    with open("file.txt", "w") as file:
        file.write("")
    print(todo_list)
    return

sort_test_function()

"""todo_list = []  # storage for delimited txt file --> list[list[str]]
with open("file.txt", "r") as r_file:
    task = r_file.readlines()
    mylist = []
    for y in [x.split(',') for x in task]:
        for z in y:
            mylist.append(z.replace('\n', ''))
    for i in range(0, len(mylist), 4):
        todo_list.append(mylist[i:i + 4])"""

"""with open("file.txt", "w") as file:
    file.write("")"""