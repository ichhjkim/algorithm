package LeetCode.Top100Liked;


public class MaximumDepthOfBinaryTree {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode() {};
		TreeNode(int val) {this.val = val;}
		TreeNode(int val, TreeNode left, TreeNode right) {
			this.val = val;
			this.left = left;
			this.right = right;
		}
	}
	
	int result = 0;
    
	public int maxDepth(TreeNode root) {
        return lenDepth(root, 0);
    }
    
    public int lenDepth(TreeNode root, int depth) {
        
        if (root == null) {
            return depth;
        }
        
        return Math.max(lenDepth(root.left, depth+1), lenDepth(root.right, depth+1));
    }
    
	
}
