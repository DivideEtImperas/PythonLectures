def delete_data(word):
    with open('/Workout/Information_system/base.csv', 'r',
              encoding="utf-8") as f:
        els = [f.readlines()]
        for i in els:
            if i.index == word:
               del els[word]  
            return print(els)

delete_data(word = input('=='))


