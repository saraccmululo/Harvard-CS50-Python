from plates import is_valid

def test_is_valid():
    # --- Valid plates ---
    assert is_valid("AB") == True              # minimal valid
    assert is_valid("AB123") == True           # letters + numbers at end
    assert is_valid("ab12") == True            # lowercase letters
    assert is_valid("HICS50") == True

    # --- Too short ---
    assert is_valid("") == False               # empty
    assert is_valid("A") == False              # single char

    # --- Beginning alphabetical checks ---
    assert is_valid("1ABC") == False           # starts with number
    assert is_valid("A1BC") == False           # second char not letter
    assert is_valid("123") == False

    # --- Number placement ---
    assert is_valid("AB1C") == False           # number in the middle
    assert is_valid("AB01") == False           # first number is 0
    assert is_valid("TRY022") == False         # number in the middle

    # --- Punctuation ---
    assert is_valid("HELLO!") == False         # contains punctuation
    assert is_valid("AB#12") == False          # contains punctuation

    # --- Edge cases ---
    assert is_valid("Make43L") == False        # number in middle, letter after number
    assert is_valid("XY0") == False            # number cannot start with 0
    assert is_valid("Xy12") == True            # valid lowercase + numbers at end

