# document text analyzer for EC530
# By JINGYI ZHANG (jyz0328@bu.edu, U26578499)

# how to run file <br>
- Step0 :download this github
- Step1 :run [python3 ./app.py] in terminal A <br>
- Step2 :run [python3 ./nowclient.py ] in terminal B <br>
- Step3 :then u can see ["What do you want to do? (1 for login, 2 for register, 3 for exit): "], input 1 or 2 or 3 to see effect<br>
- Step4 :if u login successfully u can also see [Choose an option: (1 for upload, 2 for logout): ], input 1 or 2 to see effect<br>, u can use `example.pdf`, `test.txt` or use other pdf or txt files as file for upload
- Step5 :use [control c]to exit backend<br><br>
- Noticecurrently version only document using 'pdf txt' can be analyzed, use any other document will cuase failure, i will address this in furture if i have time<br>

# usage of each component <br>
nowclient.py:frontend, which show things in front of users <br>
app.py : backend , all modules need to be import<br>
auth.py :authcation module<br>
upload.py : upload module<br>
text analyzer.py: text analyze module, a report.txt will also be formed<br>
example.pdf:sample documents for analyzing, you can use other [pdf txt] document , i will try to fix how to use other format such as png if i have time<br>
users.db: database show all valid users name and password <br>
Database Create: documents about how I generate this users.db<br>
docker and quene :current answer for [Link to your Queue Implementatiobn] and [link to your Docker and Installation implementation]<br><br>
My effort[Link to your Queue Implementatiobn] can be found in upload.py<br><br>
what need do later:<br>
must:add test like what project1 did, docker (how to add test?)<br>
optional:how to do with feed ingester such as [Keywords within paragraphs should be searchable<br>
in government opendata, wikipedia and media organizations, e.g., NYTimes ]<br>
optional:how to make more fit analyze for text<br>


