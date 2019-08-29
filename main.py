# coding: utf-8

from graphviz import Digraph
import requests
import time
from bs4 import BeautifulSoup
import json
from config import *

def get_graph_version(aid):
    videopage = requests.get('https://api.bilibili.com/x/web-interface/view?aid=56415139').json()
    cid = videopage['data']['pages'][0]['cid']

    headers = {
        'Accept': '*/*',
        'Referer': 'https://www.bilibili.com/video/av{}'.format(aid),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Sec-Fetch-Mode': 'cors',
    }

    params = (
        ('id', 'cid:{}'.format(cid)),
        ('aid', str(aid)),
    )

    player = requests.get('https://api.bilibili.com/x/player.so', headers=headers, params=params)
    player.encoding = player.apparent_encoding
    soup = BeautifulSoup(player.text, 'lxml')
    interaction = json.loads(soup.select('interaction')[0].get_text())
    graph_version = interaction['graph_version']
    print('graph_version: {}'.format(graph_version))
    return graph_version
    
graph_version = get_graph_version(aid)
node_infos = {}
graph_nodes = []
graph_edges = []

def get_node_info(node_id=''):
    url = 'https://api.bilibili.com/x/stein/nodeinfo'
    params = {
        'aid': aid,
        'node_id': node_id,
        'graph_version': graph_version,
        'platform': 'pc',
        'portal': 0,
        'screen': 0,
    }
    data = requests.get(url, params=params).json()
    time.sleep(interval)
    return data


def get_node(node_id):
    
    if node_id in node_infos.keys():
        info = node_infos[node_id]
    else:
        print(node_id)
        info = get_node_info(node_id)['data']
        node_infos[node_id] = info

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

def add_node(node_params, graph_nodes):
    if node_params not in graph_nodes:
        graph_nodes.append(node_params)
        G.node(**node_params)

def add_edge(edge_params, graph_edges):
    if edge_params not in graph_edges:
        graph_edges.append(edge_params)
        G.edge(**edge_params)


def draw_nodes(node):
    for choice in node['choices']:
        if layout == 'horizontal':
            node_params = {
                'name': str(choice['node_id']),
                'label': '{%s | %s}' % (choice.get('option', 'START'), choice['title'])
            }
            add_node(node_params, graph_nodes)

            edge_params = {
                'tail_name': str(node['node_id']),
                'head_name': str(choice['node_id'])
            }
            add_edge(edge_params, graph_edges)
        elif layout == 'edge':
            node_params = {
                'name': str(choice['node_id']),
                'label': choice['title']
            }
            add_node(node_params, graph_nodes)

            edge_params = {
                'tail_name': str(node['node_id']),
                'head_name': str(choice['node_id']),
                'label': choice.get('option', 'START')
            }
            add_edge(edge_params, graph_edges)

        draw_nodes(choice)

def initial_node(nodes):
    if layout == 'horizontal':
        G.node_attr.update({'shape': 'record'})
        node_params = {
            'name': str(nodes['node_id']),
            'label': '{%s | %s}' % (nodes.get('option', 'START'), nodes['title'])
        }
        add_node(node_params, graph_nodes)
    elif layout == 'edge':
        G.node_attr.update({'shape': 'box'})
        G.graph_attr.update({'rankdir': 'LR'})
        node_params = {
            'name': str(nodes['node_id']),
            'label': nodes['title']
        }
        add_node(node_params, graph_nodes)



if __name__ == '__main__':

    nodes = get_node(get_node_info()['data']['node_id'])

    G = Digraph(
        'av{}'.format(aid), 
        node_attr={'fontname': fontname}, 
        edge_attr={'fontname': fontname},
        strict=True
    )

    initial_node(nodes)
    draw_nodes(nodes)

    G.render(output, format=output_format)

    print('')
    print('Done.')

