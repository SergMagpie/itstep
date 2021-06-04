from src import app
from src.my_api import MyAPI
from flask import render_template, request, redirect, make_response, url_for

words_list = MyAPI()


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/words/")
def words():
    return render_template("words.html", words=words_list)


@app.route("/words/<word>/")
def word(word):
    for w in words_list:
        if w.word == word:
            rez = make_response(
                render_template("word.html",
                                word=w.word,
                                translate=w.translate,
                                title=word))
            rez.set_cookie(word, 'WLearn', max_age=60 * 60 * 24 * 7)
            return rez
    else:
        return make_response("<h2>Word not found</h2>", 404)


@app.route("/addword", methods=["POST"])
def adding_word():
    print(request.form)
    try:
        new_word = request.form.get("word")
        new_translate = request.form.get("translate")
        words_list.append(new_word, new_translate)
    except Exception as inst:
        print("Error", inst)
    return redirect(url_for("words"))


@app.route("/changeword", methods=["POST"])
def changing_word():
    print(request.form)
    try:
        old_word = request.form.get("oldword")
        new_word = request.form.get("word")
        new_translate = request.form.get("translate")
        if old_word in words_list:
            words_list.update(old_word, new_word, new_translate)
            return redirect(url_for("words"))
        else:
            return make_response("<h2>Word not found</h2>", 404)
    except Exception as inst:
        print("Error", inst)
    return redirect(url_for("words"))


@app.route("/change-word/<word>/")
def change_word(word):
    for w in words_list:
        if w.word == word:
            return render_template("change_word.html",
                                   word=w.word,
                                   translate=w.translate)
    else:
        return make_response("<h2>Word not found</h2>", 404)


@app.route("/delete-word/<word>")
def delete_word(word):
    for w in words_list:
        if w.word == word:
            words_list.remove(w)
            return redirect(url_for("words"))
    else:
        return make_response("<h2>Word not found</h2>", 404)


@app.route("/mark-word/<word>")
def mark_word(word):
    if word in words_list:
        words_list.mark(word)
        return redirect(url_for("words"))
    else:
        return make_response("<h2>Word not found</h2>", 404)


@app.route("/add")
def add_word():
    return render_template("word_add.html")


if __name__ == "__main__":
    app.run(debug=True)