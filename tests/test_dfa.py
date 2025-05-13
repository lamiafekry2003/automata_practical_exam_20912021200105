from my_automata.dfa_101 import dfa_101

def test_dfa_101():
   
    # Test cases
    test_cases = [
        ("01010", True),  # Contains '101'
        ("1101", True),   # Contains '101'
        ("1100", False),  # Does not contain '101'
        ("100", False),   # Does not contain '101'
        ("101010", True), # Contains '101'
        ("000", False),   # Does not contain '101'
        ("111", False),   # Does not contain '111'
        ("", False),      # Empty string
        ("1", False),     # Single character
        ("0", False),     # Single character
        ("abc", False),   # Non-binary input
    ]

    for input_string, expected in test_cases:
        assert dfa_101(input_string) == expected, f"Failed for input: {input_string}"
    
    print("All DFA tests passed!")

if __name__ == "__main__":
    test_dfa_101()