__Agent__ : Entity that perceives its environment and acts upon that environment.

__State__ : A configuration of the agent and its environment.

__Initial State__ : The state where the agent begins.

__Actions__ : Choices that can be made in a state. As a function, ACTIONS(s) returns the set of actions that can be executed in state _s_.

__Transition Model__ : A description of what state results from performaing any applicable action in any state. As a function RESULT(s, a) returns the state resulting from performing action _a_ in state _s_.