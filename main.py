# coding: utf-8

from graphviz import Digraph
import requests
from config import *


def get_node_info(node_id=''):
    url = 'https://api.bilibili.com/x/stein/nodeinfo'
    params = {
        'aid': aid,
        'node_id': node_id,
        'platform': 'pc',
        'portal': 0,
        'screen': 0,
        'graph_version': 28883
    }
    return requests.get(url, params=params).json()


def get_node(node_id):
    print(node_id, end='\t')
    info = get_node_info(node_id)['data']
    if 'edges' in info.keys():
        choices = info['edges']['choices']
    else:
        choices = []
    
    node = {
        'node_id': node_id,
        'title': info['title'],
        'choices': choices
    }
    for choice in node['choices']:
        choice.update(get_node(choice['node_id']))
    return node


def draw_nodes(node):
    for choice in node['choices']:
        if layout == 'horizontal':
            G.node(str(choice['node_id']), '{%s | %s}' % (choice.get('option', 'START'), choice['title']))
            G.edge(str(node['node_id']), str(choice['node_id']))
        elif layout == 'edge':
            G.node(str(choice['node_id']), choice['title'])
            G.edge(str(node['node_id']), str(choice['node_id']), label=choice.get('option', 'START'))
        draw_nodes(choice)

def initial_node(nodes):
    if layout == 'horizontal':
        G.node_attr.update({'shape': 'record'})
        G.node(str(nodes['node_id']), '{%s | %s}' % (nodes.get('option', 'START'), nodes['title']))
    elif layout == 'edge':
        G.node_attr.update({'shape': 'box'})
        G.graph_attr.update({'rankdir': 'LR'})
        G.node(str(nodes['node_id']), nodes['title'])



if __name__ == '__main__':
    nodes = get_node(get_node_info()['data']['node_id'])

    G = Digraph(
        'av{}'.format(aid), 
        node_attr={'fontname': fontname}, 
        edge_attr={'fontname': fontname}
    )

    initial_node(nodes)
    draw_nodes(nodes)

    G.render(output)

    print('')
    print('Done.')

