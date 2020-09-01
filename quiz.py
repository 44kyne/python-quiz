# 問題文を作成
questions = [
				{"question":"正しいのはどっち？","answer":"A"},
				{"question":"サザエさんの結婚前の職業は？","answer":"A"},
				{"question":"日本にある駅名は？","answer":"B"},
			]

# 選択肢を作成
selections = [
				{"A":"コアラはユーカリしか食べない。","B":"パンダは笹の葉しか食べない。"},
				{"A":"出版社の記者","B":"バスガイド"},
				{"A":"黄","B":"緑"}
			]

# 問題文と選択肢の表示
for index in range(len(questions)):

	#問題文の取得
	question = questions[index]['question']

	# 選択肢AとBを取得
	selectionA = selections[index]['A']
	selectionB = selections[index]['B']

	print("Q{0} {1}".format((index + 1),question))
	print("A:{0} {1}".format(selectionA,selectionB))

	# ユーザーの値を受け取る
	userInput = input("回答を入力：")

	print("入力された値は {0} です".format(userInput))

	# 答えを確認
	if userInput.upper() == questions[index]['answer']:
		print("正解です")
	else:
		print("不正解です")
		