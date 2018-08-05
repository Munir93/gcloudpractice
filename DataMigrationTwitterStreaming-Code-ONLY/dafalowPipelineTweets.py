import apache_beam as beam

import config

import json
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io.gcp.internal.clients import bigquery
from textblob import TextBlob

options = PipelineOptions()

google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = config.PROJECT_ID
google_cloud_options.staging_location = 'gs://dod-mwja-project1/staging'
google_cloud_options.temp_location = 'gs://dod-mwja-project1/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'
options.view_as(StandardOptions).streaming = True




def compute_sentiment(line):
    import os
    os.system('sudo pip install textblob')
    from textblob import TextBlob
    templist = line.split('-=-')
    for j, item in enumerate(templist):
        templist[j] = item.replace(',', '')
    tweet = templist[1]
    sent = TextBlob(tweet).sentiment.polarity
    templist.append(str(sent))

    diction = dict(zip(['Username', 'Tweet', 'Time', 'Followers', 'Location', 'Source', 'Sentiment'], templist))

    return diction

class sentimentDoFn(beam.DoFn):
    def process(self, element):
        import os
        os.system('sudo pip install textblob')
        from textblob import TextBlob
        templist = element.split('-=-')
        for j, item in enumerate(templist):
            templist[j] = item.replace(',', '')
        tweet = templist[1]
        sent = TextBlob(tweet).sentiment.polarity
        templist.append(sent)

        diction = dict(zip(['Username', 'Tweet', 'Time', 'Followers', 'Location', 'Source', 'Sentiment'], templist))
        return diction
def run(argv=None):




    with beam.Pipeline(options=options) as p:
        # Read the pubsub topic into a PCollection.
        lines = (p | beam.io.ReadStringsFromPubSub(topic='projects/warm-airline-207713/topics/twitter-stream')
                   | beam.ParDo(sentimentDoFn())
                   | beam.io.WriteToBigQuery('warm-airline-207713:Tweets_raw.Donald_Trump_Tweets_DS',
                    schema='Username:STRING, Tweet:STRING, Time:TIMESTAMP, Followers:INTEGER, Location:STRING, Source:STRING, Sentiment:FLOAT',
                    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))

if __name__ == '__main__':
    run()


