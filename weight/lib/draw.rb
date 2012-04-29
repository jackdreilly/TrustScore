#! /usr/bin/env ruby

=begin
# Start with a graph
dg = RGL::DirectedAdjacencyGraph[1,2 ,2,3 ,2,4, 4,5, 6,4, 1,6]

# Add node
# Update that nodes repayment


dg.reverse

# Use DOT to visualize this graph:
dg.write_to_graphic_file('jpg')

# add the node
dg.add_vertex(7)
dg.add_edge(5,7)

# Flip it and start at the first node
bfs = dg.reverse.bfs_iterator(7)
bfs.attach_distance_map
bfs.each do |v|
  dist = bfs.distance_to_root(v)
  break if dist > 3
  print v, ': ', dist, "\n"
end
dg.write_to_graphic_file('jpg')





#bfs = RGL::BFSIterator.new(dg)

# 1. Get a node ID
# 2. Start at root with a BFS
# 3. At each node if distance is less than 6 update weight
#


# Get distance


# Calculate Score
# Nodes Origional
=end

