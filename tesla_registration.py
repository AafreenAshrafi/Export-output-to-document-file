import PyPDF2,os

print('''Tesla Welcomes you 
        Please enter the details below:
        ''')
name= input('enter the customer name ')
mno= input ('enter mobile No ')
age= input('Age of customer ')
city= input ('city for registration ')
extension= input('the extension to save the details eg: txt, pdf,doc,docx ')
result= ('name = {} mobile no= {} age ={} city = {}'.format(name,mno,age,city))
#result = result.encode('utf-8')
output= 'output' + '.' + extension

# **********The output file will be saved in same directory in which the file Tesla_registration is present.************************
# **********Also txt extension can be browsable from the directory where as other content type maybe corrupted
# but we can use the file for the output will show in console as shown below.*************

fileoutput = open(output,'w',encoding='utf8') 
fileoutput.write(result)
fileoutput.close()
FileObj = open(output, 'r',encoding='utf8').read()
print ('output of your file is : ', FileObj) #In console output all the content type output can be read.
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

