from flask import Flask , render_template , request , url_for , redirect , flash
import os
import random
import socket
import sys
import redis

redis_server = os.environ['REDIS']
app = Flask(__name__,static_url_path="/static")
app.secret_key= "secret key"



try:
    if "REDIS_PWD" in os.environ:
        r = redis.StrictRedis(host=redis_server,
                        port=6379,
                        password=os.environ['REDIS_PWD'])
    else:
        r = redis.Redis(redis_server)
    r.ping()#########PING ATMADAN OLMUYOR#### ILK HANDSHAKE BURADAN YAPILIYOR ILK BRIDGE BURADA KURULUYOR !######
except redis.ConnectionError:
    exit('Failed to connect to Redis, terminating.')


button1="Turkcell"
button2="TurkTelekom"
button3="Vodafone"
hit1="hit1"
hit = 0
oy = 0
oy1="oy1"
passwrd = None
respass = None
passwerd = None
r.set(passwrd,None)


if not r.get(button1): r.set(button1,0)

if not r.get(button2): r.set(button2,0)

if not r.get(button3): r.set(button3,0)

if not r.get(hit1): r.set(hit1,0)

if not r.get(oy1): r.set(oy1,0)



@app.route("/", methods = ["GET","POST"])  # yani kök dizinde ise index() fonksiyonunu çalıştır
def index():
    global hit
    global hit1
    global oy
    global oy1
    global passwrd
    r.incr(hit1,1)
    passwrd = str(r.get(passwerd).decode('utf-8'))
    if passwrd == "None":
        return redirect(url_for('register'))
    else:
        if request.method == 'GET':
            # Get current values
            hit = r.get(hit1).decode('utf-8')
            vote1 = r.get(button1).decode('utf-8')

            vote2 = r.get(button2).decode('utf-8')

            vote3 = r.get(button3).decode('utf-8')
            oy=r.get(oy1).decode('utf-8')
            
            return render_template("index.html",button1="Turkcell",button2="TurkTelekom",button3="Vodafone",value1=int(vote1),value2=int(vote2),value3=int(vote3),hit=int(hit),oy=int(oy)) #vote.html 'yi açar


        elif request.method == 'POST':
            if request.form['vote'] == 'reset':
                respass = request.form.get("ppasswrd")
                passwrd = r.get(passwerd).decode('utf-8')
                if respass == passwrd :
                    r.set(button1,0)

                    r.set(button2,0)

                    r.set(button3,0)

                    r.set(oy1,0)
                    
                    return redirect(url_for('index'))
                else :
                    flash("Wrong Password")
                    return redirect(url_for('index'))
                # Empty table and return results

                vote1 = r.get(button1).decode('utf-8')

                vote2 = r.get(button2).decode('utf-8')

                vote3 = r.get(button3).decode('utf-8')
                hit = r.get(hit1).decode('utf-8')

                oy=r.get(oy1).decode('utf-8')
                return render_template("index.html", value1=int(vote1), value2=int(vote2), value3=int(vote3), button1=button1, button2=button2, button3=button3,hit=int(hit),oy=int(oy), title="title")

            else:
                # Insert vote result into DB
                vote = request.form['vote']
                r.incr(vote,1)
                r.incr(oy1,1)
                oy=r.get(oy1).decode('utf-8')
                # Get current values
                vote1 = r.get(button1).decode('utf-8')

                vote2 = r.get(button2).decode('utf-8')

                vote3 = r.get(button3).decode('utf-8')

                # Return results
                hit = r.get(hit1).decode('utf-8')
                return render_template("index.html", value1=int(vote1), value2=int(vote2), value3=int(vote3), button1=button1, button2=button2, button3=button3,hit=int(hit),oy=int(oy), title="title")
    
        

 ##########################<<<<<MOBILE>>>>>>############################
@app.route("/mobile", methods = ["GET","POST"])  # yani kök dizinde ise index() fonksiyonunu çalıştır
def mobile():
    global hit
    global hit1
    global oy
    global oy1
    global passwrd
    r.incr(hit1,1)
    passwrd = str(r.get(passwerd).decode('utf-8'))
    if passwrd == "None":
        return redirect(url_for('register'))
    else:
        if request.method == 'GET':
            # Get current values
            hit = r.get(hit1).decode('utf-8')
            vote1 = r.get(button1).decode('utf-8')

            vote2 = r.get(button2).decode('utf-8')

            vote3 = r.get(button3).decode('utf-8')
            oy=r.get(oy1).decode('utf-8')
            
            return render_template("mobile.html",button1="Turkcell",button2="TurkTelekom",button3="Vodafone",value1=int(vote1),value2=int(vote2),value3=int(vote3),hit=int(hit),oy=int(oy)) #vote.html 'yi açar


        elif request.method == 'POST':
            if request.form['vote'] == 'reset':
                respass = request.form.get("ppasswrd")
                passwrd = r.get(passwerd).decode('utf-8')
                if respass == passwrd :
                    r.set(button1,0)

                    r.set(button2,0)

                    r.set(button3,0)

                    r.set(oy1,0)
                    
                    return redirect(url_for('mobil'))
                else :
                    flash("Wrong Password")
                    return redirect(url_for('mobile'))
                # Empty table and return results

                vote1 = r.get(button1).decode('utf-8')

                vote2 = r.get(button2).decode('utf-8')

                vote3 = r.get(button3).decode('utf-8')
                hit = r.get(hit1).decode('utf-8')

                oy=r.get(oy1).decode('utf-8')
                return render_template("mobile.html", value1=int(vote1), value2=int(vote2), value3=int(vote3), button1=button1, button2=button2, button3=button3,hit=int(hit),oy=int(oy), title="title")

            else:
                # Insert vote result into DB
                vote = request.form['vote']
                r.incr(vote,1)
                r.incr(oy1,1)
                oy=r.get(oy1).decode('utf-8')
                # Get current values
                vote1 = r.get(button1).decode('utf-8')

                vote2 = r.get(button2).decode('utf-8')

                vote3 = r.get(button3).decode('utf-8')

                # Return results
                hit = r.get(hit1).decode('utf-8')
                return render_template("mobile.html", value1=int(vote1), value2=int(vote2), value3=int(vote3), button1=button1, button2=button2, button3=button3,hit=int(hit),oy=int(oy), title="title")

 #######################<<<<<///MOBILE>>>>>###################3






@app.route("/register", methods =["GET","POST"])
def register():

    global passwrd
    passwrd = str(r.get(passwerd).decode('utf-8'))
    print(passwrd)
    if passwrd == "None" :
        if request.method == 'GET' :
            return render_template("firstrun.html")
        elif request.method == 'POST' :
            passwrd = request.form.get("ppasswrd")
            r.set(passwerd,passwrd)
            return redirect(url_for('index'))
    else :
        return redirect(url_for('index'))


@app.errorhandler(404)
def notfound(e):
    return render_template('404.html'), 404



if __name__ == "__main__": #main'de çalıştırılıyorsa
    app.run() #debug modunda programı çalıştırır (python app.py nin çalışmasını ve çalışır kalmasını sağlar)
