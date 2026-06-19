# The Soup
### A collection of Python utility classes and functions.

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![PyPI version](https://badge.fury.io/py/thesoup.svg)](https://badge.fury.io/py/thesoup)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Docs](https://img.shields.io/badge/docs-github%20pages-blue)](https://amartya00.github.io/thesoup/)

Full API documentation is available at [amartya00.github.io/thesoup](https://amartya00.github.io/thesoup/).

---

## Installation

#### From PyPI
```bash
pip install thesoup
```

#### From source
```bash
git clone https://github.com/sigabrtio/thesoup.git
cd thesoup
pip install .
```

To run the tests:
```bash
pip install -e ".[test]"
python -m nose2 --start-dir tst
```

---

## Components

### Classes

- **Graphs**
  - `DiGraph` — abstract directed graph
  - `MutableDiGraph` — abstract mutable directed graph
  - `AdjListGraph` — adjacency-list implementation of `MutableDiGraph`

- **Heap**
  - `MinHeap`
  - `MaxHeap`

- **Binary Trees**
  - `BinarySearchTree`

- **Trie** (ASCII only)

- **Sets**
  - `CountSet` — set that tracks occurrence counts of repeated elements
  - `DisjointSets` — disjoint-set / union-find structure ([Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure))

- **Result**
  - `Result` — a result type similar to Rust's `Result`

### Functions

- **Collections**
  - `flatten` — flatten a nested collection
  - `flatten_to_tuple` — flatten a nested collection, preserving tuples
  - `subsequence` — find all subsequences of a list
  - `foreach` — foreach that works on any collection
  - `group_by` — group a collection into a map by some criteria

- **Graph Traversals**
  - `bfs` — breadth-first search
  - `dfs` — depth-first search
  - `dijkstra` — Dijkstra's shortest path
  - `shortest_path_dag` — specialised shortest path for DAGs

- **Strings**
  - `is_anagram` — test if two strings are anagrams

- **Other**
  - `merge` — k-way merge
