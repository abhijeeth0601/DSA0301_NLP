class FSA:
    def __init__(self):
        self.current_state = 'start'

    def transition(self, input_symbol):
        if self.current_state == 'start' and input_symbol == 'a':
            self.current_state = 'a'
        elif self.current_state == 'a' and input_symbol == 'b':
            self.current_state = 'ab'
        else:
            self.current_state = 'start'

    def is_accepted(self):
        return self.current_state == 'ab'


def match_pattern(input_string):
    fsa = FSA()
    for char in input_string:
        fsa.transition(char)
    return fsa.is_accepted()


# Test the FSA with example strings
strings_to_check = ["ab", "aab", "abcab", "defab", "abab"]
for string in strings_to_check:
    if match_pattern(string):
        print(f"'{string}' matches the pattern 'ab'")
    else:
        print(f"'{string}' does not match the pattern 'ab'")
