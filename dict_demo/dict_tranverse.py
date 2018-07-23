user_0 = {'username':'efermi',
          'first':'enrico',
          'last':'fermi'}
for key,value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)


favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'}
for name,language in favorite_languages.items():
    print(name.title() + ' favorite language is ' + language.title() + '.')


favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
            print('Hi ' + name.title() + ' , I see your favorite language is '
                                        + favorite_languages[name].title() + '!')

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'}
if 'erin' not in favorite_languages.keys():
    print('Erin,please take our poll!')

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for  taking the poll.')

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python'}
print('The following languages have been mentioned: ')
for language in favorite_languages.values():
    print(language.title())


for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for  taking the poll.')

favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'python',
                      'sarah':'java'}
print('The following languages have been mentioned: ')
for language in set(favorite_languages.values()):
    print(language.title())

aliens_0 = {'color': 'green','points': 5}
aliens_1 = {'color': 'yellow','points': 10}
aliens_2 = {'color': 'red','points': 15}
aliens = [aliens_0,aliens_1,aliens_2]
for alien in aliens:
    print(alien)


aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('...')
print('Total number of aliens: ' + str(len(aliens)))



aliens = []
for alien_number in range(0,30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['color'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)
print('...')

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'] }
print('You ordered a ' + pizza['crust'] +
      '-crust pizza' + ' with the following toppings: ')
for topping in pizza['toppings']:
    print('\t' + topping)


favorite_languages = {'jen':['python','ruby'],
                      'sarah':['c'],
                      'edward':['ruby','go'],
                      'phil':['python','haskell']}
for name, languages in favorite_languages.items():
    print('\n' + name.title() + ' favorite languages are:')
    for language in languages:
        print('\t' + language.title())


favorite_languages = {'jen':['python','ruby'],
                      'sarah':['c'],
                      'edward':['ruby','go'],
                      'phil':['python','haskell']}
for name, languages in favorite_languages.items():
    print('\n' + name.title() + ' favorite languages are:')
    for language in languages:
        print('\t' + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location':'princeton'},
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location':'paris'},
        }
for username,user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())

