def is_duplicated_char(text):
    """ Verify that exists duplicated chars in the text"""
    return len(set(text)) != len(text)
