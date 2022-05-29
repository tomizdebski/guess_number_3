"""
Gra w zgadywanie liczb 3
Warsztat: Gra w zgadywanie liczb 3

Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy frameworka Flask.
Użytkownik dostaje do dyspozycji formularz z trzema guzikami: To small, To big, You win.

Informacje o aktualnych zmiennych min i max przechowuj w ukrytych polach formularza (pole typu hidden).

Uwaga – nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla, np. przy pomocy Firebuga.
W tej sytuacji jednak zupełnie wystarczające. Najwyżej zepsuje sobie zabawę ;)
"""
from random import randint, shuffle, sample
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

liczba_do_zgadniecia = randint(1,100)


@app.route('/zgadywanka',methods=["GET", "POST"])
def zgadywanka():
    html = """
    <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css">
    <h2>Formularz do witania się:</h2>

    <form action="/zgadywanka" method="POST">
        <label>Liczba:
        <input type="number" name="liczba"/>
        </label>
        <button type="submit">Zgaduję</button>
    </form>
    """
    if request.method == 'POST':
        liczba_gracza = int(request.form['liczba'])
        if liczba_gracza < liczba_do_zgadniecia:
            return "<h2>Za mało</h2>"+html
        elif liczba_gracza > liczba_do_zgadniecia:
            return "<h2>Za dużo</h2>" + html
        else:
            return "Trafiłeś"
    else:
        return html

if __name__ == "__main__":
    app.run(debug=True)





