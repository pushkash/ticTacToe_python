import sys

#possible options of win-rows
#1-2-3
#4-5-6
#7-8-9

#1-4-7
#2-5-8
#3-6-9

#1-5-9
#3-5-7


board = {'1': 1, '2': 2, '3': 3,
	     '4': 4, '5': 5, '6': 6,
	 	 '7': 7, '8': 8, '9': 9 } 

sign = ''

count = 0

def boardDraw(board):
	print '-' * 9
	print str(board['1']) + ' | ' + str(board['2']) + ' | ' + str(board['3'])
	print '-' * 9
	print str(board['4']) + ' | ' + str(board['5']) + ' | ' + str(board['6'])
	print '-' * 9
	print str(board['7']) + ' | ' + str(board['8']) + ' | ' + str(board['9'])
	print '-' * 9
	print '\n' 

def chooseSide():
	while True:
		sign = str(raw_input('Choose your sign (X or 0, blank to quit): '))
		sign = sign.upper()
		print sign
		if sign == '':
			print 'Blank is exit'
			sys.exit()
		elif sign == 'X' or sign == '0':
			print 'Let it be'
			break		
		else:
			print 'Choose X or 0 (this is zero, yo,common)'
			continue
	
	return sign

def fillSquare(sign, board):
	while True:
		square = int(raw_input('Choose a square number to put a ' + sign + " : "))
		if square not in board.values():
			print 'Choose a square, please'
			continue
		else:
			square = str(square)
			board[square] = sign
			break
	return board


def checkFullRow(board):

	if board['1'] == board['2'] and board['2'] == board['3']:
		print board['1'] == board['2'] == board['3']
		print 'Sign ' + board['1'] + ' won'
		sys.exit()
	elif board['4'] == board['5'] and board['5'] == board['6']:
		print 'Sign ' + board['1'] + ' won'
		sys.exit()
	elif board['7'] == board['8'] and board['8'] == board['9']:
		print 'Sign ' + board['1'] + ' won'
		sys.exit()
	elif board['1'] == board['4'] and board['4'] == board['7']:
		print 'Sign ' + board['1'] + ' won'
		sys.exit()
	elif board['2'] == board['5'] and board['5'] == board['8']:
		print 'Sign ' + board['1'] + ' won'
		sys.exit()
	elif board['3'] == board['6'] and board['6'] == board['9']:
		print 'Sign ' + board['1'] + ' won'
		sys.exit()
	elif board['1'] == board['5'] and board['5'] == board['9']:
		print 'Sign ' + board['1'] + ' won'
		sys.exit()
	elif board['3'] == board['5'] and board['5'] == board['7']:
		print 'Sign ' + board['1'] + ' won'
		sys.exit()


sign = chooseSide()

boardDraw(board)

while True:

	checkFullRow(board)

	if count == 9:
		print "Game is over"
		break


	fillSquare(sign, board)

	boardDraw(board)

	count += 1








