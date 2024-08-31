favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
    }
#for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is "+language.title()+".")
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" hi "+name.title() + ", i see your favourite programming language is "+favorite_languages[name].title()+"!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take the poll\n")

for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.\n")

print("the followign languages have been mentioned: ")
for languages in favorite_languages.values():
    print(languages.title())
