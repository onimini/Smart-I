'''Calculate score for Smart-I examination.'''
def score(math, eng, read, social):
    '''input score of subject in parameter
    then calculate score from percent of subject which
    math eng and read will multi with 0.3
    social multi with 0.1 then find all plus.'''
    calculate = (math + eng + read) * 0.3
    total = social * 0.1
    summary = calculate + total
    if summary >= 63:
        print str(summary) + ' Maybe pass the exam.'
    else:
        print str(summary) + ' Maybe not pass the exam.'
score(input(), input(), input(), input())
