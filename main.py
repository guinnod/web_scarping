import undetected_chromedriver
import time

try:
    start_second = time.time()
    start_time = start_second
    # for executing driver without gui
    options = undetected_chromedriver.ChromeOptions()
    options.add_argument('--headless')
    # initializing driver
    driver = undetected_chromedriver.Chrome(options)
    print('Executed! Time: ' + str(time.time() - start_second))
    start_second = time.time()
    # getting page
    driver.get('https://kz.blsspainvisa.com/russian/book_appointment.php')
    print('We have got page! Time: ' + str(time.time() - start_second))
    start_second = time.time()
    # to skip security checking
    time.sleep(2)
    print('Verify code page opened! Time: ' + str(time.time() - start_second))
    start_second = time.time()
    # filling data to get verify code
    driver.execute_script('document.getElementsByTagName(\'input\')[0].click()')
    driver.execute_script('document.getElementsByTagName(\'select\')[1].value = \'35#56\'')
    driver.execute_script('getAppService(\'35#56\')')
    # to do required functions
    time.sleep(0.5)
    print('Function has done! Time: ' + str(time.time() - start_second))
    driver.execute_script('document.getElementsByTagName(\'select\')[2].value = \'Normal\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[2].value = \'+7\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[3].value = \'7476514287\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[4].value = \'grozergeorge80@gmail.com\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[5].click()')
    print('Waiting for code...')
    v_code = input()
    start_second = time.time()
    driver.execute_script('document.getElementsByTagName(\'input\')[6].value = ' + str(v_code))
    driver.execute_script('document.getElementsByTagName(\'input\')[9].click()')
    time.sleep(2)
    print('Agree page opened Time: ' + str(time.time() - start_second))
    start_second = time.time()
    driver.execute_script('document.getElementsByTagName(\'button\')[0].click()')
    time.sleep(1)
    print('End page opened Time: ' + str(time.time() - start_second))
    start_second = time.time()
    end_data = driver.page_source
    print(end_data[end_data.find('var blocked_dates'):end_data.find('var offDates_dates')])
    print('That`s all  Time: ' + str(time.time() - start_time))
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()