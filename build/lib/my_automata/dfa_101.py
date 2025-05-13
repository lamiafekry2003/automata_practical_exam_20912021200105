def dfa_101(input_string):
    
    current_state = 'q0'
    
    for char in input_string:
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

if __name__ == "__main__":
    binery_string=input("Enter a binary string: ")
    if dfa_101( binery_string):
        print("Accepted")
    else:
        print( "Rejected")