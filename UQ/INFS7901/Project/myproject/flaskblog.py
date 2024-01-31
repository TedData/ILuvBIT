### Example inspired by Tutorial at https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### However the actual example uses sqlalchemy which uses Object Relational Mapper, which are not covered in this course. I have instead used natural sQL queries for this demo. 

from flask import Flask, render_template, url_for, flash, redirect
from forms import AddForm, SelectForm, DeleteForm, ModifyForm, DeleteCascadeForm, BookForm, PasswordForm
import pymysql

conn = pymysql.connect(host='localhost',
                             user='s4663588',
                             password='123456',
                             database='s4663588_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/")
@app.route("/home")
def home():
    #Display all Stuff from the 'Stuff' table
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM Stuff")
    posts = c.fetchall()
    return render_template('home.html', posts=posts)

@app.route("/manage", methods=['GET', 'POST'])
def manage():
    return render_template('manage.html')

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        c = conn.cursor()
        #Add the new car into the 'Car' table
        query = "Insert into Car VALUES ('"+ form.V_ID.data +"', '"+ form.B_ID.data +"', '"+ form.Model.data +"','"+ form.Kilometers.data +"',"+ form.Price.data +","+ form.C_Year.data +",'"+ form.Accident.data +"','"+ form.Car_brand.data +"')" #Build the query
        c.execute(query) #Execute the query
        conn.commit() #Commit the changes
        flash(f'Created for {form.V_ID.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('add.html', title='add', form=form)

@app.route("/password", methods=['GET', 'POST'])
def password():
    form = PasswordForm()
    if form.validate_on_submit():
        if form.Password.data == '7901':
            return redirect(url_for('manage'))
        else:
            flash(f'Password mistake', 'success')
            return redirect(url_for('home'))
    return render_template('password.html', title='password', form=form)

@app.route("/modify", methods=['GET', 'POST'])
def modify():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT distinct(V_ID) FROM Car")
    results = c.fetchall()
    V_IDs = [(results.index(item), item['V_ID']) for item in results]
    form = ModifyForm()
    form.V_ID.choices = V_IDs
    if form.validate_on_submit():
        V_ID =  (form.V_ID.choices[form.V_ID.data][1])
        query_V_ID = 'where V_ID = "{}"'.format(V_ID)
        query = 'update Car set B_ID="{}", Model="{}", Kilometers ="{}",Price={},C_Year={},Accident="{}",Car_brand="{}" {}'.format(form.B_ID.data,form.Model.data,form.Kilometers.data,form.Price.data,form.C_Year.data,form.Accident.data,form.Car_brand.data, query_V_ID)
        c.execute(query) #Execute the query
        conn.commit() #Commit the changes
        flash(f'{V_ID} has been modified!', 'success')
        return redirect(url_for('home'))
    return render_template('modify.html', title='modify', form=form)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT distinct(V_ID) FROM Car")
    results = c.fetchall()
    V_IDs = [(results.index(item), item['V_ID']) for item in results]
    form = DeleteForm()
    form.V_ID.choices = V_IDs
    if form.validate_on_submit():
        V_ID =  (form.V_ID.choices[form.V_ID.data][1])
        query_V_ID = 'where V_ID = "{}"'.format(V_ID)
        query = 'delete from Car {}'.format(query_V_ID)
        conn.commit() #Commit the changes
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(query)
        flash(f'Information deleted !', 'success')
        return redirect(url_for('home'))
    return render_template('delete.html', title='Delete', form=form)

@app.route("/delete_cascade", methods=['GET', 'POST'])
def delete_cascade():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT distinct(B_ID) FROM Branch")
    results = c.fetchall()
    B_IDs = [(results.index(item), item['B_ID']) for item in results]
    form = DeleteCascadeForm()
    form.B_ID.choices = B_IDs
    if form.validate_on_submit():
        B_ID =  (form.B_ID.choices[form.B_ID.data][1])
        query_B_ID = 'where B_ID = "{}"'.format(B_ID)
        query = 'delete from Branch {}'.format(query_B_ID)
        conn.commit() #Commit the changes
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(query)
        flash(f'All information about {B_ID} has been deleted!', 'success')
        return redirect(url_for('home'))
    return render_template('delete_cascade.html', title='Delete CASCADE', form=form)

@app.route("/aggregate_group_by", methods=['GET', 'POST'])
def aggregate_group_by():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT B_ID, count(*) C, SUM(Price) S FROM Car GROUP BY B_ID")
    posts = c.fetchall()
    return render_template('aggregate_group_by.html', posts=posts)

@app.route("/division", methods=['GET', 'POST'])
def division():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT brand FROM (SELECT DISTINCT(Car.Car_brand) brand FROM Car) a WHERE NOT EXISTS (SELECT b.B_ID FROM Branch b WHERE NOT EXISTS (SELECT c.B_ID FROM Car c WHERE c.B_ID=b.B_ID AND c.Car_brand= a.brand))")
    posts = c.fetchall()
    return render_template('division.html', posts=posts)

@app.route("/aggregate", methods=['GET', 'POST'])
def aggregate():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT count(*) C FROM Car")
    posts = c.fetchall()
    return render_template('aggregate.html', posts=posts)

@app.route("/customer", methods=['GET', 'POST'])
def customer():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT * FROM Customer ORDER BY D_number desc")
    posts = c.fetchall()
    return render_template('customer.html', posts=posts)

@app.route("/select", methods=['GET', 'POST'])
def select():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT distinct(Model) FROM Car")
    results = [{'Model':'ANY'}] + c.fetchall()
    models = [(results.index(item), item['Model']) for item in results]
    c.execute('select distinct(V_ID) from Car')
    results = [{'V_ID':'ANY'}] + c.fetchall()
    V_IDs = [(results.index(item), item['V_ID']) for item in results]
    c.execute('select distinct(Location) from Branch')
    results = [{'Location':'ANY'}] + c.fetchall()
    Locations = [(results.index(item), item['Location']) for item in results]
    c.execute('select distinct(Car_brand) from Car')
    results = [{'Car_brand':'ANY'}] + c.fetchall()
    brands = [(results.index(item), item['Car_brand']) for item in results]
    form = SelectForm()
    form.Model.choices = models
    form.V_ID.choices = V_IDs
    form.Location.choices = Locations
    form.Car_brand.choices = brands
    if form.validate_on_submit():
        model =  (form.Model.choices[form.Model.data][1])
        V_ID = (form.V_ID.choices[form.V_ID.data][1])
        Location = (form.Location.choices[form.Location.data][1])
        brand = (form.Car_brand.choices[form.Car_brand.data][1])
        if model == 'ANY':
            query_model = 'select V_ID from Car'
        else:
            query_model = 'select V_ID from Car where Model = "{}"'.format(model)
        if V_ID == 'ANY':
            query_V_ID = 'select V_ID from Car'
        else:
            query_V_ID = 'select V_ID from Car where V_ID = "{}"'.format(V_ID)
        if Location == 'ANY':
            query_Location = 'select V_ID from Car'
        else:
            query_Location = 'select V_ID from Car c, Branch b where c.B_ID = b.B_ID and Location = "{}"'.format(Location)
        if brand == 'ANY':
            query_brand = 'select V_ID from Car'
        else:
            query_brand = 'select V_ID from Car where Car_brand = "{}"'.format(brand)
        query = 'select * from Car c,Branch b where c.B_ID=b.B_ID and V_ID in ({}) and V_ID in ({}) and V_ID in ({}) and V_ID in ({})'.format(query_model,query_V_ID,query_Location,query_brand)
        conn.commit() #Commit the changes
        flash(f'This is the information you need to retrieve it !', 'success')
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute(query)
        posts = c.fetchall()
        return render_template('display.html', posts=posts)
    return render_template('select.html', title='Select', form=form)

@app.route("/book", methods=['GET', 'POST'])
def book():
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    c.execute("SELECT distinct(V_ID) FROM Car")
    results = c.fetchall()
    V_IDs = [(results.index(item), item['V_ID']) for item in results]
    form = BookForm()
    form.V_ID.choices = V_IDs
    if form.validate_on_submit():
        V_ID =  (form.V_ID.choices[form.V_ID.data][1])
        query = 'Insert into Customer(Name, Phone_No, Email, V_ID) VALUES ("{}", "{}", "{}", "{}")'.format(form.Name.data,form.Phone_No.data,form.Email.data, V_ID)
        c.execute(query) #Execute the query
        conn.commit() #Commit the changes
        flash(f'Booked for {form.Name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('book.html', title='book', form=form)

if __name__ == '__main__':
    app.run(debug=True)
