import re
import operator
import csv

def errorstats(lines):
    '''this function will create a dictionary with errors and their counts'''
    error_message = {}
    for line in lines:
        line = line.strip()
        if re.search('ERROR (.*) ',line):
            msgval = (re.search('ERROR (.*) ',line)).group(1)
            #print(msgval)
            error_message[msgval] = error_message.get(msgval,0) + 1

    return error_message

def userstats(lines):
    '''this function will create a userstats by scanning the users and number of times error and info messages for that user. Dictionary key is user and dictionary value is tuple with error and info counts'''
    user_error = {}
    user_info = {}
    user_list = []
    user_stats = {}
    for line in lines:
        line = line.strip()
        theuser = ""
        if re.search('ERROR.*',line):
            theuser = re.search('.*\((.*)\)',line).group(1)
            user_error[theuser] = user_error.get(theuser,0) + 1
        else:
            theuser = re.search('.*\((.*)\)',line).group(1)
            user_info[theuser] = user_info.get(theuser,0) + 1
        
        if theuser not in user_list:
            user_list.append(theuser)

    for eachuser in user_list:
        if eachuser not in user_error:
            user_error[eachuser] = 0
        if eachuser not in user_info:
            user_info[eachuser] = 0
        user_stats[eachuser] = (user_info[eachuser], user_error[eachuser])

    return user_stats

if __name__ == '__main__':
    
    with open('logfile.txt','r',encoding='utf-8') as logfile:
        lines  = logfile.readlines()
        print("")
        #print(errorstats(lines))
        print("")
        sorted_error_stats = sorted(errorstats(lines).items(), key=operator.itemgetter(1), reverse=True)
        #print(sorted_error_stats)
        print("")

        sorted_users = sorted(userstats(lines).items(),key=operator.itemgetter(0))

        #print(sorted_users)
        '''creating two arrays from the results to create csv files'''
        userrows = []
        errorstats = []

        for item in sorted_users:
            userrows.append([item[0],item[1][0],item[1][1]])

        print(userrows)
        print(sorted_error_stats)

        for item in sorted_error_stats:
            errorstats.append([item[0],item[1]])

        print("")
        print(errorstats)

        userheader = ['Username','INFO','ERROR']
        errorheader = ['Error','Count']

  #creating actual csv files
  
        with open('user_statistics.csv', 'w', encoding='UTF8', newline='\n') as userfile:
                     writer = csv.writer(userfile)
                     writer.writerow(userheader) #Note "writerow" instead of "writerows"
                     writer.writerows(userrows)
        with open('error_message.csv','w', encoding='UTF8', newline='\n') as errorfile:
                    writer = csv.writer(errorfile)
                    writer.writerow(errorheader) #Note "writerow" instead of "writerows"
                    writer.writerows(errorstats)


