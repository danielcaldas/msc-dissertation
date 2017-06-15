"""
get friends list for a given user identified by the passed uid
"""
def get_friends(driver, uid):
    go_to_all_friends(driver, uid)
    total_friends = _get_totaln_of_friends(driver)
    _load_all_friends(driver, (total_friends/CONST.MAX_FRIENDS_DISPLAYED))

    friends = driver.find_elements_by_xpath("//div[@class='uiProfileBlockContent']")
    friends_list = []

    for friend in friends:
        tmp = friend.find_element_by_xpath(".//a[not(@class)]").get_attribute('href').split(CONST.FACEBOOK_BASE_URL)[1]
        if tmp:
            try:
                res = re.search("id=([0-9]+)?", tmp)
                friends_list.append(res.group(1))
            except:
                try:
                    res = tmp.split('?')[0]
                    friends_list.append(res)
                except:
                    pass

    return friends_list