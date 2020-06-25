import Convert


def check_links(pivot, links, index=0):

    if Convert.convert(links[index]) < Convert.convert(pivot[index]):
        return True

    if links.lower() == pivot.lower():
        if ord(links[0]) > ord(pivot[0]):
            return False
        elif ord(links[0]) < ord(pivot[0]):
            return True

    try:
        if Convert.convert(links[index]) == Convert.convert(pivot[index]):
            return check_links(pivot, links, index + 1)

    except IndexError:
        if len(links) > len(pivot):
            return False

        else:
            return True

    return False







def check_rechts(pivot, rechts, index=0):

    if Convert.convert(rechts[index]) > Convert.convert(pivot[index]):
        return True

    if rechts.lower() == pivot.lower():
        if ord(rechts[0]) < ord(pivot[0]):
            return False
        elif ord(rechts[0]) > ord(pivot[0]):
            return True
        else:
            return False

    try:
        if Convert.convert(rechts[index]) == Convert.convert(pivot[index]):
            return check_rechts(pivot, rechts, index + 1)

    except IndexError:
        if len(rechts) < len(pivot):
            return False
        else:
            return True

    else:
        return False
