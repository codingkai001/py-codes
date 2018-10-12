import collections

# 创建只有两个属性的纸牌类，用于构建纸牌类对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """一摞纸牌类"""
    # 类属性：13种点数和4种花色
    ranks = [str(i) for i in range(2, 11)] + list('AJQK')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return False

    def __getitem__(self, index):
        return self._cards[index]

    def __repr__(self):
        return 'FrenchDeck object contain ranks%r suits%r' % (self.ranks, self.suits)


if __name__ == '__main__':
    print(123)
