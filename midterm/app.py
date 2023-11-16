from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Route to form used to add a new student to the database
@app.route("/enternew")
def enternew():
    return render_template("student.html")

# Route to add a new record (INSERT) student data to the database
@app.route("/addrec", methods=['POST', 'GET'])
def addrec():
    con = None
    msg = None  # Initialize msg variable

    if request.method == 'POST':
        try:
            First_name = request.form['First_name']
            Last_name = request.form['Last_name']
            Gender = request.form['Gender']
            Email = request.form['Email']
            Age = request.form['Age']

            con = sqlite3.connect('data.db')
            cur = con.cursor()
            cur.execute("INSERT INTO Student (First_name, Last_name, Gender, Email, Age) VALUES (?,?,?,?,?)",
                        (First_name, Last_name, Gender, Email, Age))

            con.commit()
            msg = "Record successfully added to the database"
        except sqlite3.Error as e:
            con.rollback()
            msg = f"Error in the INSERT: {e}"
        except werkzeug.exceptions.BadRequestKeyError as e:
            msg = f"Bad Request: Missing key in form data - {e}"
        finally:
            if con:
                con.close()
            return render_template('result.html', msg=msg)



# Route to SELECT all data from the database and display in a table      
@app.route('/list')
def list():
    # Connect to the SQLite3 datatabase and 
    # SELECT rowid and all Rows from the students table.
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM Student")

    rows = cur.fetchall()
    con.close()
    # Send the results of the SELECT to the list.html page
    return render_template("list.html",rows=rows)

# Route that will SELECT a specific row in the database then load an Edit form 
@app.route("/edit", methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            id = request.form['id']
            # Connect to the database and SELECT a specific rowid
            con = sqlite3.connect("data.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT rowid, * FROM Student WHERE rowid = " + id)

            rows = cur.fetchall()
        except:
            id=None
        finally:
            con.close()
            # Send the specific record of data to edit.html
            return render_template("edit.html",rows=rows)

# Route used to execute the UPDATE statement on a specific record in the database
@app.route("/editrec", methods=['POST','GET'])
def editrec():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['rowid']
            First_name = request.form['First_name']
            Last_name = request.form['Last_name']
            Gender = request.form['Gender']
            Email = request.form['Email']
            Age = request.form['Age']

            # UPDATE a specific record in the database based on the rowid
            with sqlite3.connect('data.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE Student SET First_name='"+First_name+"', Last_name='"+Last_name+"', Gender='"+Gender+"', Email='"+Email+", Age='"+Age+"' WHERE rowid="+rowid)
                con.commit()
                msg = "Record successfully edited in the database"
        except:
            con.rollback()
            msg = "Error in the Edit: UPDATE Student SET nFirst_name='"+First_name+"', Last_name='"+Last_name+"', Gender='"+Gender+"', Email='"+Email+", Age='"+Age+" WHERE rowid="+rowid

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('result.html',msg=msg)

# Route used to DELETE a specific record in the database    
@app.route("/delete", methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        try:
             # Use the hidden input value of id from the form to get the rowid
            rowid = request.form['id']
            # Connect to the database and DELETE a specific record based on rowid
            with sqlite3.connect('data.db') as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM Student WHERE rowid="+rowid)

                    con.commit()
                    msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('result.html',msg=msg)
        
# Route to retrieve students with Last_name containing "ra"
@app.route('/students_with_last_name_ra')
def students_with_last_name_ra():
    con = sqlite3.connect("data.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM Student WHERE Last_name LIKE '%ra%'")

    rows = cur.fetchall()
    con.close()

    return render_template("students_with_last_name_ra.html", rows=rows)
