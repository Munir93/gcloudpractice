import apache_beam as beam

import config

import json
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io.gcp.internal.clients import bigquery

options = PipelineOptions()

google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = config.PROJECT_ID
google_cloud_options.staging_location = 'gs://dod-mwja-project1/staging'
google_cloud_options.temp_location = 'gs://dod-mwja-project1/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'
options.view_as(StandardOptions).streaming = True



def parse_pubsub(line):
    import json
    record = json.loads(line)
    return (record['Name']), (record['Tweet']), (record['Time']), (record['Followers']), (record['Location']), (record['Device'])

def handle_pubsub(line):
    templist = line.split('-=-')
    for j, item in enumerate(templist):
        templist[j] = item.replace(',', '')

    diction = dict(zip(config.COLUMN_NAMES, templist))
    f = json.dumps(diction)
    return f
#    | beam.Map(lambda Name_bq, Tweet_bq, Time_bq, Followers_bq, Location_bq, Device_bq: {'Name':Name_bq , 'Tweet':Tweet_bq, 'Time': Time_bq, 'Followers':Followers_bq, 'Location':Location_bq, 'Source':Device_bq})

def run(argv=None):




    with beam.Pipeline(options=options) as p:
        # Read the pubsub topic into a PCollection.
        lines = (p | beam.io.ReadStringsFromPubSub(topic='projects/warm-airline-207713/topics/twitter-stream')
                   | beam.Map(handle_pubsub)
                   | beam.io.WriteToBigQuery('warm-airline-207713:Tweets_raw.Donald_Trump_Tweets',
                    schema='Username:STRING, Tweet:STRING, Time:TIMESTAMP, Followers:INTEGER, Location:STRING, Source:STRING',
                    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))

if __name__ == '__main__':
    run()


