class Weight

  attr_accessor :graph

  INCREMENT = 10
  DEGREES   = 3

  def initialize(graph)
    @graph = graph
  end   

  def reweight(start, success)
    @bfs = @graph.reverse.bfs_iterator(start)
    debugger
    puts "Whats up"
  end
  
end
