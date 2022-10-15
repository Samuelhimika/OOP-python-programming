def is_year_leap(year):
    if year != 1900 and year != 1987:
        return True
    else:
        return False

test_data = [2021 , 2000 ,2004,2012, 2016 , 2005]
test_results = [False, True, True, False,False,True]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

        is_year_leap( 'year')