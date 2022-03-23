import pandas as pd
import numpy as np
from PIL import Image
import pickle
import requests
from io import BytesIO

from dataclasses import dataclass
@dataclass(frozen=True)
class Url:
    """Wrapper around a URL string to provide nice display in IPython environments."""
    # from: https://github.com/jupyterlab/jupyterlab/issues/7393

    __url: str

    def _repr_html_(self):
        """HTML link to this URL."""
        return f'<a href="{self.__url}">{self.__url}</a>'

    def __str__(self):
        """Return the underlying string."""
        return self.__url


def load_cards(path='./cards.pkl'):

    with open(path, 'rb') as f:
        return pickle.load(f)
        
study_questions = load_cards()
question_log = [0]


def view_flashcard(q_id=0, topic='data_science'):
    """Select a flash card by id number. If q_id is 0, a random question will be displayed"""

    global question_log
    rng = 1

    if q_id != 0:
        try:
            # update question log
            question_log.append(q_id)

            return study_questions[topic][q_id]['question']
        except:
            max_id = (len(study_questions[topic].keys()) + 1)
            return f'Invalid question ID. Try a number between 1-{max_id}'

    else:
        # get random question id
        rng = np.random.choice(
                range(
                    1, (len(study_questions[topic].keys()) + 1) 
                    )
                )
        q_id = rng
        
        # update question log
        question_log.append(q_id)
        
        # print question
        return study_questions[topic][q_id]['question']


def view_answer(q_id=0, topic='data_science'):
    global question_log
    output = {}
    
    if q_id == 0:
        q_id = question_log[-1]
    text_answers = study_questions[topic][q_id]['answer']['text']
    image_answers = study_questions[topic][q_id]['answer']['img']
    video_answers = study_questions[topic][q_id]['answer']['video']

    output['text'] = text_answers
    output['images'] = image_answers    
    output['video'] = video_answers

    return output
    # if len(image_answers) > 0:
    #     for image in image_answers:
    #         response = requests.get(image)
    #         im = Image.open(BytesIO(response.content))
    #         display(im) 
    
    # if len(video_answers) > 0:
    #     for video in video_answers:
    #         display(Url(video))    
