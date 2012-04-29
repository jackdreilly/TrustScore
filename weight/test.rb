#!/usr/bin/env ruby
require "./require_me.rb"

initial_graph = [[1, 2, 10], [2, 3, 10], [2, 4, 10], [4, 5, 10], [6, 4, 10], [1, 6, 10]]
graph     = Graph.new(initial_graph)
new_node  = graph.append_vertex(5, 10)
weighting = Weight.new(graph.graph)
weighting.adjust_weights(new_node, true)
weighting.graph.write_to_graphic_file('jpg')
