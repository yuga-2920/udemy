with open('restaurant_list.csv') as f:

    print('あなたの名前は何ですか')
    name = input()

    for restaurant_name in f.read():
        print(f'おすすめのレストランは{restaurant_name}です。すきですか')
        blood = input()

    print(f'{name}さん。どこのレストランが好きですか')
    restaurant = input()

    


    print(f'{name}さん。ありがとうございました。')