
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def madlibs():
    story = None
    if request.method == 'POST':
        selected = request.form.get('story')
        adjective = request.form.get('adjective')
        noun = request.form.get('noun')
        verb = request.form.get('verb')
        place = request.form.get('place')
        if selected == "1":
            story = f"Once upon a time in a {adjective} land, there was a {noun} who loved to {verb}. Every day, the {noun} would visit {place} to share its adventures. The end!"
        elif selected == "2":
            story = f"In a {adjective} city, a {noun} decided to {verb} at {place}. The {noun}'s journey was filled with excitement and surprises. The end!"
        elif selected == "3":
            story = f"Deep in the {adjective} forest, a {noun} loved to {verb}. One day, it stumbled upon {place}, changing its life forever. The end!"
        else:
            story = "Invalid selection. Please restart the game and choose 1, 2, or 3."
        return render_template('result.html', story=story)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)

# end of madlibs game