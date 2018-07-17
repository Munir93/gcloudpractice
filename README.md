# gcloudpractice

----DataMigrationTool-Code-ONLY Version 1.0----
GCS to Big Query CSV file migrator 

This version is to be run on either a GCP compute engine or in Cloud Shell.
To run from an external application please unhash the line 'from_serivce_account' and create the appropriate JSON key. Then set the key path in the config.py file

Step 1
Please go into the config.py folder and update all values accordingly. Please ignore the tiwtter etl section 

Step 2
Please ensure your bucket contains three folders Source/, Completed/ and Failed/ as the program will look for these folders. 
If using this as a standalone migration pipeline please ensure all CSV files are in the Source Folder in your bucket. 

Step 3 
run dependencies.py 

Step 4 
run gs-bq-migration.py

blob-move.py is to move files in the Failed folder to Source folder to retry migration. 





----DataMigrationTwitterETL-Code-ONLY Version 1.0----
Streams tweets and submits as csv to GCS

This version is to be run on either a GCP compute engine or in Cloud Shell.

This version is to be run on either a GCP compute engine or in Cloud Shell.
To run from an external application please unhash the line 'from_serivce_account' and create the appropriate JSON key. Then set the key path in the config.py file

Step 1
Please go into the config.py folder and update all values accordingly under the twitter ETL section 
Track term is currently set to 'Brexit' but change to what hashtag you with to track
default settings are the the tweets will run for 10 secs then submit to gcs. This can be changed in the 

Step 2
Please ensure your bucket contains a Source/ folder

Step 3 
run dependencies.py 

Step 4 
run tw



