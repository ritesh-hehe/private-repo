# Write a program that computes the sum of an alternating series where each element of the series is
# an expression of the form ((−1)k+1)/(2\*k−1) for each value of k from 1 to a million, multiplied by 4.
# Or, in more mathematical notation


# NOTE: The value is close to pi, that is till two decimal places. I have rechecked it to see if I did
# anything wrong, but I cannot find any issue. Still, pi at the end, is still a pi(e)....hehe get it?
def calc_series() -> None:
    series_sum = 0
    for k in range(1, int(10e6+1)):
        series_sum = series_sum + (((-1)**(k+1))/(2*k - 1))
    return 4 * series_sum


print(calc_series())
