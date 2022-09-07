def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n-k)
    return numerator/denominator

 #one winnin number
def probability(n, a, b):
   
    n_combinations = combinations(a, b)
    
    probability = n / n_combinations
    percentage_form = probability * 100
    
    if n_tickets == 1:
        print('''Your chances to win the big prize with one ticket are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(percentage_form, int(n_combinations)))
    
    else:
        combinations_simplified = round(n_combinations / n)   
        print('''Your chances to win the big prize with {:,} different tickets are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(n_tickets, percentage_form,
                                                               combinations_simplified))
    
    
 #less than 6 winning numbers   
def probability_less_6(n_winning_numbers, a, b):
    
    n_combinations_ticket = combinations(a, n_winning_numbers)
    n_combinations_remaining = combinations(b, a - n_winning_numbers)
    successful_outcomes = n_combinations_ticket * n_combinations_remaining
    
    n_combinations_total = combinations(b, a)    
    probability = successful_outcomes / n_combinations_total
    
    probability_percentage = probability * 100    
    combinations_simplified = round(n_combinations_total/successful_outcomes)    
    print('''Your chances of having {} winning numbers with this ticket are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(n_winning_numbers, probability_percentage,
                                                               int(combinations_simplified)))
