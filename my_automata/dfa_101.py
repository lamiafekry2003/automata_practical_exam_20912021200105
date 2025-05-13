"""
    DFA that accepts binary strings containing the substring '101' at least once.
    Args:
        input_string (str): Binary string consisting of '0' and '1'.
    Returns:
        bool: True if the string is accepted, False otherwise.
    """
def dfa_101(input_string):
    current_state = 'q0'
    for char in input_string:
        # Check if the character is not '0' or '1', if so, return False
        if char not in ['0', '1']:
            return False  
       
        if current_state == 'q0':
            
            if char == '1':
                current_state = 'q1'
            
            else:  
                current_state = 'q0'
        
        elif current_state == 'q1':
            
            if char == '0':
                current_state = 'q2'
            
            else:  
                current_state = 'q1'
        
        elif current_state == 'q2':

            if char == '1':
                current_state = 'q3'
           
            else:  
                current_state = 'q0'
        
        elif current_state == 'q3':
            current_state = 'q3' 
       
    return current_state == 'q3'
# The DFA accepts the string if it ends in state 'q3' (found "101")

# Check if the script is being run directly
if __name__ == "__main__":
    binery_string=input("Enter a binary string: ")
    if dfa_101( binery_string):
        print("Accepted")
    else:
        print( "Rejected")