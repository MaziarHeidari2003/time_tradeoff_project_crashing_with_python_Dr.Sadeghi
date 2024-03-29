#this is the task module
import numpy as np

#print stars
def stars(number):
    for i in range(number):
        print("*", end = "")
    print("")

#error messages
def errorCodeMsg():
    print("Error in input file : CODE ")
    quit()
    

def errorPredMsg():
    print("Error in input file : PREDECESSORS ")
    quit()

def errorDaysMsg():
    print("Error in input file : DAYS ")
    quit()

# Scans if the code in predecessors and successors are
# in the list of task codes:
def getTaskCode(mydata, code):
    x = 0
    flag = 0
    for i in mydata['CODE']:
        if(i == code):
            flag = 1
            break
        
        x+=1
    
    if(flag == 1):
        return x
    else:
        errorCodeMsg()



# Critical Path Method Forward Pass Function
# EF -> Earliest Finish
# ES -> Earliest Start

def forwardPass(mydata):
    ntask = mydata.shape[0]
    ES = np.zeros(ntask, dtype = np.int8)
    EF = np.zeros(ntask, dtype = np.int8)
    temp = [] #hold temporary codes
        
    for i in range(ntask):
        if(mydata['PREDECESSORS'][i] == None):
            ES[i] = 0
            try:
                EF[i] = ES[i] + mydata['DAYS'][i]
            except:
                errorDaysMsg()
        
        else:
            if i == 0  :
                continue
            for j in mydata['PREDECESSORS'][i]:
                index = getTaskCode(mydata,j)
                temp.append(EF[index])
                #Check the video for the missing line here
                
                if(index == i):
                    errorPredMsg()
                else:
                    temp.append(EF[index])

            ES[i] = max(temp)
            try:
                EF[i] = ES[i] + mydata['DAYS'][i]
            except:
                errorDaysMsg()

        #reset temp
        temp = []


    #Update dataFrame:
    mydata['ES'] = ES
    mydata['EF'] = EF
    
    return mydata


# Critical Path Method Backward Pass function
# LS -> Latest Start
# LF -> Latest Finish

def backwardPass(mydata):
    ntask = mydata.shape[0]
    temp = []
    LS = np.zeros(ntask, dtype = np.int8)
    LF = np.zeros(ntask, dtype = np.int8)
    SUCCESSORS = np.empty(ntask, dtype = object)

    #create successor column:
    
    for i in range(ntask-1, -1,-1):
        if i==0 :
            continue
        if(mydata['PREDECESSORS'][i] != None):
            for j in mydata['PREDECESSORS'][i]:
                index = getTaskCode(mydata,j)
                if(SUCCESSORS[index] != None):
                    SUCCESSORS[index] += mydata['CODE'][i]
                else:
                    SUCCESSORS[index] = mydata['CODE'][i]

    #incorporate the column to the data frame:

    mydata["SUCCESSORS"] = SUCCESSORS


    #compute for  EF and LS:

    for i in range(ntask-1, -1, -1):
        if i==0 :
            continue
        if(mydata['SUCCESSORS'][i] == None):
            LF[i] = np.max(mydata['EF'])
            LS[i] = LF[i] - mydata['DAYS'][i]
        else:
            for j in mydata['SUCCESSORS'][i]:
                index = getTaskCode(mydata,j)
                temp.append(LS[index])

            LF[i] = min(temp)
            LS[i] = LF[i] - mydata['DAYS'][i]

            #reset temp list:
            temp = []


    #incorporate LF and LS to data frame :

    mydata['LS'] = LS
    mydata['LF'] = LF

    return mydata

#compute for SLACK and CRITICAL state
def slack(mydata):
    ntask = mydata.shape[0]
    
    SLACK = np.zeros(shape = ntask, dtype = np.int8)
    CRITICAL = np.empty(shape = ntask,dtype = object)

    for i in range(ntask):
        SLACK[i] = mydata['LS'][i] - mydata['ES'][i]
        if(SLACK[i] == 0):
            CRITICAL[i] = "YES"
        else:
            CRITICAL[i] = "NO"

    #incorporate SLACK and CRITICAL to data frame

    mydata['CRITICAL'] = CRITICAL


    #slope = np.zeros(shape = ntask, dtype = np.int8)
    #for i in range(ntask):
            
            #a = mydata['DC_COST'][i]
           # b = mydata['D_COST'][i]
           # c = mydata['DAYS'][i]
           # d= mydata['CRASH_DAYS'][i]
           # slope[i] = a
    #mydata['SLOPE'] = slope


    #re arrange columns in dataframe:
    mydata = mydata.reindex(columns = ['DESCR', 'CODE','ES','EF','LS','LF','CRITICAL','SUCCESSORS','PREDECESSORS','DAYS','CRASH_DAYS','D_COST','DC_COST','SLOPE','duration','final_cost','start_time','finish_time'])

    slope = np.zeros(shape = ntask, dtype = np.int16)
    for i in range(ntask):

            a = mydata['DC_COST'][i]
            b = mydata['D_COST'][i]
            c = mydata['DAYS'][i]
            d= mydata['CRASH_DAYS'][i]
            try:
                slope[i] = (a-b)/(c-d)
            except:
                slope[i]=0    
    mydata['SLOPE'] = slope
    
    return mydata

#wrapper function:

def computeCPM(mydata):
    mydata = forwardPass(mydata)
    mydata = backwardPass(mydata)
    mydata = slack(mydata)
    return mydata

#print function

def printTask(mydata):
    print("CRITICAL PATH METHOD CALCULATOR")
    stars(90)
    print("ES = Earliest Start; EF = Earliest Finish; LS = Latest Start, LF = Latest Finish")
    stars(90)
    print(mydata)
    stars(90)




        