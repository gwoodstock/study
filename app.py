from dash import Dash, dcc, html, Input, Output, callback_context
from study import load_cards, view_flashcard, view_answer
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import os
import pickle



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

study_questions = load_cards()
question_log = [0]


app.layout = html.Div([
    html.H2('Time to Study Data Science'),
    html.Button('Next Question', id='btn-question', n_clicks=0),
    html.Button('Show Answer', id='btn-answer', n_clicks=0),
    html.Div(id='display-question'), html.Br(),
    html.Div(id='display-answer'), html.Br(),
    html.Img(id='display-img', src='https://picsum.photos/536/354')
])

@app.callback(
    Output('display-question', 'children'),
    Input('btn-question', 'n_clicks')
    )
def button_flashcard(btn_q):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    print(changed_id)
    question = 'Click button for new question.'
    
    if 'btn-question' in changed_id:
        question = view_flashcard(q_id=0)
        print(question)

    return question


@app.callback(
    # [
        Output('display-answer', 'children'),
    #  Output('display-img', 'children')
    # ],
    Input('btn-answer', 'n_clicks')
    )
def button_answer(btn_q):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    print(changed_id)
    answer = 'Click button for answer.'
    
    if 'btn-answer' in changed_id:
        answer = view_answer(q_id=0)

        text_answer = answer['text']
        # image_answer = answer['img']
        # video_answer = answer['video']
        # img = 'https://plot.ly/~chris/1639.png'
        # response = requests.get(img)
        # im = Image.open(BytesIO(response.content))

        return text_answer#, img

    return answer

if __name__ == '__main__':
    app.run_server(debug=True)