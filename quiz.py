# 問題文を作成
questions = [
				{"question":"正しいのはどっち？","answer":"A"},
				{"question":"サザエさんの結婚前の職業は？","answer":"A"},
				{"question":"日本にある駅名は？","answer":"B"},
			]

# 選択支を作成
selections = [
				{"A":"コアラはユーカリしか食べない。","B":"パンダは笹の葉しか食べない。"},
				{"A":"出版社の記者","B":"バスガイド"},
				{"A":"黄","B":"緑"}
			]

"""
for question in questions:
	print(question["question"])
	print(question["answer"])
"""

for selection in selections:
	print(selection['A'])
	print(selection['B'])
