## Code to aid in creating text corpus for Transparent Language projects
## Author: Brian Waite, brianwaite@protonmail.com
## Requires the creation of a directory titled "converter" in the same level as this script
## Place however many zip files as you want in the converter folder and this code handles the rest
## Zip files should contain .docx files with the text corpus
## The code will create a directory at the same level of the script for each zip file in .txt format

#Imports section
import pypandoc
import os
import zipfile
import codecs
#Set some paths
target_path = 'converter'
unzipped_output_path = 'converter/unzipped'
#Get list of zip files
files = os.listdir(target_path)

#Loop over zip files
for file in files:
    #ignore non zip files and create some directories needed
    if file.endswith('zip'):
        output_path = file[0:-4]
        if not (os.path.exists(output_path)):
            os.mkdir(output_path)
        if not (os.path.exists(unzipped_output_path)):
            os.mkdir(unzipped_output_path)
        if not (os.path.exists(unzipped_output_path + '/' + file[0:-4])):
            os.mkdir(unzipped_output_path + '/' + file[0:-4])
        #Extract the zip files to a directory where they can be processed
        zipped_files = zipfile.ZipFile(target_path + '/' + file).extractall(unzipped_output_path + '/' + file[0:-4])

    #Start processing the docx files
    files = os.listdir(unzipped_output_path + '/' + file[0:-4])
    text_list = []
    #iterate over all the .docx files
    for file2 in files:
        if file2.endswith('docx'):
            #perform the conversion
            text_list.append(pypandoc.convert_file(unzipped_output_path +'/'+ file[0:-4] + '/' + file2, "plain", format="docx", extra_args=(), encoding='utf-8')) #outputfile=(output_path + '/' + file2 +'.txt'))
    #Create a txt file placeholder, append the txt, and close before ending
    f = codecs.open(output_path + '/' + 'output.txt', "w", encoding='utf-8')
    for item in text_list:
        f.write("%s\n" % item)
    f.close()
