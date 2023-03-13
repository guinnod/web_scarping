import undetected_chromedriver
import time


options = undetected_chromedriver.ChromeOptions()
options.add_argument('--headless')
driver = undetected_chromedriver.Chrome(options)


link = 'https://kz.blsspainvisa.com/russian/book_appointment.php'
page_flags = ['Проверочный код:', 'Я даю согласие', 'Введите символы с картинки:']


def execute_all(scripts):
    for script in scripts:
        driver.execute_script(script)


def log_executing_time(message, time_var):
    print(message, str(time.time() - time_var))
    return time.time()


def exit_scarp():
    driver.close()
    driver.quit()


def scarp_bls(city_code, vise_type, email):
    try:

        block_first = ['document.getElementsByTagName(\'input\')[0].click()',
                       'document.getElementsByTagName(\'select\')[1].value = \'' + str(city_code) + '\'',
                       'getAppService(\'' + str(city_code) + '\')']
        block_second = ['document.getElementsByTagName(\'select\')[2].value = \'' + vise_type + '\'',
                        'document.getElementsByTagName(\'input\')[2].value = \'+7\'',
                        'document.getElementsByTagName(\'input\')[3].value = \'7476514287\'',
                        'document.getElementsByTagName(\'input\')[4].value = \'' + str(email) + '\'',
                        'document.getElementsByTagName(\'input\')[5].click()']

        temp_time = time.time()

        print('Executed!')
        driver.get(link)
        temp_time = log_executing_time('We have got page! Time:', temp_time)

        while driver.page_source.find(page_flags[0]) == -1:
            pass
        temp_time = log_executing_time('Verify code page opened! Time:', temp_time)

        execute_all(block_first)
        time.sleep(0.5)
        log_executing_time('Function has done! Time:', temp_time)

        execute_all(block_second)
        print('Waiting for code...')
        return True
    except Exception as e:
        print(e)
        exit_scarp()
        return False


def scarp_bls_verified():
    try:
        v_code = input()
        temp_time = time.time()
        block_third = ['document.getElementsByTagName(\'input\')[6].value = ' + str(v_code),
                       'document.getElementsByTagName(\'input\')[9].click()']
        execute_all(block_third)
        while driver.page_source.find(page_flags[1]) == -1:
            pass
        temp_time = log_executing_time('Agree page opened Time:', temp_time)

        driver.execute_script('document.getElementsByTagName(\'button\')[0].click()')
        while driver.page_source.find(page_flags[2]) == -1:
            pass
        log_executing_time('End page opened Time:', temp_time)

        end_data = driver.page_source
        print(end_data[end_data.find('var blocked_dates'):end_data.find('var offDates_dates')])
    except Exception as e:
        print(e)
    finally:
        exit_scarp()