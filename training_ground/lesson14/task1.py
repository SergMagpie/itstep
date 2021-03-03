fruits = ('Banana', 'Blackcurrant', 'Blueberry', 'Chili pepper', 'Cranberry', 'Eggplant', 'Gooseberry', 'Grape', 'Guava', 'Kiwifruit', 'Lucuma', 'Pomegranate', 'Redcurrant', 'Tomato',	'Cucumber', 'Gourd', 'Melon',
          'Pumpkin',	'Grapefruit', 'Lemon', 'Lime', 'Orange',	'Blackberry', 'Boysenberry', 'Raspberry',	'Fig', 'Hedge apple', 'Mulberry', 'Pineapple',	'Apple', 'Pineapple', 'Rose hip', 'Stone fruit', 'Strawberry',
          'Banana', 'Blackcurrant', 'Blueberry', 'Chili pepper', 'Cranberry', 'Eggplant', 'Gooseberry', 'Grape', 'Guava', 'Kiwifruit', 'Lucuma', 'Pomegranate', 'Redcurrant', 'Tomato',	'Cucumber', 'Gourd', 'Melon',)
fruit = input('Enter fruit name ')
count = 0
for i in fruits:
    if i.lower() == fruit.lower():
        count += 1
print(count)
