# gcloudpractice

----DataMigrationTool-Code-ONLY Version 1.0----
GCS to Big Query CSV file migrator 

This version is to be run on either a GCP compute engine or in Cloud Shell.
To run from an external application please unhash the line 'from_serivce_account' and create the appropriate JSON key. Then set the key path in the config.py file

Step 1
Please go into the config.py folder and update all values accordingly.

Step 2
Please ensure your bucket contains three folders Source/, Completed/ and Failed/ as the program will look for these folders. 
If using this as a standalone migration pipeline please ensure all CSV files are in the Source Folder in your bucket. 

Step 3 
run dependencies.py 

Step 4 


