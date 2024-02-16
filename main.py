import auto
import pandas as pd

if __name__ == "__main__":
    signal = 'x'
    stuinfo = pd.read_csv("stuinfo.csv",encoding='ansi', header=None, index_col=0)
    print("Hello, " + stuinfo.loc['stuid', 1])
    print("The program need to open website, which may cause time delay, please wait patiently.\n"+\
          "Also, program is not very stable, so if any error is returned, please rerun the program several times until nothing wrong.")
    data = auto.getinfo(stuinfo.loc['stuid', 1], stuinfo.loc['password', 1])
    total, cre_total, major, cre_major = auto.dataprocess(data)

    #print result
    print('The Average GPA is '+str('{:.2f}'.format(total))+'; The Total Credit is '+str('{:.1f}'.format(cre_total)))
    print('The Average Major GPA is '+str('{:.2f}'.format(major))+'; The Total Major Credit is '+str('{:.1f}'.format(cre_major)))
    print("GPA information is stored in 'gpa_auto.csv'. Program finished, farewell.")
    input()