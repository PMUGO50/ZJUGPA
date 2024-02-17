#yyq26314@outlook.com
#to read zju's scores from website and calculate average GPA

#import module
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

def getinfo(stuid, password):
    #set headless option as headless
    option=webdriver.FirefoxOptions()
    option.add_argument("--headless")

    #open website and prepare to log in
    driver=webdriver.Firefox(options=option)
    ur='http://zdbk.zju.edu.cn/jwglxt/xtgl/login_slogin.html'
    driver.get(ur)
    driver.find_element(By.XPATH,'//*[@id="ssodl"]').click()

    #clear username
    driver.find_element(By.XPATH,'//*[@id="username"]').clear()
    #input username:3210106014
    driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(stuid)
    #clear password
    driver.find_element(By.XPATH,'//*[@id="password"]').clear()
    #input password
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    #log in
    driver.find_element(By.XPATH,'//*[@id="dl"]').click()

    #clear tip window
    loop = 1
    while loop:
        try:
            sleep(0.5)
            driver.find_element(By.XPATH,'//*[@id="btn_cancel"]').click()
        except:
            sleep(0.5)
            loop = 0

    #get to the score's site
    driver.find_element(By.XPATH,'/html/body/div[2]/div/nav/div[2]/div[2]/ul/li[5]/a').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[6]/div[1]/div[2]').click()

    #wait 0.5s in order to operate on the score's page successfully
    #then switch to new page to sign in
    sleep(0.5)
    lst=driver.window_handles #get list of web page
    driver.switch_to.window(lst[len(lst)-1])
    
    #scroll page to choose number of items that can be seen in the table
    sleep(1)
    target_temp = driver.find_element_by_id('pager')
    driver.execute_script("arguments[0].scrollIntoView();", target_temp)
    sleep(2) #wait for scrolling finished
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[8]/select').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[5]/div/table/tbody/tr/td[2]/table/tbody/tr/td[8]/select/option[16]').click()

    #generate a DataFrame from the table of score
    sleep(1)
    htm=driver.page_source
    data=pd.read_html(htm)[1]

    #quit the broswer
    driver.quit()
    return data

def dataprocess(data):
    #calculate average GPA
    total=0
    cre_total=0
    major=0
    cre_major=0
    for i in range(1,len(data)):
        total=total+float(data.at[i,3])*float(data.at[i,4])
        cre_total=cre_total+float(data.at[i,3])
        if ord('0')<=ord(data.at[i,0][18])<=ord('9') and data.at[i,0][14:22]!='32190010':#major or not
            major=major+float(data.at[i,3])*float(data.at[i,4])
            cre_major=cre_major+float(data.at[i,3])
    total=total/cre_total
    major=major/cre_major

    #output as csv
    datahead = pd.DataFrame([['课程号', '课程名', '成绩', '学分', '绩点']])
    data = datahead._append(data.loc[1:]).loc[:,:4]
    data.to_csv('gpa_auto.csv',sep=',',index=False,header=False,encoding='ansi')
    fl=open('gpa_auto.csv','a',encoding='ansi')
    fl.write('\n'+'The Average GPA is '+str('{:.2f}'.format(total))+'; The Total Credit is '+str('{:.1f}'.format(cre_total))+'\n')
    fl.write('\n'+'The Average Major GPA is '+str('{:.2f}'.format(major))+'; The Total Major Credit is '+str('{:.1f}'.format(cre_major)))
    fl.close()

    return total, cre_total, major, cre_major


