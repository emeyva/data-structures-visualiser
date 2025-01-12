"""Interactive Visual Data Structures Learning Tool (Browser-Based Version)
 Updated Code Architecture"""

from flask import Flask, render_template, jsonify, request
from data_structures.linked_list import LinkedList
from data_structures.binary_tree import BinaryTree
from data_structures.graph import Graph

app = Flask(__name__)
linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_node', methods=['POST'])
def add_node():
    data = request.json
    value = data.get('value')
    if value is not None:
        linked_list.add(int(value))
        return linked_list.to_list()

@app.route('/delete_node', methods=['POST'])
def delete_node():
    data = request.json
    value = data.get('value')
    if value is not None:
        linked_list.delete(int(value))
        return linked_list.to_list()

@app.route('/get_linked_list', methods=['GET'])
def get_linked_list():
    return linked_list.to_list()

@app.route('/linked-list')
def linked_list_route():
    return render_template('linked_list.html')

@app.route('/binary-tree')
def binary_tree_route():
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    return render_template('binary_tree.html', tree=tree)

@app.route('/graph')
def graph_route():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    return render_template('graph.html', graph=g)

if __name__ == '__main__':
    app.run(debug=True)
