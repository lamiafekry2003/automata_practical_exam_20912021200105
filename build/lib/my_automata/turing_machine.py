def turing_machine(input_string):
    
   
    if not input_string:
        return True  
    for char in input_string:
        if char not in ['0', '1']:
            return False

   
    tape = ['_'] + list(input_string) + ['_']
    head = 1  
    state = 'q0'  

    while True:
        current_symbol = tape[head]

        if current_symbol not in ['0', '1', '_']:
            state = 'q_reject'

        if state == 'q0':
            if current_symbol == '0':
                head += 1
                state = 'q0'
            elif current_symbol == '1':
                head += 1
                state = 'q1'
            elif current_symbol == '_':
                state = 'q_accept'

        elif state == 'q1':
            if current_symbol == '0':
                head += 1
                state = 'q2'
            elif current_symbol == '1':
                head += 1
                state = 'q0'
            elif current_symbol == '_':
                state = 'q_reject'

        elif state == 'q2':
            if current_symbol == '0':
                head += 1
                state = 'q1'
            elif current_symbol == '1':
                head += 1
                state = 'q2'
            elif current_symbol == '_':
                state = 'q_reject'

        elif state == 'q_accept':
            return True

        elif state == 'q_reject':
            return False

if __name__ == "__main__":
    binary_input = input("ُEnter a binary number: ")
    if turing_machine(binary_input):
        print("number is divisible by 3")
    else:
        print("number is not divisible by 3")