import math
from Node import Node

NODES = []
T_MAX = []
def read_file(file_name):
    file_path = "Instances/" + file_name + ".txt"
    file = open(file_path, "r")
    lines = file.readlines()
    lines_len = len(lines)
    for i in range (lines_len):
        line_list = [float(x) for x in lines[i].split()]
        if(i == 0):
            T_MAX.append(line_list[0])
            continue
        else:
            node = Node(i, line_list[0], line_list[1], line_list[2])
            NODES.append(node)


def distance(node1, node2):
    return math.sqrt((node1.x - node2.x)**2 + (node1.y- node2.y)**2)


def checker(solution):
    t_max = T_MAX[0]
    time = 0
    profit = 0
    for index in range (len(solution)):
        node_id = solution[index]
        current_node = NODES[node_id - 1]
        if(time > t_max):
            print("Can't visit", node_id)
            break
        print("We can visit node", node_id)
        profit += current_node.profit
        if(index < len(solution) - 1):
            next_node_id = solution[index + 1]
            next_node = NODES[next_node_id - 1]
            travel_time = distance(current_node, next_node)
            print("Travel time from", node_id, "to", next_node_id,":",travel_time)
            time += travel_time
            print("Time unitll now", time)
                
    
    print("Profit", profit)
    print("Time", time)

# read file and initalise data
read_file("set_66_1_020")

# put solution here
solution_array = [1,5,4,8,12,15,60]
checker(solution_array)
            

        

