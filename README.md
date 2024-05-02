# document text analyzer for EC530
# By JINGYI ZHANG (jyz0328@bu.edu, U26578499)

# how to run file
- Step0 :download this github
- Step1 :run [python3 ./app.py] in terminal A
- Step2 :run [python3 ./nowclient.py ] in terminal B
- Step3 :then u can see ["What do you want to do? (1 for login, 2 for register, 3 for exit): "], input 1 or 2 or 3 to see effect
- Step4 :if u login successfully u can also see [Choose an option: (1 for upload, 2 for logout): ], input 1 or 2 to see effect, u can use `example.pdf`, `test.txt` or use other pdf or txt files as file for upload
- Step5 :use [control c]to exit backend
- Notice : currently version only document using 'pdf txt' can be analyzed, use any other document will cuase failure, i will address this in furture if i have time<br>
- Notice : u can also follow `Docker_and_Packaging` folder to download the codes in packaging method

# usage of each component <br>
- `nowclient.py` :frontend, which show things in front of users.
- `app.py` : backend , all other codes modules need to be imported and connected here.
- `auth.py` :authcation module, which is used for login, logout, register users.
- `upload.py` : upload module, which is used for upload documents. I also do quene implementation in this code .
- `textanalyzer.py`: text analyze module, which is used for analyze text of upload document , the analyzing result will be saved as a report.txt automatically<br>
- `example.pdf` `test.txt`:sample documents for analyzing, you can use other [pdf / txt] document 
- `users.db`: database show all valid users name and password 
- `Database Create` folder : documents about how I generate this users.db
- `Queue Implementation` folder : In this folder I explain what I do for quene implementation. Check `Quene_Implement_Report.pdf` to see detailed explanation
- `Docker_and_Packaging` folder: in this folder explain what i did for python packaging.
- `docker and quene` previous answer for [Link to your Queue Implementatiobn] and [link to your Docker and Installation implementation], needs to be abandoned<br><br>

what need do later:<br>
must:add test like what project1 did,then add unit test part into `Queue Implementation`  and `Docker_and_Packaging` <br>
optional:how to do with feed ingester such as [Keywords within paragraphs should be searchable<br>
in government opendata, wikipedia and media organizations, e.g., NYTimes ]<br>
optional:how to make more fit analyze for text<br>
optional:how to use other format such as png if i have time


