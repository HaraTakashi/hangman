import random

# def hangman(word):
def hangman():
    lists = ["python", "java", "c++", "drinking"]
    lists_ind = random.randint(0, len(lists)) - 1
    word = lists[lists_ind]
    print(len(lists))
    wrong = 0
    stages = [
        "",
        "11111111111111",
        "22222222222222",
        "33333333333333",
        "44444444444444",
        "55555555555555",
        "66666666666666",
        "77777777777777",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    corrected_char = "$"
    print("ハングマンへようこそ!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters and char != corrected_char:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = corrected_char
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0 : wrong + 1]))
        print("You lose! correct {}.".format(word))


# lists = ["cat", "dog", "bird", "frog"]
# hangman(random.choice(lists))
hangman()
