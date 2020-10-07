import os
heroes = ['warrior','shaman','rogue','paladin','hunter','druid','warlock','mage','priest','neutral']
with open(os.getcwd()+'/../base/card.py','r',encoding='utf-8') as f:
    script = f.read()
for hero in heroes:
    for i in range(50):
        with open(os.getcwd()+'/../card/card_%s_%04d.py' %(hero,i),'w',encoding='utf-8') as f:
            f.write('from base.card import Card\n'+script.replace('class Card','class Card%s%04d(Card)' % (hero.capitalize(),i)))