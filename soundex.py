from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.initial_state = 'start'

    #add the intermidiate states 
    f1.add_state('first_character')
    f1.add_state('non_initial_remover')
    f1.add_state('group_1')
    f1.add_state('group_2')
    f1.add_state('group_3')
    f1.add_state('group_4')
    f1.add_state('group_5')
    f1.add_state('group_6') 

    # Set all the final states
    f1.set_final('non_initial_remover')
    f1.set_final('group_1')
    f1.set_final('group_2')
    f1.set_final('group_3')
    f1.set_final('group_4')
    f1.set_final('group_5')
    f1.set_final('group_6')

    # Add the rest of the arcs
    for letter in string.ascii_lowercase + string.ascii_uppercase:

        if letter in ['a', 'e', 'i', 'o', 'u', 'h', 'w', 'y', 'A', 'E', 'I', 'O', 'U', 'H', 'W', 'Y']:
            f1.add_arc('start','first_character', (letter), (letter))
            f1.add_arc('first_character', 'non_initial_remover', (letter), ())
            f1.add_arc('non_initial_remover', 'non_initial_remover', (letter),())
            f1.add_arc('group_1', 'non_initial_remover', (letter), ())
            f1.add_arc('group_2', 'non_initial_remover', (letter), ())
            f1.add_arc('group_3', 'non_initial_remover', (letter), ())
            f1.add_arc('group_4', 'non_initial_remover', (letter), ())
            f1.add_arc('group_5', 'non_initial_remover', (letter), ())
            f1.add_arc('group_6', 'non_initial_remover', (letter), ())

        if letter in ['b', 'f', 'p', 'v', 'B', 'F', 'P', 'V']:
            f1.add_arc('start','first_character', (letter), (letter))
            f1.add_arc('first_character','group_1', (letter), ('1'))
            f1.add_arc('non_initial_remover','group_1', (letter), ('1'))
            f1.add_arc('group_2','group_1', (letter), ('1'))
            f1.add_arc('group_3','group_1', (letter), ('1'))
            f1.add_arc('group_4','group_1', (letter), ('1'))
            f1.add_arc('group_5','group_1', (letter), ('1'))
            f1.add_arc('group_6','group_1', (letter), ('1'))
            f1.add_arc('group_1', 'group_1', (letter), ())

        if letter in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z', 'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z']:
            f1.add_arc('start','first_character', (letter), (letter))
            f1.add_arc('first_character','group_2', (letter), ('2'))
            f1.add_arc('non_initial_remover', 'group_2',(letter), ('2'))
            f1.add_arc('group_1','group_2', (letter), ('2'))
            f1.add_arc('group_3','group_2', (letter), ('2'))
            f1.add_arc('group_4','group_2', (letter), ('2'))
            f1.add_arc('group_5','group_2', (letter), ('2'))
            f1.add_arc('group_6','group_2', (letter), ('2'))
            f1.add_arc('group_2', 'group_2', (letter), ())

        if letter in ['d', 't', 'D', 'T']:
            f1.add_arc('start','first_character', (letter), (letter))
            f1.add_arc('first_character','group_3', (letter), ('3'))
            f1.add_arc('non_initial_remover', 'group_3',(letter), ('3'))
            f1.add_arc('group_1','group_3', (letter), ('3'))
            f1.add_arc('group_2','group_3', (letter), ('3'))
            f1.add_arc('group_4','group_3', (letter), ('3'))
            f1.add_arc('group_5','group_3', (letter), ('3'))
            f1.add_arc('group_6','group_3', (letter), ('3'))
            f1.add_arc('group_3', 'group_3', (letter), ())

        if letter in ['l', 'L']:
            f1.add_arc('start','first_character', (letter), (letter))
            f1.add_arc('first_character','group_4', (letter), ('4'))
            f1.add_arc('non_initial_remover', 'group_4',(letter), ('4'))
            f1.add_arc('group_1','group_4', (letter), ('4'))
            f1.add_arc('group_2','group_4', (letter), ('4'))
            f1.add_arc('group_3','group_4', (letter), ('4'))
            f1.add_arc('group_5','group_4', (letter), ('4'))
            f1.add_arc('group_6','group_4', (letter), ('4'))
            f1.add_arc('group_4', 'group_4', (letter), ())

        if letter in ['m', 'n', 'M', 'N']:
            f1.add_arc('start','first_character', (letter), (letter))
            f1.add_arc('first_character','group_5', (letter), ('5'))
            f1.add_arc('non_initial_remover', 'group_5',(letter), ('5'))
            f1.add_arc('group_1','group_5', (letter), ('5'))
            f1.add_arc('group_2','group_5', (letter), ('5'))
            f1.add_arc('group_3','group_5', (letter), ('5'))
            f1.add_arc('group_4','group_5', (letter), ('5'))
            f1.add_arc('group_6','group_5', (letter), ('5'))
            f1.add_arc('group_5', 'group_5', (letter), ())     

        if letter in ['r', 'R']:
            f1.add_arc('start','first_character', (letter), (letter))
            f1.add_arc('first_character','group_6', (letter), ('6'))
            f1.add_arc('non_initial_remover', 'group_6',(letter), ('6'))
            f1.add_arc('group_1','group_6', (letter), ('6'))
            f1.add_arc('group_2','group_6', (letter), ('6'))
            f1.add_arc('group_3','group_6', (letter), ('6'))
            f1.add_arc('group_4','group_6', (letter), ('6'))
            f1.add_arc('group_5','group_6', (letter), ('6'))
            f1.add_arc('group_6', 'group_6', (letter), ())     

    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('start')
    f2.initial_state = 'start'
    
    f2.add_state('first_number')
    f2.add_state('second_number')
    f2.add_state('third_number')
    f2.add_state('fourth_number')

    f2.set_final('first_number')
    f2.set_final('second_number')
    f2.set_final('third_number')
    f2.set_final('fourth_number')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('start', 'start', (letter), (letter))

    for n in range(10):
        f2.add_arc('start', 'first_number', (str(n)), (str(n)))
        f2.add_arc('first_number', 'second_number', (str(n)), (str(n)))
        f2.add_arc('second_number', 'third_number', (str(n)), (str(n)))
        f2.add_arc('third_number', 'fourth_number', (str(n)), ())
        f2.add_arc('fourth_number', 'fourth_number', (str(n)), ())

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('start')
    f3.add_state('from_first_number')
    f3.add_state('from_second_number')
    f3.add_state('from_third_number')
    
    f3.add_state('first_zero_append')
    f3.add_state('second_zero_append')
    f3.add_state('third_zero_append')

    f3.initial_state = 'start'
    f3.set_final('from_third_number')
    f3.set_final('third_zero_append')

    for letter in string.letters:
        f3.add_arc('start', 'start', (letter), (letter))

    f3.add_arc('start', 'first_zero_append', (), ('0'))
    f3.add_arc('first_zero_append', 'second_zero_append', (), ('0'))
    f3.add_arc('second_zero_append', 'third_zero_append', (), ('0'))
    f3.add_arc('from_first_number', 'second_zero_append', (), ('0'))
    f3.add_arc('from_second_number', 'third_zero_append', (), ('0'))


    for number in xrange(10):
        f3.add_arc('start', 'from_first_number', (str(number)), (str(number)))
        f3.add_arc('from_first_number', 'from_second_number', (str(number)), (str(number)))
        f3.add_arc('from_second_number', 'from_third_number', (str(number)), (str(number)))
    
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
