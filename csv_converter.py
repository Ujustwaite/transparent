## Code to aid in creating text corpus for Transparent Language projects
## Author: Brian Waite, brianwaite@protonmail.com
## Requires the creation of a directory titled "converter" in the same level as this script
## Place however many csv files as you want in the converter folder and this code handles the rest


#imports section
import pandas as pd
import os
#Set up some directory paths
target_path = 'converter'
output_path = target_path + '/output'
#Check for existence and create if not exists
if not (os.path.exists(output_path)):
  os.mkdir(output_path)

#Get list of csv files to be processed
files = os.listdir(target_path)

#iterate over the csv files and create the excel spreadsheets
for file in files:
  if file.endswith('csv'):
      df = pd.read_csv(target_path +'/'+ file)
      nouns = df[df.pos == 'NOUN']
      verbs = df[df.pos == 'VERB']
      adj = df[df.pos == 'ADJ']
      adv = df[df.pos == 'ADV']

      with pd.ExcelWriter(output_path + '/' + file[0:-4] + '.xlsx') as writer:
         df.to_excel(writer, sheet_name = file[0:-4])

         nouns.to_excel(writer, sheet_name='NOUN')

         verbs.to_excel(writer, sheet_name='VERB')

         adj.to_excel(writer, sheet_name='ADJ')

         adv.to_excel(writer, sheet_name='ADV')
