def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if (yourLeft + yourRight) == (friendsLeft + friendsRight):
        if max(yourLeft, yourRight) == max(friendsLeft, friendsRight):
            return True
            
    return False
