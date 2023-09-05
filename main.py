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
    # This return goes to the end of program before if __name
    # return m_perc, f_perc


    m_perc = float(input("Number of male students: "))
    f_perc = float(input("Number of female students: "))
    total = m_perc + f_perc

    # You should develop your expression to get ratio of male students and female students
    # m_perc = number of male students / total students * 100
    # f_perc = number of female students / total students * 100
    
    
    print("Total number of students: ", int(total))
    print("The number of males and females: ", int(m_perc), int(f_perc))
    print(f'The percentages of males and females:\t{m_perc:.2f}, {f_perc:.2f}')


    # move here
    return m_perc, f_perc

if __name__ == '__main__':
    main()
