import heapq

class Node:
    def __init__(self, x, y, cost, heuristic, parent=None):
        self.x = x
        self.y = y
        self.cost = cost  # Cost from start to this node
        self.heuristic = heuristic  # Estimated cost from this node to goal
        self.parent = parent  # Parent node in the path

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def heuristic(a, b):
    # Use Manhattan distance as heuristic
    return abs(a.x - b.x) + abs(a.y - b.y)

def astar(start_pos, goal_pos, obstacles):
    # Create a priority queue and add the start node
    open_list = []
    start_node = Node(start_pos[0], start_pos[1], 0, 0)
    goal_node = Node(goal_pos[0], goal_pos[1], 0, 0)
    heapq.heappush(open_list, start_node)

    # Keep track of visited positions
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if (current_node.x, current_node.y) == (goal_node.x, goal_node.y):
            # Reconstruct path
            path = []
            while current_node.parent:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add((current_node.x, current_node.y))

        # Generate neighbors (up, down, left, right)
        neighbors = [
            (current_node.x, current_node.y - 1),
            (current_node.x, current_node.y + 1),
            (current_node.x - 1, current_node.y),
            (current_node.x + 1, current_node.y),
        ]

        for pos in neighbors:
            x, y = pos
            if x < 0 or x > 597 or y < 0 or y > 597:
                continue  # Skip positions outside the map
            if pos in obstacles or pos in closed_set:
                continue  # Skip obstacles and visited positions

            neighbor_node = Node(
                x, y,
                current_node.cost + 1,
                heuristic(Node(x, y, 0, 0), goal_node),
                current_node
            )
            heapq.heappush(open_list, neighbor_node)

    return None  # No path found