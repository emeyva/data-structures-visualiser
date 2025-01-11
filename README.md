# Data structures visualizer
A simple way to visualize and mess with some data structure on the browser.

## Supported Data structures
- Linked list

## Project dir structure
```
interactive_data_structures_tool/
├── app.py                       # Main Flask application
├── data_structures/              # Python modules for different data structures
│   ├── linked_list.py            # Linked List implementation
│   ├── binary_tree.py            # Binary Tree implementation
│   └── graph.py                  # Graph implementation
├── templates/                    # HTML templates for the web interface
│   ├── index.html                # Home page
│   ├── linked_list.html          # Linked List visualization
│   ├── binary_tree.html          # Binary Tree visualization
│   └── graph.html                # Graph visualization
├── static/                       # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css            # Custom CSS styles
│   ├── js/
│   │   └── scripts.js            # Custom JavaScript functions
│   └── images/                   # Any images used in the project
├── tests/                        # Unit tests for your data structures
│   ├── test_linked_list.py       # Tests for Linked List
│   ├── test_binary_tree.py       # Tests for Binary Tree
│   └── test_graph.py             # Tests for Graph
└── README.md                     # Project documentation
```
