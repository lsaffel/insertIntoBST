class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = TreeNode(value)
      else:
        self.left.insert(value)
    else:              # therefore, the value is >= the node's value
      if self.right is None:
        self.right = TreeNode(value)
      else:
        self.right.insert(value)
