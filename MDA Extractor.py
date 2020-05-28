
with open(address, 'r', encoding='UTF-8', errors='ignore') as myfile:
        document = myfile.read()
    # doc_len = len(doc)
    document = re.sub('(May|MAY)', ' ', document)  # drop all May month references
    p = document.upper()  # for this parse caps aren't informative so shift
######Remove <DIV>, <TR>, <TD>, and <FONT>##########################
        p = re.compile(r'(<DIV.*?>)|(<DIV\n.*?>)|(<DIV\n\r.*?>)|(<DIV\r\n.*?>)|(<DIV.*?\n.*?>)|(<DIV.*?\n\r.*?>)|(<DIV.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<div.*?>)|(<div\n.*?>)|(<div\n\r.*?>)|(<div\r\n.*?>)|(<div.*?\n.*?>)|(<div.*?\n\r.*?>)|(<div.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<TD.*?>)|(<TD\n.*?>)|(<TD\n\r.*?>)|(<TD\r\n.*?>)|(<TD.*?\n.*?>)|(<TD.*?\n\r.*?>)|(<TD.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<td.*?>)|(<td\n.*?>)|(<td\n\r.*?>)|(<td\r\n.*?>)|(<td.*?\n.*?>)|(<td.*?\n\r.*?>)|(<td.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<TR.*?>)|(<TR\n.*?>)|(<TR\n\r.*?>)|(<TR\r\n.*?>)|(<TR.*?\n.*?>)|(<TR.*?\n\r.*?>)|(<TR.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<tr.*?>)|(<tr\n.*?>)|(<tr\n\r.*?>)|(<tr\r\n.*?>)|(<tr.*?\n.*?>)|(<tr.*?\n\r.*?>)|(<tr.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<FONT.*?>)|(<FONT\n.*?>)|(<FONT\n\r.*?>)|(<FONT\r\n.*?>)|(<FONT.*?\n.*?>)|(<FONT.*?\n\r.*?>)|(<FONT.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<font.*?>)|(<font\n.*?>)|(<font\n\r.*?>)|(<font\r\n.*?>)|(<font.*?\n.*?>)|(<font.*?\n\r.*?>)|(<font.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<P.*?>)|(<P\n.*?>)|(<P\n\r.*?>)|(<P\r\n.*?>)|(<P.*?\n.*?>)|(<P.*?\n\r.*?>)|(<P.*?\r\n.*?>)')
        str1=p.sub("",str1)
        p = re.compile(r'(<p.*?>)|(<p\n.*?>)|(<p\n\r.*?>)|(<p\r\n.*?>)|(<p.*?\n.*?>)|(<p.*?\n\r.*?>)|(<p.*?\r\n.*?>)')
        str1=p.sub("",str1)
        str1=str1.replace("</DIV>","")
        str1=str1.replace("</div>","")
        str1=str1.replace("</TR>","")
        str1=str1.replace("</tr>","")
        str1=str1.replace("</TD>","")
        str1=str1.replace("</td>","")
        str1=str1.replace("</FONT>","")
        str1=str1.replace("</font>","")
        str1=str1.replace("</P>","")
        str1=str1.replace("</p>","")
        
############# Remove XBRL Sections #########################
                
        output=str1
        locations_xbrlsmall=xbrl_clean("<xbrl", "</xbrl.*>", output)
        locations_xbrlsmall.append(len(output))
        
        if locations_xbrlsmall!=[0]:
            str1=""
            if len(locations_xbrlsmall)%2==0:
                for i in xrange(0,len(locations_xbrlsmall),2):
                    str1=str1+output[locations_xbrlsmall[i]:locations_xbrlsmall[i+1]]
        
############# Remove Teble Sections #########################

        output1=table_clean('<table','</table>',str1)
        
############# Remove Newlines and Carriage Returns #########################

        str1=str1.replace("\r\n"," ")
        p = re.compile(r'<.*?>')
        str1=p.sub("",str1)
        
############# Remove '<a' and '<hr' and <sup Sections #########################        
        
        str1=str1.replace("&nbsp;"," ")
        str1=str1.replace("&NBSP;"," ")
        str1=str1.replace("&LT;","LT")
        str1=str1.replace("&#60;","LT")
        str1=str1.replace("&#160;"," ")
        str1=str1.replace("&AMP;","&")
        str1=str1.replace("&amp;","&")
        str1=str1.replace("&#38;","&")
        str1=str1.replace("&APOS;","'")
        str1=str1.replace("&apos;","'")
        str1=str1.replace("&#39;","'")
        str1=str1.replace('&QUOT;','"')
        str1=str1.replace('&quot;','"')
        str1=str1.replace('&#34;','"')
        str1=str1.replace("\t"," ")
        str1=str1.replace("\v","")
        str1=str1.replace("&#149;"," ")
        str1=str1.replace("&#224;","")
        str1=str1.replace("&#145;","")
        str1=str1.replace("&#146;","")
        str1=str1.replace("&#147;","")
        str1=str1.replace("&#148;","")
        str1=str1.replace("&#151;"," ")
        str1=str1.replace("&#153;","") 
        str1=str1.replace("&#111;","")
        str1=str1.replace("&#153;","")
        str1=str1.replace("&#253;","")
        str1=str1.replace("&#8217;","")
        str1=str1.replace("&#32;"," ")
        str1=str1.replace("&#174;","")
        str1=str1.replace("&#167;","")
        str1=str1.replace("&#169;","")
        str1=str1.replace("&#8220;","")
        str1=str1.replace("&#8221;","")
        str1=str1.replace("&rsquo;","")
        str1=str1.replace("&lsquo;","")
        str1=str1.replace("&sbquo;","")
        str1=str1.replace("&bdquo;","")
        str1=str1.replace("&ldquo;","")
        str1=str1.replace("&rdquo;","")
        str1=str1.replace("\'","")
        p = re.compile(r'&#\d{1,5};')
        str1=p.sub("",str1)
        p = re.compile(r'&#.{1,5};')
        str1=p.sub("",str1)
        str1=str1.replace("_"," ")
        str1=str1.replace("and/or","and or")
        str1=str1.replace("-\n"," ")
        p = re.compile(r'\s*-\s*')
        str1=p.sub(" ",str1)
        p = re.compile(r'(-|=)\s*')
        str1=p.sub(" ",str1)
        p = re.compile(r'\s\s*')
        str1=p.sub(" ",str1)
        p = re.compile(r'(\n\s*){3,}')
        str1=p.sub("\n\n",str1)
        p = re.compile(r'<.*?>')
        str1=p.sub("",str1)

################################## MD&A Section #####################################################

        item7={}
        item7[1]="item 7\. managements discussion and analysis"
        item7[2]="item 7\.managements discussion and analysis"
        item7[3]="item7\. managements discussion and analysis"
        item7[4]="item7\.managements discussion and analysis"
        item7[5]="item 7\. management discussion and analysis"
        item7[6]="item 7\.management discussion and analysis"
        item7[7]="item7\. management discussion and analysis"
        item7[8]="item7\.management discussion and analysis"
        item7[9]="item 7 managements discussion and analysis"
        item7[10]="item 7managements discussion and analysis"
        item7[11]="item7 managements discussion and analysis"
        item7[12]="item7managements discussion and analysis"
        item7[13]="item 7 management discussion and analysis"
        item7[14]="item 7management discussion and analysis"
        item7[15]="item7 management discussion and analysis"
        item7[16]="item7management discussion and analysis"
        item7[17]="item 7: managements discussion and analysis"
        item7[18]="item 7:managements discussion and analysis"
        item7[19]="item7: managements discussion and analysis"
        item7[20]="item7:managements discussion and analysis"
        item7[21]="item 7: management discussion and analysis"
        item7[22]="item 7:management discussion and analysis"
        item7[23]="item7: management discussion and analysis"
        item7[24]="item7:management discussion and analysis"
        
        
        item8={}
        item8[1]="item 8\. financial statements"
        item8[2]="item 8\.financial statements"
        item8[3]="item8\. financial statements"
        item8[4]="item8\.financial statements"
        item8[5]="item 8 financial statements"
        item8[6]="item 8financial statements"
        item8[7]="item8 financial statements"
        item8[8]="item8financial statements"
        item8[9]="item 8a\. financial statements"
        item8[10]="item 8a\.financial statements"
        item8[11]="item8a\. financial statements"
        item8[12]="item8a\.financial statements"
        item8[13]="item 8a financial statements"
        item8[14]="item 8afinancial statements"
        item8[15]="item8a financial statements"
        item8[16]="item8afinancial statements"
        item8[17]="item 8\. consolidated financial statements"
        item8[18]="item 8\.consolidated financial statements"
        item8[19]="item8\. consolidated financial statements"
        item8[20]="item8\.consolidated financial statements"
        item8[21]="item 8 consolidated  financial statements"
        item8[22]="item 8consolidated financial statements"
        item8[23]="item8 consolidated  financial statements"
        item8[24]="item8consolidated financial statements"
        item8[25]="item 8a\. consolidated financial statements"
        item8[26]="item 8a\.consolidated financial statements"
        item8[27]="item8a\. consolidated financial statements"
        item8[28]="item8a\.consolidated financial statements"
        item8[29]="item 8a consolidated financial statements"
        item8[30]="item 8aconsolidated financial statements"
        item8[31]="item8a consolidated financial statements"
        item8[32]="item8aconsolidated financial statements"
        item8[33]="item 8\. audited financial statements"
        item8[34]="item 8\.audited financial statements"
        item8[35]="item8\. audited financial statements"
        item8[36]="item8\.audited financial statements"
        item8[37]="item 8 audited financial statements"
        item8[38]="item 8audited financial statements"
        item8[39]="item8 audited financial statements"
        item8[40]="item8audited financial statements"
        item8[41]="item 8: financial statements"
        item8[42]="item 8:financial statements"
        item8[43]="item8: financial statements"
        item8[44]="item8:financial statements"
        item8[45]="item 8: consolidated financial statements"
        item8[46]="item 8:consolidated financial statements"
        item8[47]="item8: consolidated financial statements"
        item8[48]="item8:consolidated financial statements"
        
        look={" see ", " refer to ", " included in "," contained in "}
        
        a={}
        c={}
       
        lstr1=str1.lower()
        for j in range(1,25):
            a[j]=[]
            for m in re.finditer(item7[j], lstr1):
                if not m:
                    break
                else:
                    substr1=lstr1[m.start()-20:m.start()]
                    if not any(s in substr1 for s in look):   
                        #print substr1
                        b=m.start()
                        a[j].append(b)
        #print i
    
        list1=[]
        for value in a.values():
            for thing1 in value:
                list1.append(thing1)
        list1.sort()
        list1.append(len(lstr1))
        #print list1
               
        for j in range(1,49):
            c[j]=[]
            for m in re.finditer(item8[j], lstr1):
                if not m:
                    break
                else:
                    substr1=lstr1[m.start()-20:m.start()]
                    if not any(s in substr1 for s in look):   
                        #print substr1
                        b=m.start()
                        c[j].append(b)
        list2=[]
        for value in c.values():
            for thing2 in value:
                list2.append(thing2)
        list2.sort()
        
        locations={}
        if list2==[]:
            print ("NO MD&A")
        else:
            if list1==[]:
                print ("NO MD&A")
            else:
                for k0 in range(len(list1)):
                    locations[k0]=[]
                    locations[k0].append(list1[k0])
                for k0 in range(len(locations)):
                    for item in range(len(list2)):
                        if locations[k0][0]<=list2[item]:
                            locations[k0].append(list2[item])
                            break
                    if len(locations[k0])==1:
                        del locations[k0]
        
        if locations=={}:
            with open(LOG,'a') as f:
                f.write(str(FileNUM)+"\t"+"0\n")
                f.close()
        else:
            sections=0
            for k0 in range(len(locations)): 
                substring2=str1[locations[k0][0]:locations[k0][1]]
                substring3=substring2.split()
                if len(substring3)>250:
                    sections=sections+1
                    with open(Filer,'a') as f:
                        f.write("<SECTION>\n")
                        f.write(substring2+"\n")
                        f.write("</SECTION>\n")
                        f.close()
            with open(LOG,'a') as f:
                    f.write(str(FileNUM)+"\t"+str(sections)+"\n")
                    f.close()
        print (FileNUM)
     
        

        
