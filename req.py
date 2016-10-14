import requests
import urllib

# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, session, abort, current_app, json, render_template

app = Flask(__name__)
# This is the very unsecret key from the Flask-docs
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# POST echo form
@app.route('/', methods=['GET', 'POST'])
def post_echo():
    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        img_url = request.form.get('mystring')
        related = get_related_image(img_url)
        return render_template('result.html', img_url=related)

def get_related_image(img_url):

    img_url_encoded = urllib.quote_plus(img_url)
    response = requests.get('https://www.bing.com/images/insights?IG=11427078AF4D41A58B8DAF3116A6EF78&IID=images.4&SFX=1&mode=ImageViewer&iss=sbi&mid=5F5A40B7595E527DD86C25E8D35FC7D70B46CC82&ccid=141ucrNy&vw=cd70f%20629c9%206d1f3%20c23b7%20c1b63%205e6c6%20cd4ba%2012a0a%200fcd8%20cde10%2091a8b%20ab649%20d7eb2%20f0fd6%20cf323%20d8789%208e667%2047693%20c82e2%20d30a2%20c58f68bca8d1d4ab174e10e498be4289368da0a18ca22881b4a96b8605bea38ccc3dab88fb8cac734824d9cea7cbbd0edde5&simid=0&thid=&thh=960&thw=794&q=%20&qpvt=&mst=15&mscr=16&spurl=' + img_url_encoded + '&imgurl=' + img_url_encoded + '&brq=%20&bcid=497B662F30B705BB4C2D86F73B8E5E23')
    content = response.content

    result_url = content.split('<img class="mimg"')[1]
    result_url = result_url.split(' alt="Related image result"/>')[0]
    result_url = result_url.split('src="')[1]
    result_url = result_url.replace('"', "")

    return result_url


# We only need this for local development.
if __name__ == '__main__':
    app.run()
