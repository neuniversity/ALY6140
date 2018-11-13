"""
<Project Title>


Copyright (c) 2017
Licensed
Written by <>
"""



def function1(var1,var2,var2):
    """

    :param var1:
    :param var2:
    :return:
    """

    return

def function2(var1,var2,var3):
    """

    :param var1:
    :param var2:
    :param var3:
    :return:
    """

    return

if __name__ == "__main__":
    # Main functions to Run
#### The authentication of blackboard

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "https://northeastern.blackboard.com/webapps/login/"
password_mgr.add_password(None, top_level_url, 'jiang.can', 'Jiangcanlin123')

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
opener.open('https://northeastern.blackboard.com/webapps/blackboard/execute/content/file?cmd=view&content_id=_19572178_1&course_id=_2571461_1')
# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)