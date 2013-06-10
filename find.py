

import glob
from BeautifulSoup import BeautifulSoup
import os



start_html = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
  <meta http-equiv="content-type" content="text/html; charset=windows-1250">
  <meta name="generator" content="PSPad editor, www.pspad.com">
  <title></title>
  </head>
  <style type="text/css"><!--
  BODY {
    BACKGROUND-COLOR: #ffffff
 }
  A {   TEXT-DECORATION: none }
  A:visited {   COLOR: #0000cf; TEXT-DECORATION: none }
  A:link {  COLOR: #0000cf; TEXT-DECORATION: none }
  A:active {    COLOR: #0000cf; TEXT-DECORATION: underline }
  A:hover { COLOR: #0000cf; TEXT-DECORATION: underline }
  OL {  COLOR: #333333; FONT-FAMILY: tahoma,helvetica,sans-serif }
  UL {  COLOR: #333333; FONT-FAMILY: tahoma,helvetica,sans-serif }
  P {   COLOR: #333333; FONT-FAMILY: tahoma,helvetica,sans-serif }
  BODY {    COLOR: #333333; FONT-FAMILY: tahoma,helvetica,sans-serif }
  TD {  COLOR: #333333; FONT-FAMILY: tahoma,helvetica,sans-serif }
  TR {  COLOR: #333333; FONT-FAMILY: tahoma,helvetica,sans-serif }
  TH {  COLOR: #333333; FONT-FAMILY: tahoma,helvetica,sans-serif }
  FONT.title {  BACKGROUND-COLOR: white; COLOR: #363636; FONT-FAMILY:
                tahoma,helvetica,verdana,lucida console,utopia; FONT-SIZE: 10pt; FONT-WEIGHT: bold }
  FONT.sub {    BACKGROUND-COLOR: white; COLOR: #000000; padding-left: 5px; FONT-FAMILY:
                tahoma,helvetica,verdana,lucida console,utopia; FONT-SIZE: 10pt }
  FONT.layer {  COLOR: #ff0000; FONT-FAMILY: courrier,sans-serif,arial,helvetica; FONT-SIZE: 8pt; TEXT-ALIGN: left }
  TD.title {    BACKGROUND-COLOR: #4477BB; COLOR: #FFFFFF; FONT-FAMILY:
                tahoma,helvetica,verdana,lucida console,utopia; FONT-SIZE: 10pt; FONT-WEIGHT: bold; HEIGHT: 20px; TEXT-ALIGN: right }
  TD.sub {      BACKGROUND-COLOR: #CCCCCC; COLOR: #000000; FONT-FAMILY:
                tahoma,helvetica,verdana,lucida console,utopia; FONT-SIZE: 10pt; FONT-WEIGHT: bold; HEIGHT: 18px; TEXT-ALIGN: left }
  TD.content {  BACKGROUND-COLOR: white; COLOR: #000000; padding-left: 5px;
                FONT-FAMILY: tahoma,arial,helvetica,verdana,lucida console,utopia; FONT-SIZE: 8pt; TEXT-ALIGN: left; VERTICAL-ALIGN: top }
  TD.wide60 {   width: 60% }
  TD.wide50 {   width: 50% }
  TD.wide30 {   width: 30% }
  TD.wide25 {   width: 25% }
  TD.wide20 {   width: 20% }
  TD.high   {   color: #E60000; font-weight: bold }
  TD.medium {   color: #E67300; font-weight: bold }
  TD.low    {   color: #999900; font-weight: bold }
  TD.attention {color: green; font-weight: bold }
  TD.high-th   {   background-color: #CC0000; font-weight: bold}
  TD.medium-th {   background-color: darkorange; font-weight: bold }
  TD.low-th    {   background-color: goldenrod; font-weight: bold }
  TD.attention-th {background-color: green; font-weight: bold }
  TD.center {   text-align: center }

  TD.default {  BACKGROUND-COLOR: WHITE; COLOR: #000000; FONT-FAMILY:
                tahoma,arial,helvetica,verdana,lucida console,utopia; FONT-SIZE: 8pt; }
  TD.border {   BACKGROUND-COLOR: #cccccc; COLOR: black; FONT-FAMILY:
                tahoma,helvetica,verdana,lucida console,utopia; FONT-SIZE: 10pt; HEIGHT: 25px }
  TD.border-HILIGHT {   BACKGROUND-COLOR: #ffffcc; COLOR: black; FONT-FAMILY:
                        verdana,arial,helvetica,lucida console,utopia; FONT-SIZE: 10pt; HEIGHT: 25px }
  #high      {   color: #E60000; font-weight: bold }
  #medium    {   color: #E67300; font-weight: bold }
  #low       {   color: #999900; font-weight: bold }
  #attention {   color: green; font-weight: bold }
  #other     {   font-weight: bold }
  #returnlink{   text-align: left; font-size:60% }
  
   --></style></body>
'''
end_html = ''' </body></html>'''   
list_files = []               
findings = []   
def create_export(test):
    if test == True:
        new_file = open("export.html","w")
        new_file.write(start_html)
        print len(findings)
     
        text = "{0}{1}".format(start_html,end_html)
             
        new_file.write(text)
        
           
                  
#         new_file.write(test)
        new_file.write(end_html)
        new_file.close()
    else:
        AttributeError
    

for files in glob.glob("*.html"):
        list_files.append(files)

if "export.html" in list_files:
        path = os.getcwd() + "\\" + "export.html"
        path = path.replace("\\","/")
        os.remove(path)      
        print "i found export and delete it" 
else:
    for report in list_files:
        soup = BeautifulSoup(open(report).read())
        replace = soup.findAll('table') 
        findings.append(replace[3])
    create_export(True)
            

           
    
        
        
  
    
    
    
    
    