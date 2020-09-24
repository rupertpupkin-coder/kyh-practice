import requests

ENDPOINT = 'https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda'


class QuizzWebServiceAPI(object):

    def __init__(self):
        self.url = ENDPOINT

    def get_all_questions(self):
        r = requests.get(self.url)
        ls = r.json()['questions']
        return ls

    def add_question(self, prompt, answer, alternatives):
        data = {
            'prompt': prompt,
            'rightAnswer': answer,
            'wrongAnswers': alternatives
        }
        r = requests.post(url=self.url, json=data)
        return True if r.status_code == 200 else False

if __name__ == '__main__':
    call_mod = QuizzWebServiceAPI()

