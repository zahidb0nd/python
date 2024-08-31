favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
    }

poll = ['jen','edward','sarah','phil','zahid','dwight','angela','micheal']

for polls in poll:
    if polls in favorite_languages:
        print(polls+" thank you for polling\n")
    else:
        print(polls+" please take the pole")
