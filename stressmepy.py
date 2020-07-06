import threading,datetime
import requests


class StressTest():
    def __init__(self,url,total_requests,options=None,detailed=False):
        self.url = url
        self.total = total_requests
        self.lowest=10000000
        self.highest=0
        self.average=0
        self.connected=0
        self.refused=0
        self.success=0
        self.failed=0
        self.codes=[]
        self.codes_map={}
        self.total_time=0
        self.treads=[]
        self.times=[]
        self.options=options
        self.detailed=detailed
        self.txt_log=""
    
    def run(self):
        for i in range(self.total):
            self.times.append(0)
            self.codes.append(0)
            thread = self.HookThread(i,self,self.total,self.url,self.options)
            self.treads.append(thread)

        for i in range(self.total):
            self.treads[i].start()

        for i in range(self.total):
            self.treads[i].join()
    
    def results(self):
        results= {
            "url":self.url,
            "total_requests":self.total,
            "total_time":self.total_time,
            "time_stat":{
                "highest":self.highest,
                "lowest":self.lowest,
                "average":self.average
            },
            "performance_stat":{
                "success":self.success,
                "failed":self.failed,
                "connected":self.connected,
                "refused":self.refused
            },
            "code_map":self.codes_map
        }
        if self.detailed:
            results["time_log"]=self.times
            results["code_log"]=self.codes
        return results

 

    def log(self,id,count,text):
        self.txt_log+="[*][T"+str(id)+"]\t\t"+text+"\n"

    def logTime(self,id,time,connected,success,code):
        if time<self.lowest:
            self.lowest=time
        if time>self.highest:
            self.highest=time
        self.total_time+=time
        self.average=self.total_time/self.total
        self.times[id]=time
        if connected:
            self.connected+=1
        else:
            self.refused+=1
        if success:
            self.success+=1
        else:
            self.failed=0
        self.codes[id]=code
        if code in self.codes_map:
            self.codes_map[code]+=1
        else:
            self.codes_map[code]=1
      

    def requestUrl(self,url,options):
        #init
        body=None
        headers={"User-Agent":"stessmepy"}
        method="GET"
        
        #valid
        valid_methods=["GET","POST","PUT","DELETE"]

        #Validate
        if options!=None:
            if "method" in options and options["method"] in valid_methods:
                method=options["method"]
            if "body" in options and isinstance(options["body"],dict):
                for key in options["body"]:
                    if isinstance(key,str) and isinstance(options["body"][key],str):
                        body[key]=options["body"][key]
            if "headers" in options and isinstance(options["headers"],dict):
                for key in options["headers"]:
                    if isinstance(key,str) and isinstance(options["headers"][key],str):
                        headers[key]=options["headers"][key]
        #init results
        connected=True
        success=True
        code=0
        #try to perform
        try:
            if method=="POST":
                r=requests.post(url,json=body,headers=headers)
            if method=="PUT":
                r=requests.put(url,json=body,headers=headers)
            if method=="DELETE":
                r=requests.delete(url,json=body,headers=headers)
            if method=="GET":
                r=requests.get(url,json=body,headers=headers)
            success=(r.status_code<400)
            code=r.status_code
        except:
            connected=False
            success=False
        #return
        return connected,success,code

    class HookThread (threading.Thread):
        def __init__(self,id,parent,count, url,options):
            threading.Thread.__init__(self)
            self.url = url
            self.id = id
            self.options = options
            self.parent = parent
            self.count = count

        def run(self):
            self.parent.log(self.id,self.count,"Started...")
            self.parent.log(self.id,self.count,"Requesting"+" "+self.url)
            datetime_start= datetime.datetime.now()
            connected,success,code=self.parent.requestUrl(self.url,self.options)
            datetime_end= datetime.datetime.now()
            self.parent.log(self.id,self.count,"Request ended with status"+" "+str(code))
            self.parent.log(self.id,self.count,"Elapsed"+" "+str((datetime_end-datetime_start).total_seconds())+" "+"seconds")
            self.parent.log(self.id,self.count,"Ended.")
            self.parent.logTime(self.id,(datetime_end-datetime_start).total_seconds(),connected,success,code)


 