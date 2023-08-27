def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc
male = float(input("How many male students: "))
female = float(input("How many female students: "))
total = male + female
m_perc = male / 100
f_perc = female / 100
print("Total number of students: ", int(total))
print("The number of males and females: ", int(male), int(female))
print(f'The percentages of males and females:\t{m_perc:.2%}, {f_perc:.2%}')
if __name__ == '__main__':
    main()
