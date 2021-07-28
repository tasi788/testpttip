import os
from PyPtt import PTT

ptt_bot = PTT.API()

ptt_bot.login(
    os.getenv('acc'),
    os.getenv('passwd'),
    kick_other_login=True)

board = os.getenv('board')

test_board_list = board.split(',')

for test_board in test_board_list:
    index = ptt_bot.get_newest_index(
        PTT.data_type.index_type.BBS,
        board=test_board
    )
    print(f'{test_board} 最新文章編號 {index}')
