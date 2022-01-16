def get_count(text):

    _head = text[0]
    head = _head
    
    counts = []
    count = 0

    for num in text:
        
        if num == head:
            count += 1
        
        else:
            counts.append(count)
            count = 1
            head = num

    else:
        counts.append(count)
    
    return _head, counts

def int2str(count):
    
    if count < 10:
        return '0' + str(count)
    
    else:
        return str(count)

def encode(text):
    head, counts = get_count(text)

    text_encode = head
    for count in counts:
        text_encode += int2str(count)
    
    return text_encode


def return_count(text):
    _encode = encode(text)
    head = _encode[0]
    _encode = _encode[1:]
    counts = []

    while _encode != '':
        counts.append(_encode[:2])
        _encode = _encode[2:]

    return head, counts

def str2int(count):

    count = int(count)

    return count

def decode(text):
    head, counts = return_count(text)
    new_text = ''

    for num, count in enumerate(counts):
        count = int(count)

        if num % 2 == 0:
            new_text += head * str2int(count)

        else:
            if int(head) == 0:
                new_text += '1' * count

            else:
                new_text += '0' * count

    return new_text

with open('\\Users\\karon\\OneDrive\\ドキュメント\\practice\\udemy\\【キカガク流】プログラミング力向上のためのPythonで学ぶアルゴリズム論（前編）\\input.txt','r') as f:
    text = f.read()

new_text = decode(text)

if new_text == text:
    print('True')
else:
    print('False')