# document text analyzer for EC530
# By JINGYI ZHANG (jyz0328@bu.edu, U26578499)

# how to run file
- Step0 :download files of this github
- Step1 :run [python3 ./app.py] in terminal A
- Step2 :run [python3 ./nowclient.py ] in terminal B
- Step3 :then u can see ["What do you want to do? (1 for login, 2 for register, 3 for exit): "], input 1 or 2 or 3 to see effect
- Step4 :if u login successfully u can also see [Choose an option: (1 for upload, 2 for logout): ], input 1 or 2 to see effect, u can use `example.pdf`, `test.txt` `grade.pdf``resume.pdf` or use other pdf or txt files as file for upload
- Step5 :use [control c]to exit backend
- Notice : one of username is [OKOK] with [okok] as password. one of username is [wewe] with [wewe] as password, they are stored in users.db, you can use them directly for convenient.
- Notice : currently version only document using 'pdf txt' can be analyzed, use any other document will cuase failure, i will address this in furture if i have time<br>
- Notice : u can also follow `Docker_and_Packaging` folder to download the codes in packaging method. Here is also my documentation link: https://test.pypi.org/project/EC530-project2-new/0.1.0/

# demo of code 
- see `DEMO_report.pdf`

# how to run test
- Step 0:download `tests`  folder of this github
- Step 1:open `test_upload` folder, then run [pytest test_upload.py] in terminal
- Step 2:open `test_textanalyzer` folder, then run [pytest test_textanalyzer.py] in terminal
- demo of this are built in `DEMO_Report.pdf`
 
# usage of each component <br>
- `nowclient.py` :frontend, which show things in front of users.
- `app.py` : backend , all other codes modules need to be imported and connected here.
- `auth.py` :authcation module, which is used for login, logout, register users.
- `upload.py` : upload module, which is used for upload documents. I also do quene implementation in this code .
- `textanalyzer.py`: text analyze module, which is used for analyze text of upload document , the analyzing result will be saved as a report.txt automatically<br>
- `example.pdf` `test.txt` `grade.pdf``resume.pdf`:sample documents for analyzing, you can use other [pdf / txt] document 
- `users.db`: database show all valid users name and password
- `DEMO_Report.pdf`:demo of this code 
- `tests` folder : documents about my unit tests
- -`demo_and_results` folder : documents about my demo and results of original docuemnts after text analyzering
- `Queue Implementation` folder : In this folder I explain what I do for quene implementation. Check `Quene_Implement_Report.pdf` to see detailed explanation
- `Docker_and_Packaging` folder: in this folder explain what i did for python packaging. Here is also my documentation link: https://test.pypi.org/project/EC530-project2-new/0.1.0/ , see more details in `Packaging and Docker Report.pdf`
- `docker and quene` previous answer for [Link to your Queue Implementatiobn] and [link to your Docker and Installation implementation], however the answers of these two links have already updated by other two links, so this folder is not necessary now<br><br>

what need do later:<br>
must:try to demonstrate data protection, then update quene implemnation /readme/docker and packaging <br>
optional:how to do with feed ingester such as [Keywords within paragraphs should be searchable<br>
in government opendata, wikipedia and media organizations, e.g., NYTimes ]<br>
optional:how to make more fit analyze for text<br>
optional:how to use other format such as png if i have time


