""" import nlpcloud
import difflib
import json
from monkeylearn import MonkeyLearn
class TextSummarization:

    #token = '8d3b56019533d689a42599fa70bf719221a5d50a'
    text = 'this morning, while I have been doing the groceries, I felt a strong pain in my chest. After having difficulties breathing for a while, I managed to get up again and drive home with my car. I was very afraid that it happens again since I am living alone and no one would be around to drive me to the hospital.'
    #model_name = 't5-base-en-generate-headline'
    model_name_sentiment= 'distilbert-base-uncased-finetuned-sst-2-english'

    # client & API call
    def GetSummarization(self):
        #''' Function to call the NLP Cloud API to get a summary of the text'''
        # # setup
        text = 'this morning, while I have been doing the groceries, I felt a strong pain in my chest. After having difficulties breathing for a while, I managed to get up again and drive home with my car. I was very afraid that it happens again since I am living alone and no one would be around to drive me to the hospital.'
        token = '8d3b56019533d689a42599fa70bf719221a5d50a'
        model_name = 't5-base-en-generate-headline'#'pegasus-xsum'
        # API call
        client = nlpcloud.Client(model_name, token)
        summary = client.summarization(self.text)
        return summary['summary_text']
        #client = nlpcloud.Client(self.model_name, self.token)
        #summary = client.summarization(self.text)
        #return summary['summary_text']
    
    
    def GetSentiiment(self):
        client = nlpcloud.Client(self.model_name_sentiment, self.token)
        return self.sentiment['scored_labels']

    def PostAudioData(self):
        url = ''
        myobj = {'somekey': 'somevalue'}
    # Keyword extraction
    text = 'this morning, while I have been doing the groceries, I felt a strong pain in my chest. After having difficulties breathing for a while, I managed to get up again and drive home with my car. I was very afraid that it happens again since I am living alone and no one would be around to drive me to the hospital.'
    ml = MonkeyLearn('a6f42191b073097764dd072cda15af041260caea')
    model_id = 'ex_YCya9nrn'
    result = ml.extractors.extract(model_id, [text])

    # get keyword list
    kw_list = []
    for kw in result.body[0]['extractions']:
        if float(kw['relevance']) > 0.4:
            kw_list.append(kw['parsed_value'])

    text_list = text.split()
    def GetKeywordList(self):
        return self.kw_list
        #print(text)#print(kw_list)

    # get position of keyword in text
    def GetPositionOfKeywords(self):
        for kw in self.kw_list:
        # try first to find word via list operation
        # except if its lemmatized and we would fall back to kind of nearest neigbhor search
            try:
                return print(self.text.index(kw))
            except:
                nearest_neighbor = difflib.get_close_matches(kw, self.text_list, n=1, cutoff=0.1)[0]
                print(self.text.index(nearest_neighbor)) """