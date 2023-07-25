__Agent__ : Entity that perceives its environment and acts upon that environment.

__State__ : A configuration of the agent and its environment.

__Initial State__ : The state where the agent begins.

__Actions__ : Choices that can be made in a state. As a function, ACTIONS(s) returns the set of actions that can be executed in state _s_.

__Transition Model__ : A description of what state results from performaing any applicable action in any state. As a function RESULT(s, a) returns the state resulting from performing action _a_ in state _s_.

__State Space__ : The set of all states reachable from the initial state by any sequence of actions. Often represented as a graph.

__Goal Test__ : Way to determine whether a given state is a goal state.

__Path Cost__ : Numerical cost associated with a given path.

__Solution__ : A sequence of actions that leads from the initial state to the goal state.

__Optimal Solution__ : A solution that has the lowest path cost among all solutions.

A __Node__ can be a useful data structure to store the information needed to solve a search problem. It's a data structure that keeps track of:

* A state
* A parent (a note that generated this node)
* An action (action applied to parent to get node)
* A path cost (from initial state to node)

A search problem has:
* initial state
* actions
* transition model
* goal test
* path cost function

An approach to solving search problems is as follows:
* Start with a frontier that contains the initial state (that's the only state we know about at the beginning)
* Start with an empty explored set
* Repeat:
    * If the frontier is empty, then there is no solution
    * Remove a node from the frontier
    * If the node contains goal state, return the solution
    * Otherwise, add the node to the explored set
    * Expand the node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set.

How you remove nodes from the frontier and store them matters. For example, if you use a stack to store items, the algorithm will use depth-first search, since the last items added to the frontier are searched first (LIFO). On the other hand, you can achieve breadth-first search by using a queue to store the frontier.

__Depth-First Search (DFS)__ : Search algorithm that always expands the deepest node in the frontier.

__Breadth-First Search (BFS)__ : Search algorithm that always expands the shallowest node in the frontier.

__Uninformed Search__ : Search strategy that uses no problem-specific knowledge (DFS, BFS).

__Informed Search__ : Search strategy that uses problem-specific knowledge to find solutions more efficiently. For example, in a maze problem using information about the distance between current location and the goal state. There are a number of informed search algorithms.

__Greedy Best-First Search__ : Search algorithm that expands the node that it thinks is closest to the goal, as estimated by a heuristic function _h(n)_

__A* Search__ : Search algorithm that expands node with lowest value of _g(n) + h(n)_ where _g(n) = cost to reach node_ and _h(n) = estimates cost to goal_. A* is an optimal search algorithm if the following conditions are met:
* _h(n)_ is admissible (never overestimates the true cost), and
* _h(n)_ is consistent (for every node _n_ and successor _n'_ with step cost _c_, _h(n) <= h(n') + c)_

__Minimax__ : In a two player game for example, the Max player aims to maximize their score and the Min player aims to minimize their score. Each outcome of the game is assigned a point value.

Implementing a game could use the following functions:
* _S0_: Initial state
* _Player(s)_: Returns which player to move in state _s_
* _Action(s)_: Returns legal moves in state _s_
* _Result(s, a)_: Returns state after action _a_ taken in state _s_
* _Terminal(s)_: Checks if state _s_ is a terminal state
* _Utility(s)_: Final numerical value for terminal state _s_