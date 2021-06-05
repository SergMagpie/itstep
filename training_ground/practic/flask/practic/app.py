from flask import Flask, make_response, render_template, request, redirect, url_for, session

app = Flask(__name__)

students_dict = {1: "Jhon Wowich", 2: "Karl Lagerfield", 3: "Bill Klinton", 4: "Teo Bear"}

@app.route("/itstep")
def itstep():
    return "Hello ITSTEP!!"


@app.route("/")
def index():
    # return "Index page/ Main page"
    
    response = make_response("<h4>400 Error</h4>", 400)
    response.set_cookie("404", "true", max_age=0)
    return response

@app.route("/students/")
def students():
        return render_template("students.html", students=students_dict)

@app.route("/students/<int:id>/")
def student(id):
    if id in students_dict:
        return render_template("student.html", name=students_dict.get(id))
    else:
        return make_response("<h2>Student not found</h2>", 404)

@app.route("/add", methods=["POST"])
def add_student():
    print(request.form)
    try:
        new_name = request.form.get("name")
        students_dict[len(students_dict) + 1] = new_name
    except:
        print("Error")
    return redirect(url_for("students"))

@app.route("/students/add")
def student_add():
    return render_template("student_add.html")

if __name__ == "__main__":
    app.run(debug=True)