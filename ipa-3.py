'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "Friends"
    elif to_member in social_graph[from_member]["following"]:
        return "Follower"
    elif from_member in social_graph[to_member]["following"]:
        return "Followed by"
    else:
        return "No relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    rows = len(board)
    cols = len(board[0])

    # Check rows
    for row in board: # For every row in board
        #Check if every symbol in the row is the same
        if all(symbol == row[0] for symbol in row) and row[0] != '':
            #If all symbols the same, return symbol (symbol is the winner)
            return row[0]

    # Check columns
    for col in range(cols):
        if all(board[row][col] == board[0][col] for row in range(rows)) and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if all(board[i][i] == board[0][0] for i in range(rows)) and board[0][0] != '':
        return board[0][0]

    if all(board[i][cols - i - 1] == board[0][cols - 1] for i in range(rows)) and board[0][cols - 1] != '':
        return board[0][cols - 1]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travelling = False
    travel_time = 0
    
    if first_stop == second_stop:
        return 0
    
    for route in route_map: #Iterate through possible routes
        if route[0] == first_stop: # Determine if start of leg is first stop
            travelling = True # Start the journey
            
        if travelling == True: # If journey has started, add travel time of the leg to ETA
            travel_time += route_map.get(route).get('travel_time_mins') 
            
            if route[1] == second_stop: # If end of leg is second stop end the journey
                travelling = False
                break
            
    # Edge case: If second stop is before first stop loop through routes again
    if travelling == True:
        for route in route_map:
            travel_time += route_map.get(route).get('travel_time_mins')
            if route[1] == second_stop:
                break
            
    return travel_time
