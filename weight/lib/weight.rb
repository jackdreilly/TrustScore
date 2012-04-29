class Weight

  attr_accessor :graph

  INCREMENT = 10
  DEGREES_OF_SEPERATION   = 3

  def initialize(graph)
    @graph = graph
  end   

  def adjust_weights(start_node, success)
    @bfs = @graph.reverse.bfs_iterator(start_node)
    @bfs.attach_distance_map
    distance = 0
    while distance < DEGREES_OF_SEPERATION 
      current_node  = @bfs.forward
      distance      = @bfs.distance_to_root(current_node)
      reweight_node(current_node, distance, success)
    end
  end

  def reweight_node(current_node, distance, success)    
    if success
      current_node.weight += INCREMENT/(distance + 1)
    else
      current_node.weight -= INCREMENT/(distance + 1)
    end
  end

end
