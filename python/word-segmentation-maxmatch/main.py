VALID_WORDS = {'any', 'yet', 'short', 'life', 'eat', 'everyone', 'older', 'wednesday', 'leave', 'sandwiches', 'hear', 'people', 'environment', '1111',
        'friday', 'too', 'a', 'love', 'meal', 'once', 'drive', 'toasted', 'just', 'returned', 'sight', 'shop', 'fact', 'with', 'detailed', 'green', '1',
        'stranger', 'midsent', 'in', 'roof', 'likes', 'quite', 'get', 'off', 'clock', 'sure', 'lot', 'slammed', 'each', 'pastels', 'bold', 'above',
        'however', 'windows', 'anyway', 'we', 'werent', 'where', 'later', 'pets', 'sounds', 'start', 'hasnt', 'couldnt', 'or', 'away', 'longer', 'they',
        'gods', 'music', 'authority', 'lazy', 'lovely', 'babies', 'recently', 'to', 'told', 'bunny', 'small', 'cats', 'something', 'borrowed', 'has', 'on',
        'wow', 'vividly', 'folded', 'up', 'mary', 'he', 'bread', 'same', 'please', 'great', 'spend', 'isnt', 'an', 'river', 'person', 'did', 'conditions',
        'chocolate', 'shake', 'camel', 'that', 'works', 'caramel', 'went', 'read', 'ever', 'many', 'years', 'donation', 'freezer', 'worm', 'room', 'lease',
        'true', 'need', 'nickname', 'thoughts', 'everything', 'go', 'enough', 'time', 'different', 'over', 'middle', 'asking', 'year', 'legless', 'join',
        'saying', 'you', 'night', 'movie', 'his', 'mysterious', 'japanese', 'sunburnt', 'math', 'piece', 'bird', 'cheat', 'ruin', 'research', 'last',
        'june', 'does', 'combined', 'want', 'open', 'brown', 'cheese', 'arrived', 'writing', 'back', 'when', 'house', 'hump', 'dont', 'fine', 'waves',
        'share', 'by', 'impassable', 'fish', 'velocity', 'book', 'still', 'not', 'currently', 'tom', 'piano', 'doll', 'promotion', 'lets', 'someone',
        'proud', 'favorite', 'milk', 'mum', 'me', 'cookies', 'youre', 'nancy', 'spotted', 'africa', 'ice', 'alone', 'combining', 'white', 'adventure',
        'luck', 'for', 'stole', 'how', 'more', 'free', 'apple', 'fence', 'why', 'early', 'sugar', 'am', 'plan', 'lizard', 'had', 'sentence', 'stars',
        'getting', 'sixtyfour', 'attendance', 'seats', 'sick', 'memory', 'sentences', 'step', 'letter', 'than', 'asia', 'appreciated', 'here', 'of',
        'used', 'least', 'old', 'within', 'like', 'hands', 'coming', 'it', 'shooter', 'paints', 'first', 'little', 'diary', 'perhaps', 'my', 'now', 'suit',
        'out', 'italy', 'voice', 'wrote', 'cool', 'abstraction', 'yeah', 'taste', 'consumption', 'do', 'onesie', 'way', 'rain', 'plays', 'test', 'busy',
        'random', 'sundays', 'is', 'help', 'other', 'information', 'saw', 'there', 'from', 'fox', 'two', 'amount', 'completely', 'buttered', 'one', 'should',
        'metaphysics', 'unique', 'real', 'ended', 'try', 'tomato', 'blog', 'easter', 'know', 'dog', 'ran', 'baggage', 'alive', 'day', 'rock', 'tries', 'counting',
        'were', 'dark', 'our', 'gem', 'today', 'story', 'after', 'records', 'at', 'no', 'good', 'always', 'persons', 'decorated', 'wait', 'again', 'come', 'nor',
        'wasnt', 'bad', 'party', 'thing', 'tooth', 'tomorrow', 'dentist', 'didnt', 'anyone', 'until', 'red', 'pig', '4', 'hes', 'popcorn', 'stay', 'compensates',
        'next', 'cows', 'dessert', 'approaches', 'its', 'clean', 'going', 'visited', 'mind', 'clear', 'checked', 'so', 'id', 'will', 'advised', 'car', 'loss', 'what',
        'meet', 'handkerchief', 'can', 'may', 'broken', 'best', 'teeth', 'sauce', 'throughout', 'let', 'was', 'buy', 'find', 'but', 'donkey', 'only', 'us', 'oh',
        'this', 'rent', 'loud', 'human', 'ago', 'weeks', 'together', 'poker', 'jumps', 'song', 'better', 'gotten', 'noisy', 'flew', 'about', 'reason', 'are', 'maple',
        'never', 'her', 'clocks', 'vacant', 'cream', 'fairy', 'turned', 'sky', 'officiates', 'happy', 'hurry', 'young', 'remember', 'paper', 'neatly', 'long', 'subsequently',
        'pie', 'discovered', 'striped', 'hand', 'ill', 'right', 'places', 'joe', 'been', 'recommend', 'high', 'list', 'got', 'says', 'as', 'think', 'playing', 'i',
        'harder', 'frame', 'him', 'front', 'check', 'jobs', 'see', 'colors', 'them', 'either', 'coherent', 'work', 'really', 'money', 'she', 'would', 'initially',
        'floor', 'christmas', 'outside', 'things', 'rather', 'stop', 'crashing', 'ass', 'otherwise', 'eaters', 'school', 'shore', 'sometimes', 'the', 'comes', 'laugh',
        'pretty', 'twinkling', 'country', '1234', 'yesterday', 'hour', 'often', 'made', 'and', 'passed', 'take', 'have', 'glass', 'kite', 'yourself', 'place', 'goodbye',
        'malls', 'three', 'ends', 'realise', 'else', 'if', 'thought', 'all', 'laptop', 'roads', 'under', 'syrup', 'shut', 'body', 'exciting', 'very', 'quick',
        'make', 'purple', 'learning', 'asked', 'revels', 'thinking', 'store', 'your', 'blue', 'door', 'english', 'be', 'eating', 'having', 'lake', 'said', 'glittering',
        'speaks', 'greatly', 'home', 'walk', 'table', 'calories', 'class', 'town', 'susan', 'tuna', 'wont'}

# def max_match(sentence): 
    # words = [] 
    # while sentence != '':
        # before = sentence
        # for i in range(len(sentence), 0, -1):
            # if sentence[0:i] in VALID_WORDS:
                # words.append(sentence[0:i])
                # sentence = sentence[i:]
                # break
        # if sentence == '' or before != sentence:
            # continue
        # words.append(sentence[0])
        # sentence = sentence[1:]

    # return words

max_match=__import__('re').compile('|'.join(sorted(VALID_WORDS,key=len)[::-1])+'|.').findall

assert max_match('goodluck') == ['good','luck']
assert max_match('ewingsa') == ['e','w','in','g','s','a']
