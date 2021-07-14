from flask import Flask, render_template, url_for, request, make_response, redirect
import sqlite3
app = Flask(__name__)

logined = False
userlogin = ['', '']
@app.route('/')
def index():
	global logined
	logined = False
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def reg():
	db = sqlite3.connect('users.db')
	sql = db.cursor()
	sql.execute('''CREATE TABLE IF NOT EXISTS users (
		login TEXT,
		password TEXT,
		counter BIGINT
	)''')
	db.commit()
	
	login = request.form['login']
	passwd = request.form['password']
	
	sql.execute('SELECT login FROM users')
	
	f = sql.fetchall()
	usd = False
	for i in range(len(f)):
		if login == str(f[i])[2:-3]:
			usd = True
			break
	
	if not usd:
		sql.execute('INSERT INTO users VALUES (?, ?, ?)', (login, passwd, 0))
		db.commit()
		return render_template('rgstrd.html')
	else:
		return render_template('not_rgstrd.html')


@app.route('/login', methods=['POST'])
def lg():
	db = sqlite3.connect('users.db')
	sql = db.cursor()
	sql.execute('''CREATE TABLE IF NOT EXISTS users (
		login TEXT,
		password TEXT,
		counter BIGINT
	)''')
	db.commit()
	
	login = request.form['login']
	passwd = request.form['password']
	
	sql.execute('SELECT * from users')
	f = sql.fetchall()
	
	for i in range(len(f)):
		login1 = f[i][0]
		passwd1 = f[i][1]
		if (login == login1) and (passwd == passwd1):
			global logined
			global userlogin
			userlogin[0] = login
			userlogin[1] = passwd
			logined = True
			return redirect(url_for('counter'))
	
	return redirect(url_for('index'))

@app.route('/counter')
def counter():
	global logined
	if logined:
		db = sqlite3.connect('users.db')
		sql = db.cursor()
		sql.execute('''CREATE TABLE IF NOT EXISTS users (
			login TEXT,
			password TEXT,
			counter BIGINT
		)''')
		db.commit()
		
		sql.execute('''SELECT * FROM users''')
		f = sql.fetchall()
		
		for i in range(len(f)):
			global userlogin
			lg = f[i][0]
			cnt = f[i][2]
			if (userlogin[0] == lg):
				break
		
		
		return render_template('cnt.html', cnt=str(cnt))
	else:
		return redirect(url_for('index'))

@app.route('/counterSave', methods=["GET"])
def counterSave():
	global logined
	global userlogin
	
	if logined:
		db = sqlite3.connect('users.db')
		sql = db.cursor()
		sql.execute('''CREATE TABLE IF NOT EXISTS users (
			login TEXT,
			password TEXT,
			counter BIGINT
		)''')
		db.commit()
		
		sql.execute("UPDATE users SET counter = (?) WHERE login = (?)", (int(request.args.get('cnt', '')), userlogin[0]))
		db.commit()
		return redirect(url_for('counter'))
	return redirect(url_for('index'))
		

if __name__ == '__main__':
	app.run(host='localhost', port=8080)
	print(url_for('static', filename='./Pages/styles.css'))
