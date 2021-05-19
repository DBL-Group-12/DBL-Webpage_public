from os import link
from flask import Flask, app, render_template
import pandas as pd
import csv,json



csv_file_path = './static/enron-v1.csv'


json_file_path = './Template/Enron.json'

json_new_enron = './Template/Forced_graph.json'

json_3d_scatter = './Template/3d_scatter.json'



data = {}
with open(csv_file_path) as csvFile:
   csvReader = csv.DictReader(csvFile)
   for csvRow in csvReader:
      date = csvRow['date']
      data[date] = csvRow

#add a route to the dictionary

root = {}
root['node'] = data

edge = {}
edge['link'] = root
      
with open(json_file_path, "w") as jsonFile:
   Enron_json = jsonFile.write(json.dumps(data, indent=4))


cols_list = ["fromEmail", "toEmail", "sentiment"]
df_new = pd.read_csv(csv_file_path, usecols=cols_list)

#df_new.to_csv(r'C:\Users\20201077\Desktop\Doruk Güngör\Eindhoven\Computer Science\Year 1\Q4\DBL-Webtech\Phyton\static\scatter_3d.csv')

csv_3d = './static/scatter_3d.csv'

new_data = {}
with open(csv_3d) as csvFile_1:
   csvReader_1 = csv.DictReader(csvFile_1)
   for csvRow_1 in csvReader_1:
      fromEmail = csvRow_1['fromEmail']
      new_data[fromEmail] = csvRow_1


with open(json_3d_scatter, "w") as jsonFile:
   Enron_3d_Json = jsonFile.write(json.dumps(new_data, indent=4))



#Bunu silme
app =Flask(__name__,template_folder= "Template")





#Bunu silme
@app.route('/')
def homepage():
   return render_template("Base.html")


@app.route('/data')
def data():
    filename = './static/enron-v1.csv'
    data = pd.read_csv(filename, header=0)
    myData = list(data.values)
    
    return render_template('data.html', myData=myData)

@app.route('/visualizations/Template/Forced_graph.json', methods = ['GET', 'POST'])
def Enron_force():
   with open("./Template/Forced_graph.json") as file:
      enron_data = file.read()
      return enron_data
   

@app.route('/visualizations/Template/Enron_3d_scatter.json', methods = ['GET', 'POST'])
def Enron_3d():
   with open("./Template/3d_scatter.json") as file:
      enron_data_3d_SCATTER = file.read()
      return enron_data_3d_SCATTER



@app.route('/visualizations/Template/Enron.json', methods = ['GET', 'POST'])
def Enron():
   with open("./Template/Enron.json") as file:
      enron_data = file.read()
      return enron_data
   
   
#Bunu silme
@app.route('/visualizations/')
def visulizations():
   return render_template("AQ.html")







#Bunu silme
if __name__ == "__main__":
    app.run(debug=True)