
import store_data
from copy import deepcopy
from collections import defaultdict


""" The program takes input from the terminal, stores node details after encryption in nested dict which is saved as json file
  A new node file is created for each node number. Each node file contains a set of nodes.
  """

initial_data = {
    'owner_name' : 'shashank',
    'address' : 'Pehowa',
    'mobile' : '8743042393',
    'phone' : 'NA',
    'value' : 0.0
}

owner_data = {
    'owner_name' : '',
    'address' : '',
    'mobile' : '',
    'phone' : '',
    'value' : 0.0
}

node_struct = {
    'timestamp' : '20/08/2018',
    'Data' : defaultdict(lambda: deepcopy(owner_data)),
    'NodeNumber' : 0,
    'NodeId' : '',
    'ReferenceNodeId' : '',
    'ChildNodeId' : '',
    'ReferenceChildNodeId' : ''
}

node = defaultdict(lambda: deepcopy(node_struct))
total_nodes = defaultdict(lambda: deepcopy(node))

def main():
    node_no = 1
    option = input('Enter option no.')
    if(option == '1'):
        node_struct['Data'] = initial_data
        total_nodes['1']['0'] = node_struct
        store_data.writeToJSONFile('first_file', total_nodes[str(node_no)])
    if(option == '2'):
        num = input('how many sets you want to make for first node')
        for i in range(1,int(num)):
            total_nodes['1'][str(i)] = node_struct
            print (total_nodes['1'])
        store_data.writeToJSONFile('first_file', total_nodes[str(node_no)])
    if(option == 3):
        """ Takes node number and all the details as input and store it in dict total_nodes[node_number]"""
    if(option == 4):
        """encrypt details using security module"""
    if(option == 5):
        """matches owner details stored in json"""

main()




