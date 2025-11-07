from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'POST':
        mood = request.form.get('mood').lower()
        if "happy" in mood or "good" in mood:
            quote = "The only way to do great work is to love what you do. - Steve Jobs"
        elif "sad" in mood or "down" in mood:
            quote = "Even the darkest night will end and the sun will rise. - Victor Hugo"
        elif "stressed" in mood or "anxious" in mood:
            quote = "Grant me the serenity to accept the things I cannot change, courage to change the things I can, and wisdom to know the difference. - Reinhold Niebuhr"
        else:
            quote = "Every day may not be good, but there's something good in every day."
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
