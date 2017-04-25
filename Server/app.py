from bottle import Bottle , route, get, post, request, response , delete
app = Bottle()
#for send mails 
import smtplib
#for uploud files
import os

# ~~~~~~~~~~~~~~~~~~ A : I Wanted to use sqlalchemy but there is unknowen error ~~~~~~~~~~~~~~~~~ 
#from bottle.ext import sqlalchemy
#from sqlalchemy import create_engine, Column, Integer, Sequence, String , UniqueConstraint
#from sqlalchemy.ext.declarative import declarative_base  
# ~~~~~~~~~~~~~ B : I Wanted to use sqlalchemy but there is unknowen error ~~~~~~~~~~~~~~~ 
#import peewee
#from peewee import *

# SO .. Maybe I will just use normal Mysql connection and write the SQL my self 
import MySQLdb

 # ~~~~~~~~~~~~~~~~~~~ DB CONNECTION ~~~~~~~~~~~~~~~~~
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="d_task")

cur = db.cursor()

 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#  {{{{{------ DB  Operations interface  ------ }}}}}}  
def get_info_by_id(id):
    # will get user info from db
    return { 'name':'Mohamed' , 'email':'mhmeeaad@gmail.com' , 'pw':'somepw'}


def check_login(email, pw):
    #check if this user exists in the DB
        stmt = (
        "SELECT id FROM user WHERE email=%s AND pw=%s;"
        )
    cur.execute(stmt,(email,pw))
    row = cur.fetchone()
    if row is not None:
        return row[0]


def add_user(name,email,pw):
    #All validation shoud be implemented here
    cur.execute("SELECT email FROM user WHERE email='"+email+"';")
    row = cur.fetchone()
    if len(pw) > 8 and row is None :
        cur.execute("SELECT * FROM user")
        id = cur.rowcount+1   
        insert_stmt = (
        "INSERT INTO employees ( id, name, email, pw) "
        "VALUES (%s, %s, %s, %s)"
        )
        data = ( id , name , email , pw )
        
        cursor.execute(insert_stmt, data)
        return True
    else:
        return False


# requst for reseting a pw 
def reset_requst(email):
    stmt = (
        "SELECT id FROM user WHERE email=%s"
        )
    cur.execute(stmt,email)
    row = cur.fetchone()
    id=row[0]
    new_token = makeToken()
    stmt = (
        "INSERT INTO resets(id,token) VALUES (%s, %s)"
        )
    cur.execute(stmt,(id,token))
    return new_token
    

# the idea is that if some one know the token then change the pw and delete the token
def reset_pw( new_pw, token):
    stmt = ("SELECT id FROM resets WHERE token=%s")
    cur.execute(stmt , token)
    row = cur.fetchone()    
    if row is not None :
        id=row[0]
        stmt_u = ("UPDATE user SET pw =%s WHERE id =%s;")
        cur.execute(stmt_u ,(new_pw,id))
        stmt_d = ("DELETE FROM resets WHERE id =%s ;")
        cur.execute(stmt_d,id)
        return True
    else:
        return False

# {{{{{{{{{{{{{{-------------------------------}}}}}}}}}}}}}}






# >>>>>>>>>>>>>>>>>>> Simple Pages With Cookies  <<<<<<<<<<<<<<<<<<<<
@app.route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


#Using a cookie here !
@app.post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    id = check_login(username, password)
    if id is not None:
        response.set_cookie('user_id', str(id) , path='/')
        return '''
        <p>Your login information was correct.</p>
        <a href="/myinfo" >My Profile</a>
        '''
    else:
        return "<p>Login failed.</p>"


#Using a cookie here too !
@app.get('/myinfo')
def get_info():
    id = int( str(request.get_cookie('user_id')))
    user_info = get_info_by_id(id)
    #if there is info with this id get it from DB and return it
    if user_info is not None:
        # can be implemented with template() fun
        return 'Cookie Works .. <br> Your Name : ' + user_info['name']+ '<br>' +'Your Email : ' + user_info['email']






# >>>>>>>>>>>>>>>>>>>>>>> RESTFUL API <<<<<<<<<<<<<<<<<<<<<<<<<


@app.post('/api/login')
def do_login():
    username = request.json.get('email')
    password = request.json.get('pw')
    id = check_login(username, password)
    if id is not None:
        return {'id':id}
    else:
        return {'state':'err'}


#get all user data 
@app.get('/api/myinfo/<id>')
def get_info(id):
    user_info = get_info_by_id(id)
    #if there is info with this id get it from DB and return it
    if user_info is not None:
        return get_info_by_id(id)
    

@app.post('/api/signup')
def signup():
    
    if add_user(name= request.json.get('name') , email= request.json.get('email') , pw= request.json.get('pw') ):
        return {'state':'OK'}
    else:
        return {'state':'err'}


# the idea is if a user forget the pw we will send her a massge with secret token to reset the pw 
@app.get('/api/forget/<email>')
def forget_pw(email):
    token=reset_requst(email)
    sendMail('from',email,'reset your password','open this link to reset your password http://**/api/reset/'+token)
    return {'state':'OK'}


@app.post('/api/reset/<token>')
def reseting(token):
    new_pw = request.json.get('pw');
    reset_pw(new_pw,token)
    return {'state':'OK'}








# >>>>>>>>>>>>>>>>>>>>> GENERAL FUNCTIONS <<<<<<<<<<<<<<<<<<<<<<

#--------------------  Generate Tokens ---------------
def makeToken():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))



#--------------------  FOR SEND EMAILS ---------------
def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
    """this is some test documentation in the function"""
    message = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Send the mail
    server = smtplib.SMTP(SERVER)
    "New part"
    server.starttls()
    server.sendmail(FROM, TO, message)
    server.quit()

app.run(reloader=True, debug=True)






# ---------------------- FOR FILE UPLOAD --------------------
# sourse http://stackoverflow.com/questions/15050064/how-to-upload-and-save-a-file-using-bottle-framework
@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    save_path = "/tmp/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "File successfully saved to '{0}'.".format(save_path)





# ----------------------- A -----------------------

#URI = 'mysql://localhost/'
#Base = declarative_base()
#engine = create_engine(URI)
#plugin = sqlalchemy.Plugin(engine, keyword='db')
#app.install(plugin);



"""
class User (Base):
    __tablename_ ='user'
    id = Column( Integer , primary_key=True)
    name = Column(String(100))
    email= Column(String(100))
    pw = Column(String(100))
    __table_args__ = (
    UniqueConstraint("name", "parent_id",
                     name='unique_category_and_parent'),)
"""





# ------------------------- B -----------------------
#db = MySQLDatabase( 'd_task' , user='root',passwd='')

"""
class User(peewee.Model):
    id = peewee.IntegerField()
    name = peewee.TextField()
    email = peewee.TextField()
    pw = peewee.TextField()
    
    class Meta:
        database = db

User.create_table()

user = User(id= 2 ,name="Nasser", email="mhm@gmail.com" , pw="0509699701")

user.save()


for book in Book.filter(name="Nasser"):
    print book.email
"""
