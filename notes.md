# Plan
## Solving puzzle
> State space representation

> Outputs 
(1) Case number.
(2) The number of moves to solve the case (i.e. the number of states – 1 in the
shortest path from the initial state to the goal).
(3) The number of nodes opened, that is, the number of yield made by the move
method during the search for a solution.
(4) The computing time the search took.


## IDDFS
- Depth first over n depths


> Algo
- Input state
- perform all moves
- repeat until goal or state = prev state
    * remember previous move
    * next state != state-1

