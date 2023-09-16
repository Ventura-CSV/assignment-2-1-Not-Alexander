def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_perc = float(input("Number of male students: "))
    f_perc = float(input("Number of female students: "))
    total = m_perc + f_perc
    print("Total number of students: ", int(total))
    print("The number of males and females: ", int(m_perc), int(f_perc))
    print(f'The percentages of males and females:\t{m_perc:.2f}, {f_perc:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc
if __name__ == '__main__':
    main()
