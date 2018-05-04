#/usr/bin/python2.7

import sys
import random

board = {'1': 1, '2': 2, '3': 3,
	     '4': 4, '5': 5, '6': 6,
	 	 '7': 7, '8': 8, '9': 9 }

def boardDraw(board):
	print('-' * 9)
	print(str(board['1']) + ' | ' + str(board['2']) + ' | ' + str(board['3']))
	print('-' * 9)
	print(str(board['4']) + ' | ' + str(board['5']) + ' | ' + str(board['6']))
	print('-' * 9)
	print(str(board['7']) + ' | ' + str(board['8']) + ' | ' + str(board['9']))
	print('-' * 9)
	print('\n')


def chooseSide():
	while True:
		sign = str(raw_input('Choose your sign (X or 0, blank to quit): '))
		sign = sign.upper()
		print("Your choise is " + sign)
		if sign == '':
			print('Blank is exit')
			sys.exit()
		elif sign == 'X' or sign == '0':
			print('Let it be')
			break
		else:
			print('Choose X or 0 (this is zero, yo, common)')
			continue
	return sign


def fillSquare(sign, board):
	while True:
		square = int(raw_input('Choose a square number to put a ' + sign + " : "))
		if square not in board.values():
			print('Choose a square, please')
			continue
		else:
			square = str(square)
			board[square] = sign
			break
	return board


def checkFullRow(board):
	# TODO: advance algorythm of checking win situation
	if board['1'] == board['2'] == board['3']:
		print('Sign ' + board['1'] + ' won')
		sys.exit()
	elif board['4'] == board['5'] == board['6']:
		print('Sign ' + board['4'] + ' won')
		sys.exit()
	elif board['7'] == board['8'] == board['9']:
		print('Sign ' + board['7'] + ' won')
		sys.exit()
	elif board['1'] == board['4'] == board['7']:
		print('Sign ' + board['1'] + ' won')
		sys.exit()
	elif board['2'] == board['5'] == board['8']:
		print('Sign ' + board['2'] + ' won')
		sys.exit()
	elif board['3'] == board['6'] == board['9']:
		print('Sign ' + board['3'] + ' won')
		sys.exit()
	elif board['1'] == board['5'] == board['9']:
		print('Sign ' + board['1'] + ' won')
		sys.exit()
	elif board['3'] == board['5'] == board['7']:
		print('Sign ' + board['3'] + ' won')
		sys.exit()

def oppositeSide(sign, board):
	if board['5'] != 'X' and board['5'] != '0':
		board['5'] = sign

	else:
		# TODO:Check 2 signs in a raw to avoid losing caused by random number

		while True:
			square = random.randint(1, 9)
			square = str(square)
			if board[square] != 'X' and board[square] != '0':
				board[square] = sign
				break
			else:
				continue
	return board


############################################
#Start game

sign = chooseSide()

if sign == 'X':
	enemySign = '0'
else:
	enemySign = 'X'

boardDraw(board)

count = 0

while True:
	checkFullRow(board)
	
	if count == 9:
		print("Game is over")
		break

	fillSquare(sign, board)

	boardDraw(board)

	oppositeSide(enemySign, board)

	boardDraw(board)

	count += 1
