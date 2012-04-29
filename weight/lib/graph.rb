class Graph

  attr_accessor :nodes, :graph
  
  DEFAULT_WEIGHT = 10

  def initialize(data=[])
    @graph = RGL::DirectedAdjacencyGraph.new
    @data  = data   
    @nodes = {} 
    intialize_nodes
    populate_nodes
    generate_graph
  end
  
  def intialize_nodes
    @data.collect{|x| [x[0], x[1]]}.flatten.uniq.each{|y| @nodes[y] = Node.new(y, DEFAULT_WEIGHT)}
  end
  
  def populate_nodes
    @data.each{|w| @nodes[w[0]] = Node.new(w[0], w[1])}
  end

  def generate_graph
    @data.each do |a|
      @graph.add_edge(@nodes[a[0]], @nodes[a[1]])
    end
  end

  def append_vertex(append_to, weight)
    node_id = @nodes.keys.sort[-1] + 1
    @nodes[node_id] = Node.new(node_id, weight)
    @graph.add_edge(@nodes[append_to], @nodes[node_id])
  end

  def draw
    @graph.write_to_graphic_file('jpg')
  end

end

