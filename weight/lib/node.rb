class Node

  attr_accessor :node_id, :weight

  def initialize(id=nil, weight=nil)
    @node_id  = id
    @weight   = weight
  end

  def ==(node)
    self.class == node.class && self.node_id == node.node_id
  end

  def <=>(node)
    self.node_id <=> node.node_id 
  end

end

