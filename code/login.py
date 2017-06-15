"""
sleep_extra allows multiprocesses not conflit on login in different
browsers (avoid logging in at the same time)
"""
def login_facebook(driver, email, passwd, sleep_extra):
    driver.get(CONST.FACEBOOK_LOGIN_URL)
    time.sleep(CONST.BEFORE_LOGIN_SLEEP_TIME + sleep_extra)
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('pass').send_keys(passwd)
    driver.find_element_by_id('loginbutton').click()