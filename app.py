from flask import Flask, render_template, send_from_directory
import os
import json
app = Flask(__name__)

Samples = "Samples"


@app.route('/')
def hello():
	with open('buttons.json') as f:
		data = json.load(f)
	buttons = {}
	for key in data:
		if data[key] != "":
			s = data[key][data[key].index('/') + 1:]
			buttons[key] = {s.replace('-', ' ')[:s.index('.')]: data[key]}
		else:
			buttons[key] = {"undefined": "undefined"}
	indexTemplate = {
		"categories": {f: {s.replace('-', ' ')[:s.index('.')]: s for s in os.listdir(os.path.join("Samples/",f))} 
						for f in os.listdir("Samples")},
		"buttons": buttons,
	}
	print sorted(buttons.keys())
	return render_template('index.html', **indexTemplate)


@app.route('/sound/<c>/<s>')
def send_js(c, s):
    return send_from_directory(os.path.join('Samples', c), s)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')