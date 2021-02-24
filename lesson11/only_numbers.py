old_list = ['Damascus, SyriaDamascus, Syria', '5000', 'Athens, Greece', '7000',
            'Sidon, Lebanon', '6000', 'Rayy, Iran', '8000', 'Jerusalem, Israel',
            '4800', 'Faiyum, Egypt', '6000', 'Byblos, Lebanon', '7000',
            'Jericho, Palestinian Territories', '13000', 'Plovdiv, Bulgaria',
            '6000', 'Gaziantep, Turkey', '5650']

new_list = list(map(int, filter(lambda x: x.isdigit(), old_list)))

print(new_list)
