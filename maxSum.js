
class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

const maxPathSum = (root) => {
    if (!root) return 0;
    debugger

    let maxSum = -Infinity;
    const stack = [{ node: root, leftSum: 0, rightSum: 0 }];

    while (stack.length > 0) {
        const { node, leftSum, rightSum } = stack.pop();
                // 3 , 0 , 0
                // 4 , 3 ,3

        // Calculate the maximum path sum interval
        const intervalSum = node.val + leftSum + rightSum;
        maxSum = Math.max(maxSum, intervalSum);

        // Push the left child onto the stack
        if (node.left) {
            stack.push({
                node: node.left,
                leftSum: Math.max(leftSum + node.val, 0),
                rightSum: Math.max(rightSum + node.val, 0),
            });
        }

        // Push the right child onto the stack
        if (node.right) {
            stack.push({
                node: node.right,
                leftSum: Math.max(leftSum + node.val, 0),
                rightSum: Math.max(rightSum + node.val, 0),
            });
        }
    }

    return maxSum;
};


a = new Node(3)
b = new Node(11)
c = new Node(4)
d = new Node(4)
e = new Node(-2)
f = new Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

// #       3
// #    /    \
// #   11     4
// #  / \      \
// # 4   -2     1

console.log(maxPathSum(a))
