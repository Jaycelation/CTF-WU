class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [None] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = (arr[start], arr[start], arr[start], arr[start])
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])

    def merge(self, left, right):
        total_sum = left[0] + right[0]
        max_prefix = max(left[1], left[0] + right[1])
        max_suffix = max(right[2], right[0] + left[2])
        max_subarray = max(left[3], right[3], left[2] + right[1])
        return (total_sum, max_prefix, max_suffix, max_subarray)

    def update(self, index, value, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        
        if start == end:
            self.tree[node] = (value, value, value, value)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if index <= mid:
                self.update(index, value, left_child, start, mid)
            else:
                self.update(index, value, right_child, mid + 1, end)
            
            self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])

    def query(self, l, r, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        
        if r < start or l > end:
            return (0, float('-inf'), float('-inf'), float('-inf'))
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_result = self.query(l, r, left_child, start, mid)
        right_result = self.query(l, r, right_child, mid + 1, end)
        
        return self.merge(left_result, right_result)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split("\n")
    
    N, Q = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    segment_tree = SegmentTree(arr)
    
    result = []
    for i in range(2, len(data)):
        if not data[i]:
            continue
        query = data[i].split()
        if query[0] == "U":
            index = int(query[1]) - 1
            value = int(query[2])
            segment_tree.update(index, value)
        elif query[0] == "Q":
            l, r = int(query[1]) - 1, int(query[2]) - 1
            result.append(str(segment_tree.query(l, r)[3]))
    
    sys.stdout.write("\n".join(result) + "\n")
