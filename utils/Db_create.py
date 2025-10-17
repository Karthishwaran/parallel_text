import sqlite3
con = sqlite3.connect("./utils/tutorial.db", check_same_thread=False)
cur = conn.cursor()
#sentence_database
cur.execute("CREATE TABLE sentence(sentence TEXT, score INT, sentiment TEXT)")
#word_list_database
cur.execute("CREATE TABLE words(word TEXT, score INT, sentiment TEXT,is_available_in_dict BOOLEAN)")
#analysis_database
cur.execute("CREATE TABLE analysis(total_sentences NUM, total_paras NUM, total_words NUM,total_negative_words NUM,total_positive_words NUM,total_dict_hits NUM,total_dict_miss NUM,total_positive_sentences NUM,toptal_negative_sentances num)")

#cur.execute("INSERT INTO names VALUES(?,?)",("Tofu masala",330))
#cur.execute("INSERT INTO names VALUES(?,?)",("Mushroom",290))
conn.commit()
conn.close()