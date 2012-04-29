#!/usr/bin/env ruby
require "./require_me.rb"

initial_graph = [[1, 2, 10], [2, 3, 10], [2, 4, 10], [4, 5, 10], [6, 4, 10], [1, 6, 10]]
graph = Graph.new(initial_graph)
graph.append_vertex(5, 10)
debugger
weighting = Weight.new(graph.graph)
