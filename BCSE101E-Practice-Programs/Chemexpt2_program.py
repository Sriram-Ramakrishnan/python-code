import math
from mysql_csv_fns import *
    
class rate_analysis:
    volume_default = 26.7
    def __init__(self,volume,t):
        self.volume  = volume
        self.t = t
        self.log_val = round(math.log(volume,10),3)
    def rate(self):
        log_val_0 = round(math.log(rate_analysis.volume_default,10),4)
        rate = (2.303/self.t)*(log_val_0 - self.log_val)
        rate = round(rate,6)
        return [str(self.t),str(self.volume),str(self.log_val),str(rate)]

def expt2():   
    list_of_values =[]
    colnames =["time","volume","log value","rate"]
    for i in range(6):
        t = (i+1)*10
        volume = float(input("Enter Volume for time t = "+str(t)+":"))
        reading = rate_analysis(volume,t)
        list_of_values.append(reading.rate())
    MySQL_display(list_of_values,colnames)


def expt5():
    list1,list2 = [],[]
    n1 = int(input("No of rows for table 1"))
    for i in range(n1):
        ml = float(input("mL"))
        volt = float(input("Volt:"))
        list1.append([ml,volt])
    list2 =[[3.5,0.360],
            [3.7,0.363],
            [3.9,0.383],
            [4.1,0.387],
            [4.3,0.457],
            [4.5,0.816],
            [4.7,0.823],
            [4.9,0.837],
            [5.1,0.845],
            [5.3,0.856]]
    colnames = ["mL","Volt","ΔE","ΔV","ΔE/ΔV","Avg ml"]

    for i in list2:
        traverse = list2.index(i)
        if traverse == len(list2)-1:
            upperlimE,upperlimV = list1[6][1],list1[6][0]
            lowerlimE,lowerlimV = i[1],i[0]
            deltaE = round(upperlimE - lowerlimE,3)
            deltaV = round(upperlimV - lowerlimV,1)
            i.append(deltaE)
            i.append(deltaV)
            i.append(round((deltaE/deltaV),3))
            i.append(round((upperlimV+lowerlimV)/2,1))
            
        else:
            upperlimE,upperlimV = list2[traverse+1][1],list2[traverse+1][0]
            lowerlimE,lowerlimV = i[1],i[0]
            deltaE = round(upperlimE - lowerlimE,3)
            deltaV = round(upperlimV - lowerlimV,1)
            i.append(deltaE)
            i.append(deltaV)
            i.append(round((deltaE/deltaV),3))
            i.append(round((upperlimV+lowerlimV)/2,1))
        print("ΔE = %0.3f - %0.3f = %0.3f"%(upperlimE,lowerlimE,deltaE))
        print("ΔV = %0.1f - %f = %0.1f"%(upperlimV,lowerlimV,deltaV))
        print("ΔE/ΔV = %0.3f"%(deltaE/deltaV))
        print()
    MySQL_display(list2,colnames)

def expt4():
    n = int(input("No of rows for table 1"))
    for i in range(n):
        val1 = float(input("TH: "))
        val2 = float(input("PR: "))
        ans = abs(val1-val2)
        final = ans/val1
        print(final)
        print(round(final*100,3))

def expt7():
    k = float(input("K: "))
    lambda_wvelgth = float(input("K: "))
    Exp_table = []
    thetas = []
    fwhms = []
    csizes = []
    for i in range(5):
        theta = float(input("Theta: "))
        fwhm = float(input("FWHM: "))
        thetas.append(theta)
        fwhms.append(fwhm)
    print("Experiment Table:")
    for i in range(5):
        row = []
        row.append(i+1)
        theta = round(thetas[i]/2,2)
        row.append(thetas[i])
        row.append(theta)
        fwhm = round(fwhms[i],2)
        row.append(fwhm)
        cosO = round(math.cos(math.radians(round(theta,2))),2)
        c_size = round(((k*lambda_wvelgth)/(cosO*fwhm)),3)
        row.append(c_size)
        Exp_table.append(row)
    MySQL_display(Exp_table,['S.No','2θ','θ','FWHM','Crystallite size'])
    sum = 0
    print("Calculations:")
    for i in range(5):
        print(str(Exp_table[i][0])+".",end = ' ')
        theta2,theta = Exp_table[i][1],Exp_table[i][2]
        print("Now, 2θ = %.2f , ∴ θ = %.2f"%(theta2,theta))
        print("Full width at half maximum(FWHM) = %.2f"%Exp_table[i][3])
        cosO = round(math.cos(math.radians(round(theta,2))),2)
        print("""∴ Crystallite size:
            (k)(λ)       (%.2f)(%.2f)
    c =  ------------ = ---------------
        (cosθ)(fwhm)    (%.2f)(%.2f) """%(k,lambda_wvelgth,cosO,Exp_table[i][3]))     
        print(" c = %.3f"%Exp_table[i][4])
        print()
        sum+=Exp_table[i][4]
    print(sum)
    print(round(sum/5,3))

def expt1():
    pass
# Inputs: Con

expt5()

