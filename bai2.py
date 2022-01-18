import itertools

cards = [     #Bo bai 52 la + them 4 la A (xi) co gia tri la 11
    1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    5, 5, 5, 5,
    6, 6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9, 9,
    10, 10, 10, 10,
    10, 10, 10, 10,
    10, 10, 10, 10,
    10, 10, 10, 10,
    11, 11, 11, 11,
]


def find_combination(cards, sum_target):
    total_case = 0 # Tong so truong hop trong 1 lan dem
    dict = {} # Tu dien ghi lai ruong hop boc bai, so lan xay ra truong hop do
    for combine in itertools.combinations(cards, 3):  #combinations lua chon 3 la bai trong bo bai cards
        if sum(combine) == sum_target:   #Neu tong gia tri cac la bai bang voi tagert thi them vao bo nho
            if combine not in dict.keys():
                dict[combine] = 1
            else:
                dict[combine] += 1
            total_case += 1
    return dict, total_case


targets = [17, 18, 19, 20, 21]
for target in targets:
    dict, total_case = find_combination(cards, target)
    print('------------------')
    print('Target = {}'.format(target))
    print('Nums cases: {}'.format(total_case))
    for key in dict.keys():
        print('{} : {}'.format(key, dict[key]))
