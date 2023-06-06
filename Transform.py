import pandas as pd
import os
import time
import multiprocessing

src_dir = 'D:\Python\Transformation\output.csv'
trns_dir = 'D:\Python\Transformation\Transformation_Logic.xlsx'

src_df = pd.read_csv(src_dir)
trns_df = pd.read_excel(trns_dir)

def incoming_Check(logic_string):
    print("----incoming_Check----")
    logic_dict = []
    iflogic_dic = {}
    if logic_string != "None":
        logic_dict = [item.split("=") for item in logic_string.split("|")]
        print(logic_dict)
    for i in logic_dict:
        if "Error" in i[0]:
            print("Error Logic Executing"),
            print(i[1])
            #print(logic_dict.get("Error"))
        if "query" in i[0]:
            print("query Logic Executing")
            print(i[1])
            #print(logic_dict.get("query"))
        if "cal" in i[0]:
            print("cal Logic Executing")
            print(i[1])
            #print(logic_dict.get("cal"))
        if "condition" in i[0]:
            print("condition Logic Executing")
            print(i[1])
            #print(logic_dict.get("condition"))
        if "if" in i[0]:
            a = 5
            b = 2
            c = 6
            print("if condition")
            ifstring = logic_dict.get("if")
            # print(ifstring)
            iflist = ifstring.split(',')
            # print(iflist)
            for i in iflist:
                ifcon, thencon, elsecon = i.split('-')

                if eval(ifcon):
                    eval(thencon)
                else:
                    eval(elsecon)



def TRF_Check(logic_string):
    print("----TRF_Check----")
    logic_dict = {}
    if logic_string != "None":
        logic_dict = dict(item.split("=") for item in logic_string.split("|"))
    if "Error" in logic_dict.keys():
        print("Error Logic Executing")
        print(logic_dict.get("Error"))
    if "query" in logic_dict.keys():
        print("query Logic Executing")
        print(logic_dict.get("query"))

def MSTR_Check(logic_string):
    print("----MSTR_Check----")
    logic_dict = {}
    if logic_string != "None":
        logic_dict = dict(item.split("=") for item in logic_string.split("|"))
    if "Error" in logic_dict.keys():
        print("Error Logic Executing")
        print(logic_dict.get("Error"))
    if "query" in logic_dict.keys():
        print("query Logic Executing")
        print(logic_dict.get("query"))

def Calculation(logic_string):
    print("---Calculation---")
    logic_dict = {}
    if logic_string != "None":
        logic_dict = dict(item.split("=") for item in logic_string.split("|"))
    if "Error" in logic_dict.keys():
        print("Error Logic Executing")
        print(logic_dict.get("Error"))
    if "query" in logic_dict.keys():
        print("query Logic Executing")
        print(logic_dict.get("query"))

def Load():
    print("load")
def incoming_Check2(logic_string):
    print("----incoming_Check----")
    logic_dict = []
    iflogic_dic = {}
    if logic_string != "None":
        logic_dict = [item.split("=") for item in logic_string.split("|")]
        print(logic_dict)
    for i in logic_dict:
        if "Error" in i[0]:
            print("Error Logic Executing"),
            print(i[1])
            #print(logic_dict.get("Error"))
        if "query" in i[0]:
            print("query Logic Executing")
            print(i[1])
            #print(logic_dict.get("query"))
        if "cal" in i[0]:
            print("cal Logic Executing")
            print(i[1])
            #print(logic_dict.get("cal"))
        if "condition" in i[0]:
            print("condition Logic Executing")
            print(i[1])
            #print(logic_dict.get("condition"))
        if "if" in i[0]:
            a = 5
            b = 2
            c = 6
            print("if condition")
            ifstring = logic_dict.get("if")
            # print(ifstring)
            iflist = ifstring.split(',')
            # print(iflist)
            for i in iflist:
                ifcon, thencon, elsecon = i.split('-')

                if eval(ifcon):
                    eval(thencon)
                else:
                    eval(elsecon)



def TRF_Check2(logic_string):
    print("----TRF_Check----")
    logic_dict = {}
    if logic_string != "None":
        logic_dict = dict(item.split("=") for item in logic_string.split("|"))
    if "Error" in logic_dict.keys():
        print("Error Logic Executing")
        print(logic_dict.get("Error"))
    if "query" in logic_dict.keys():
        print("query Logic Executing")
        print(logic_dict.get("query"))

def MSTR_Check2(logic_string):
    print("----MSTR_Check----")
    logic_dict = {}
    if logic_string != "None":
        logic_dict = dict(item.split("=") for item in logic_string.split("|"))
    if "Error" in logic_dict.keys():
        print("Error Logic Executing")
        print(logic_dict.get("Error"))
    if "query" in logic_dict.keys():
        print("query Logic Executing")
        print(logic_dict.get("query"))

def Calculation2(logic_string):
    print("---Calculation---")
    logic_dict = {}
    if logic_string != "None":
        logic_dict = dict(item.split("=") for item in logic_string.split("|"))
    if "Error" in logic_dict.keys():
        print("Error Logic Executing")
        print(logic_dict.get("Error"))
    if "query" in logic_dict.keys():
        print("query Logic Executing")
        print(logic_dict.get("query"))

trns_dict = trns_df.to_dict('records')
trns_dict2 = trns_df.to_dict('records')
def main1():

    # for index,row in trns_df.iterrows():
    for row in trns_dict:

        if row["incoming_Check"] != "None":
            incoming_Check(row["incoming_Check"])

        if row["TRF_Check"] != "None":
            TRF_Check(row["TRF_Check"])

        if row["MSTR_Check"] != "None":
            MSTR_Check(row["MSTR_Check"])

def main2():

    # for index,row in trns_df.iterrows():
    for row in trns_dict2:

        if row["incoming_Check"] != "None":
            incoming_Check2(row["incoming_Check"])

        if row["TRF_Check"] != "None":
            TRF_Check2(row["TRF_Check"])

        if row["MSTR_Check"] != "None":
            MSTR_Check2(row["MSTR_Check"])



'''starttime = time.time()
main1()
main2()
endtime = time.time()

print("exe time : ", (endtime - starttime))'''

def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')

if __name__ == "__main__":

    start_time = time.perf_counter()

    # Creates two processes
    p1 = multiprocessing.Process(target=sleepy_man)
    p2 = multiprocessing.Process(target=sleepy_man)
    p3 = multiprocessing.Process(target=sleepy_man)
    # Starts both processes
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    finish_time = time.perf_counter()
    starttime = time.time()
    main1()
    main2()
    endtime = time.time()

    print("exe time : ", (endtime - starttime))



    print(f"Program finished in {finish_time - start_time} seconds")






