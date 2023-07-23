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
* Repeat:
    * If the frontier is empty, then there is no solution
    * Remove a node from the frontier
    * If the node contains goal state, return the solution
    * Otherwise, expand teh note, add resulting nodes to the frontier
