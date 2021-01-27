def print_comparison(name, dates, times, original_data, computed_data):
    """
    Print a comparison of two time series (original and computed)

    Parameters:
        name: A string name for the data being compared (limited to 9 characters in length) 
        dates: A list of strings representing dates for each data
        times: A list of strings representing times for each data
        original_data: A list of original data (floats)
        computed_data: A list of computed data (floats)
    """
    #Output comparison
    print('                ORIGINAL  COMPUTED')
    print(f' DATE    TIME  {name.upper():>9} {name.upper():>9} DIFFERENCE')
    print('------- ------ --------- --------- ----------')
    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {diff:10.6f}')
