from my_automata.turing_machine import turing_machine

def test_turing_machine():
    """
    Test the Turing Machine that accepts binary numbers divisible by 3.
    """
    test_cases = [
        ("", True),        # 0 (divisible by 3)
        ("0", True),       # 0 (divisible by 3)
        ("11", True),      # 3 (divisible by 3)
        ("110", True),     # 6 (divisible by 3)
        ("1001", True),    # 9 (divisible by 3)
        ("10", False),     # 2 (not divisible by 3)
        ("100", False),    # 4 (not divisible by 3)
        ("101", False),    # 5 (not divisible by 3)
        ("111", False),    # 7 (not divisible by 3)
        ("abc", False),    # Invalid input
    ]

    for input_string, expected in test_cases:
        assert turing_machine(input_string) == expected, f"Failed for input: {input_string}"
    
    print("All Turing Machine tests passed!")

if __name__ == "__main__":
    test_turing_machine()