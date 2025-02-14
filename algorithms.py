from math import ceil
import heapq

def heuristic(capacities : list[int], current_amount : int, target : int) -> int:
    """
    Calculates the theoretical and approximate minimum number of steps required for reaching the target.
    
    Args:
        capacities : list[int]
            Capacities of the pitchers.
        current_amount : int
            The current amount of water in the destination.
        target : int
            The desired quantity of water in the destination.
    
    Returns:
        int : the number of steps required to reach or surpass the target by only using the largest pitcher.
    """
    max_capacity = max(capacities) if capacities else 0

    if max_capacity == 0:
        return float('inf') if current_amount != target else 0

    error     = abs(target - current_amount)
    min_steps = ceil(error / max_capacity)
    
    return min_steps

def water_pitcher_solver(capacities : list[int], target : int, bounding_coefficient : int = 2) -> int:
    """
    Solves the water pitcher problem using A* algorithm.

    Args:
        capacities : list[int]
            Capacities of the pitchers.
        target : int
            The target quantity in the destination.
        bounding_coefficient : int
            Prevents the model from running too far away from the target. 
            Used as the multiplying factor for the `overshoot = max_pitcher * bounding_coefficient`

    Returns:
        The minimum number of steps to reach the target, or -1 if no path exists.
    """

    # trivial cases
    if not capacities and target != 0:
        return -1
    if not capacities and target == 0:
        return 0

    if target < 0:
        return -1

    if target == 0:
        return 0

    # setup
    start_state = 0
    max_capacity = max(capacities)

    pq = [(
        heuristic(capacities, start_state, target),  # f_score
        0,                                           # g_score
        start_state                                  # state
        )]  
    
    visited = set()
    visited.add(start_state)

    # running the search
    while pq:
        f_score, g_score, current_state = heapq.heappop(pq)

        # reached the goal
        if current_state == target:
            return g_score

         # Check whether there existis a path possible from here according to heuristic
        if ( f_score == float('inf') ) and ( current_state != target ):
            continue

        for capacity in capacities:

            # Pour out (subtract)
            next_state_sub = max(0, current_state - capacity)

            if next_state_sub not in visited:

                visited.add(next_state_sub)
                new_g_score = g_score + 1 # as we have decided to take a step forward, the current amount of steps increases by 1 

                new_h_score = heuristic(capacities, next_state_sub, target)
                new_f_score = new_g_score + new_h_score

                heapq.heappush(pq, (new_f_score, new_g_score, next_state_sub))

            # Pour in (add)
            next_state_add = current_state + capacity
            
            # Simple bound to avoid running too far away from the target
            if ( next_state_add > target + max_capacity * bounding_coefficient ): 
               continue

            if next_state_add not in visited: 
                
                visited.add(next_state_add)
                new_g_score = g_score + 1 # as we have decided to take a step forward, the current amount of steps increases by 1 

                new_h_score = heuristic(capacities, next_state_add, target)
                new_f_score = new_g_score + new_h_score

                heapq.heappush(pq, (new_f_score, new_g_score, next_state_add))

    return -1 # default case, no path found

