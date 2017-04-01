import sys
board = {'1': '1', '2': '2', '3': '3',
	 '4': '4', '5': '5', '6': '6',
	 '7': '7', '8': '8', '9': '9' }

sign = ''

count = 0

def boardDraw(board):
	print '-' * 9
	print board['1'] + ' | ' + board['2'] + ' | ' + board['3']
	print '-' * 9
	print board['4'] + ' | ' + board['5'] + ' | ' + board['6']
	print '-' * 9
	print board['7'] + ' | ' + board['8'] + ' | ' + board['9']
	print '-' * 9
	print '\n' 

def chooseSide():
	while True:
		sign = str(raw_input('Choose your sign (X or 0): '))
		sign = sign.upper()
		print sign
		if sign == '':
			print 'Blank is exit, bye'
			sys.exit()
		elif sign == 'X' or sign == 'x' or sign == '0':
			print 'Let it be'
			break		
		else:
			print 'Choose X or 0 (this is zero, yo,common)'
			continue
	
	return sign

def fillSquare(sign, board):
	while True:
		square = raw_input('Choose a square number to put a ' + sign + " : ")
		if square not in board.values():
			print 'Choose a square, please'
			continue
		else:
			board[square] = sign
			break
	return board



sign = chooseSide()

boardDraw(board)

while True:

	if count == 9:
		print "Game is over"
		break

	fillSquare(sign, board)

	boardDraw(board)

	count += 1










