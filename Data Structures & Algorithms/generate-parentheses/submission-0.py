class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the result list to store valid combinations of parentheses
        res = []
        
        # Define the backtrack function
        def backtrack(open_n, closed_n, path):
            # Base case: if the number of open and closed parentheses equals n,
            # we have a valid combination
            if open_n == closed_n == n:
                res.append(path)  # Add the current valid combination to the result
                return
            
            # If we can still add an open parenthesis
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")  # Add an open parenthesis
            
            # If we can add a closed parenthesis without exceeding the number of open ones
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")  # Add a closed parenthesis
        
        # Start backtracking with 0 open and 0 closed parentheses, and an empty path
        backtrack(0, 0, "")
        
        return res  # Return the list of valid parentheses combinations
