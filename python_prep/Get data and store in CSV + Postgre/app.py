from flask import Flask, render_template
import requests
import tablib
import os
from os import path
from models.entry import Entry, db
from custom_functions.write_to_csv import writeToCsv
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://root:123@localhost/python_prep"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/csv')
def csv():
    # Get json data from the endpoint
    try:
        response = requests.get("https://api.publicapis.org/entries").json()
    except Exception as e:
        error = f"Error! {e}"
        return render_template('index.html', err=error)
    else:
        try:
            if path.exists('data/data.csv'):
                # Raise custom error
                raise FileExistsError
        # For the error I raised
        except FileExistsError as e:
            error = f"Error! data.csv already exists"
            return render_template('index.html', err=error)
        # Fallback for any other error
        except Exception as e:
            error = f"Error! {e}"
            return render_template('index.html', err=error)
        else:
            try:
                # Calling our method to write data to CSV
                writeToCsv(response["entries"])
                message = "Data Successfully written to file"

                # Read the file and send it to the template using tablib
                dataset = tablib.Dataset()
                with open(os.path.join(os.path.dirname(__file__), 'data/data.csv')) as f:
                    dataset.csv = f.read()
                    print(dataset.csv)

                # Tablib comes with a handy method to render csv files in html
                data = dataset.html
                return render_template('index.html', success=message, csv=data)
            except Exception as e:
                error = f"Error! {e}"
                return render_template('index.html', err=error)


@app.route('/database')
def storeInDatabase():
    # Get json data from the endpoint
    try:
        response = requests.get("https://api.publicapis.org/entries").json()
    except Exception as e:
        error = f"Error! {e}"
        return render_template('index.html', err=error)
    else:
        limit = 0
        for entry in response["entries"]:
            entry = Entry(entry["API"], entry["Description"], entry["Auth"],
                          entry["HTTPS"], entry["Cors"], entry["Link"], entry["Category"])
            try:
                db.session.add(entry)
            except Exception as e:
                error = f"Error! {e}"
                return render_template('index.html', err=error)

            # Limit to insert only 50 records
            limit += 1
            if limit == 50:
                break
        try:
            # Commit the new records to DB
            db.session.commit()
            message = "Data Successfully Stored in database"
        except SQLAlchemyError as e:
            error = e.__dict__['orig']
            return render_template('index.html', err=error)
        else:
            # Get all entries from database
            entries = Entry.query.all()
            return render_template('index.html', success=message, entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
