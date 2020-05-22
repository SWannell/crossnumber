# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:15:57 2020

@author: setat
"""

import json
 import networkx as nx
 import matplotlib.pyplot as plt

# Grid associations
connections = {'A1': ['D1', 'D2', 'D3', 'D4'],
               'A5': ['D6', 'D7'],
               'A8': [],
               'A9': ['D2'],
               'A10': ['D6'],
               'A13': [],
               'A15': ['D6', 'D7', 'D11', 'D12'],
               'A17': ['D6', 'D14'],
               'A18': ['D19'],
               'A20': ['D6'],
               'A21': ['D16'],
               'A24': ['D22'],
               'A25': ['D19'],
               'A26': ['D6'],
               'A27': ['D19', 'D23'],
               'A29': ['D19', 'D22', 'D29', 'D30', 'D31'],
               'A32': [],
               'A33': ['D19'],
               'A35': ['D35'],
               'A36': [],
               'A37': ['D31', 'D37'],
               'A38': ['D28', 'D34', 'D35', 'D37']
               }

for source in connections.keys():
    lst = connections[source]
    new_dict = {t: 0.1 for t in lst}
    connections[source] = new_dict

print(connections)

# Clue associations
connections['A1']['A38'] = 1
connections['A8']['D12'] = 0.5
connections['A8']['D29'] = 0.5
connections['A9']['D1'] = 1
connections['A13']['A18'] = 0.5
connections['A13']['A26'] = 0.5
connections['A17']['A20'] = 0.5
connections['A20']['D6'] = 0.5
connections['A21']['A10'] = 0.1
connections['A21']['A10'] = 0.1
connections['A24']['A33'] = 0.1
connections['A25']['D19'] = 1
connections['A27']['A25'] = 0.5
connections['A32']['A18'] = 0.5
connections['A32']['A26'] = 0.5
connections['A35']['D37'] = 1
connections['A36']['D12'] = 0.5
connections['A36']['D29'] = 0.5
connections['A36']['A8'] = 1 # same clue!
connections['A38']['A1'] = 0.5

def add_link(source, target, weight):
    if source in connections.keys():
        connections[source][target] = weight
    else:
        connections[source] = {target: weight}

add_link('D1', 'A9', 1)
add_link('D2', 'A9', 0.5)
add_link('D2', 'D1', 0.5)
add_link('D3', 'D35', 0.5)
add_link('D4', 'D28', 0.5)
add_link('D11', 'A15', 0.5)
add_link('D12', 'A15', 0.1)
add_link('D14', 'D16', 0.5)
add_link('D16', 'D14', 1)
add_link('D22', 'D23', 1)
add_link('D23', 'D22', 0.5)
add_link('D28', 'D4', 1)
add_link('D29', 'A29', 0.1)
add_link('D30', 'A29', 0.5)
add_link('D34', 'D2', 0.5)
add_link('D35', 'A35', 0.5)
add_link('D35', 'D37', 0.5)
add_link('D37', 'D35', 1)

# Make into edge/node lists

nodes = set([])
for n1, links in connections.items():
    nodes.add(n1)
    for n2 in links.keys():
        nodes.add(n2)
print(nodes)
assert len(nodes) == 42

nodes_id = [{'name': el, 'id': i} for (el, i) in zip(nodes, range(len(nodes)))]
for i in range(lngth):
    nodes_id[i]['group'] = nodes_id[i]['name'][0]

edges_names = [{'source': source,
                'target': target,
                'value': connections[source][target]}
                for source in connections.keys()
                for target in connections[source].keys()]

edges_id = []
lngth = len(nodes)
for el in edges_names:
    s = el['source']
    t = el['target']
    v = el['value']
    s_id = [nodes_id[i]['id'] for i in range(lngth) if nodes_id[i]['name']==s]
    t_id = [nodes_id[i]['id'] for i in range(lngth) if nodes_id[i]['name']==t]
    edges_id.append({'source': s_id[0], 'target': t_id[0], 'value': v})

print(edges_id)


json_prep = {"nodes":nodes_id, "links":edges_id}
json_dump = json.dumps(json_prep, indent=1, sort_keys=True)
print(json_dump)

fn = 'connections.json'
json_out = open(fn,'w')
json_out.write(json_dump)
json_out.close()

# Show graph

G = nx.Graph(figsize=(9, 9))

# Import id, name, and group into node of Networkx:
for i in nodes_id:
    G.add_node(i['id'], name=i['name'], group=i['group'])

# Import source, target, and value into edges of Networkx:
for i in edges_id:
    G.add_edge(i['source'], i['target'], value=i['value'])

# Visualize the network:
fig, ax = plt.subplots(1, 1, figsize=(9, 9))
nx.draw_networkx(G, ax=ax, with_labels=True)
plt.axis('off')

# Show graph

G = nx.Graph(figsize=(9, 9))

# Import id, name, and group into node of Networkx:
for i in nodes_id:
    G.add_node(i['name'])

# Import source, target, and value into edges of Networkx:
for i in edges_names:
    G.add_edge(i['source'], i['target'], value=i['value'])

# Visualize the network:
fig, ax = plt.subplots(1, 1, figsize=(9, 9))
nx.draw_networkx(G, ax=ax, with_labels=True)
plt.axis('off')
plt.savefig('connections.png')

end_nodes = [node for (node, degree) in G.degree() if degree==1]
print('The nodes at the far ends of the graph:', end_nodes)

# Make a directed graph instead, as the clues are directional?