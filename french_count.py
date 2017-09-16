import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.initial_state = 'start'

    f.add_state('hundred')
    f.add_state('zero_at_hundredth')
    f.add_state('zero_tenth')
    f.add_state('zero_zero')
    f.add_state('one_tenth')
    f.add_state('two_to_sixth_tenth')
    f.add_state('seven_tenth')
    f.add_state('eigth_tenth')
    f.add_state('nine_tenth')
    f.add_state('units')

    f.set_final('units')

    for ii in xrange(10):
        if ii  == 0:
            f.add_arc('start', 'zero_at_hundredth', [str(ii)] , ())
            f.add_arc('zero_at_hundredth', 'zero_zero', [str(ii)], ())
            f.add_arc('zero_zero', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('zero_tenth', 'units', [str(ii)], ())
            f.add_arc('hundred', 'zero_tenth', [str(ii)], ())
            f.add_arc('one_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('two_to_sixth_tenth', 'units', [str(ii)], ())
            f.add_arc('seven_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('eigth_tenth', 'units', [str(ii)], ())
            f.add_arc('nine_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10]])

        if ii == 1:
            f.add_arc('start', 'hundred', [str(ii)], [kFRENCH_TRANS[100]])
            f.add_arc('hundred', 'one_tenth', [str(ii)], ())
            f.add_arc('zero_at_hundredth', 'one_tenth', [str(ii)], ())
            f.add_arc('zero_zero', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('zero_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('one_tenth', 'units', [str(ii)], [kFRENCH_TRANS[11]])
            f.add_arc('two_to_sixth_tenth', 'units', [str(ii)], [kFRENCH_AND + ' ' + kFRENCH_TRANS[ii]])
            f.add_arc('seven_tenth', 'units', [str(ii)], [kFRENCH_AND + ' ' + kFRENCH_TRANS[10 + ii]])
            f.add_arc('eigth_tenth', 'units', [str(ii)], [kFRENCH_AND + ' ' + kFRENCH_TRANS[ii]])
            f.add_arc('nine_tenth', 'units', [str(ii)], [kFRENCH_AND + ' ' + kFRENCH_TRANS[11]])

        if ii >=2 and ii <=6:
            f.add_arc('start', 'hundred', [str(ii)], [ kFRENCH_TRANS[ii] + ' ' + kFRENCH_TRANS[100]])
            f.add_arc('hundred', 'two_to_sixth_tenth', [str(ii)], [kFRENCH_TRANS[ii * 10]])
            f.add_arc('zero_at_hundredth', 'two_to_sixth_tenth', [str(ii)], [kFRENCH_TRANS[ii * 10]])
            f.add_arc('zero_zero', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('zero_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('one_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10 + ii]])
            f.add_arc('two_to_sixth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('seven_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii + 10]])
            f.add_arc('eigth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('nine_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii + 10]])

        if ii == 7:
            f.add_arc('start', 'hundred', [str(ii)], [kFRENCH_TRANS[ii] + ' ' + kFRENCH_TRANS[100]])
            f.add_arc('hundred', 'seven_tenth', [str(ii)], [kFRENCH_TRANS[60]])
            f.add_arc('zero_at_hundredth', 'seven_tenth', [str(ii)], [kFRENCH_TRANS[60]])
            f.add_arc('zero_zero', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('zero_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('one_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]] )
            f.add_arc('two_to_sixth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('seven_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]])
            f.add_arc('eigth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('nine_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]]) 

        if ii == 8:
            f.add_arc('start', 'hundred', [str(ii)], [ kFRENCH_TRANS[ii] + ' ' + kFRENCH_TRANS[100]])
            f.add_arc('hundred', 'eigth_tenth', [str(ii)], [kFRENCH_TRANS[4] + ' ' + kFRENCH_TRANS[20]])
            f.add_arc('zero_at_hundredth', 'eigth_tenth', [str(ii)], [kFRENCH_TRANS[4] + ' ' + kFRENCH_TRANS[20]])
            f.add_arc('zero_zero', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('zero_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('one_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]])
            f.add_arc('two_to_sixth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('seven_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]])
            f.add_arc('eigth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('nine_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]])    

        if ii == 9:
            f.add_arc('start', 'hundred', [str(ii)], [kFRENCH_TRANS[ii] + ' ' + kFRENCH_TRANS[100]])
            f.add_arc('hundred', 'nine_tenth', [str(ii)], [kFRENCH_TRANS[4] + ' ' + kFRENCH_TRANS[20]])
            f.add_arc('zero_at_hundredth', 'nine_tenth', [str(ii)], [kFRENCH_TRANS[4] + ' ' + kFRENCH_TRANS[20]])
            f.add_arc('zero_zero', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('zero_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('one_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]])
            f.add_arc('two_to_sixth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('seven_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]])
            f.add_arc('eigth_tenth', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('nine_tenth', 'units', [str(ii)], [kFRENCH_TRANS[10] + ' ' + kFRENCH_TRANS[ii]]) 

    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
