from flask import Flask, render_template, request, redirect
from stackoverflow_practice import get_jobs

app = Flask('SupperScrapper')

@app. route("/")
def home():
    return render_template('jobSearch.html')

@app.route("/report")
def report():
    search = request.args.get('search')
    if search:
        search = search.lower()
        jobs = get_jobs(search)
        print(jobs)
    else:
        return redirect("/")
    return render_template('report.html',serchingBy=search)
