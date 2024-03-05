


from subprocess import Popen, PIPE
from os import dup
from os import write
import random
import sys
import subprocess
from subprocess import *
import copy
import os


def perform_DCJ(lst, adj1, adj2, sub_position1, sub_position2):
    #creating resulting genome
    evolved_list = []

    #the sub_pos with higher index gets set to sub_position2 just to maintain convention throughout the code
    if sub_position1>=sub_position2:
      sub_pos1=sub_position2
      sub_list1=lst[sub_position2]
      sub_pos2=sub_position1
      sub_list2=lst[sub_position1]
      if sub_pos1==sub_pos2:
          if adj1>adj2:
             adj_1=adj2
             adj_2=adj1
          else:
            adj_1=adj1
            adj_2=adj2
      else:
          sub_pos1=sub_position2
          adj_1=adj2
          sub_pos2=sub_position1
          adj_2=adj1
          sub_list1=lst[sub_pos1]
          sub_list2=lst[sub_pos2]
    else:
      sub_pos2=sub_position2
      sub_list2=lst[sub_pos2]
      sub_pos1=sub_position1
      sub_list1=lst[sub_pos1]
      adj_1=adj1
      adj_2=adj2



    option=[1,2]
    DCJ_option=random.choices(option)
    evolved_sublist=[]

    if DCJ_option==[1]:
       print("DCJ OPTION 1 IS PICKED")
       evolved_list=DCJ_option_1(sub_pos1, sub_pos2, adj_1, adj_2, lst, evolved_sublist, sub_list1, sub_list2)
    else:
       evolved_list=DCJ_option_2(sub_pos1, sub_pos2, adj_1, adj_2, lst, evolved_sublist, sub_list1, sub_list2)
       print("DCJ OPTION 2 IS PICKED")


    return evolved_list




#the first option: both adj in diff linear chromosomes
def  DCJ_option_1(sub_pos1, sub_pos2, adj1, adj2, lst, evolved_sublist, sub_list1, sub_list2):



    #this is where things will change depending on the type of our adj
    #there are two main groups: both adj in same chromosome vs both adj in diff chromosme
    #1st option: both adj in diff chromosomes
    if not sub_pos1==sub_pos2:

        #if there are diff chromosomes, we have 3 groups: 1. both adj linear, 2. one adj linear, 3. no adj linear

        #1st option: both adj linear: both sublist contain 0
        if (0 in sub_list1 and 0 in sub_list2):

            #append everything left of the 1st adj (L1)
            for i in sub_list1[:adj1+1]:
                evolved_sublist.append(i)
            #appeding things present in the right of sub_list2 within same chromosom
            for i in sub_list2[adj2+1:]:
                  evolved_sublist.append(i)

            #replacing with the first sub_list
            lst[sub_pos1]=evolved_sublist
            #emptying the sublist
            evolved_sublist=[]


            #append everything left of adj2 including it
            for i in sub_list2[:adj2+1]:
                evolved_sublist.append(i)
               
            #append everything right of adj1
            for i in sub_list1[adj1+1:]:
                  evolved_sublist.append(i)

            #replacing with the second sub_list
            lst[sub_pos2]=evolved_sublist

        #either adj is not linear
        else:

            if 0 in sub_list1 or 0 in sub_list2:
                if 0 in sub_list1:
                  linear_sublist=sub_list1
                  circular_sublist=sub_list2
                else:
                  linear_sublist=sub_list2
                  circular_sublist=sub_list1

                #append everything left of the 1st adj
                for i in linear_sublist[:adj1+1]:
                  evolved_sublist.append(i)
                
                #appeding things present in the right of sub_list2 within same chromosome
                for i in circular_sublist[adj2+1:]:
                    evolved_sublist.append(i)
                
                #appending everything left of circular chromosome
                for i in circular_sublist[:adj2+1]:
                    evolved_sublist.append(i)
                
                #appending everything right of adj1
                for i in linear_sublist[adj1+1:]:
                  evolved_sublist.append(i)





            #if no adj is linear, we get a resulting new linear chromosme so appending 0 to the sublist
            else:
                #append everything left of the 1st adj
                if not (adj1==len(sub_list1)-1):
                  for i in sub_list1[:adj1+1]:
                    evolved_sublist.append(i)
                else:
                  for i in sub_list1:
                    evolved_sublist.append(i)

                #appeding things present in the left of sub_list2 within same chromosome
                if not (adj2==len(sub_list2)-1):
                  for i in sub_list2[adj2+1:]:
                    evolved_sublist.append(i)
                if not (adj2==len(sub_list2)-1):
                  for i in sub_list2[:adj2+1]:
                    evolved_sublist.append(i)
                else:
                  for i in sub_list2:
                    evolved_sublist.append(i)
                if not (adj1==len(sub_list1)-1):
                  for i in sub_list1[adj1+1:]:
                    evolved_sublist.append(i)


            #replace the sublist to the main list
            lst[sub_pos1]=evolved_sublist
	    
            if not sub_pos2==len(lst)-1:
               lst=lst[:sub_pos2]+lst[sub_pos2+1:]

            else:
               lst=lst[:sub_pos2]



    #both adj in the same chromosomes
    else:
          #if both adj in the same linear chromsome:
          if 0 in sub_list1:
            #append everything left of the 1st adj
            for i in sub_list1[:adj1+1]:
                  evolved_sublist.append(i)
            #appeding things present in the left of sub_list1 within same chromosome
            for i in sub_list1[adj2+1:]:
              evolved_sublist.append(i)

            lst[sub_pos1]=evolved_sublist
            evolved_sublist=[]

            for i in sub_list1[adj1+1:adj2+1]:
                  evolved_sublist.append(i)
               




          else:
            #both adj in the same circular chromosomes
            #append everything left of the 1st adj
            if not (adj1==len(sub_list1)-1):
              for i in sub_list1[:adj1+1]:
                evolved_sublist.append(i)
            else:
              for i in sub_list1:
                evolved_sublist.append(i)
               
            
            #appeding things present in the right of adj2 within same chromosome excluding it
            #if adj2 is not the last element, only then append
            if not (adj2==len(sub_list1)-1):
              for i in sub_list1[adj2+1:]:
                  evolved_sublist.append(i)

            #append the sublist to the main list
            lst[sub_pos1]=evolved_sublist

            #empty the sublist so that we can create a second sublist with another circular chromosome
            evolved_sublist=[]

            #if adj2 is not the last element
            if not (adj2==len(sub_list1)-1):
              for i in sub_list1[adj1+1:adj2+1]:
                  evolved_sublist.append(i)
            else:
               for i in sub_list1[adj1+1:]:
                  evolved_sublist.append(i)



          #add the circular chromosome to the main list
          lst.append(evolved_sublist)




    return lst






#the first option: both adj in diff linear chromosomes
def  DCJ_option_2(sub_pos1, sub_pos2, adj1, adj2, lst,evolved_sublist, sub_list1, sub_list2):

      #this is where things will change depending on the type of our adj
      #there are two main groups: both adj in same chromosome vs both adj in diff chromosme
      #1st option: both adj in diff chromosomes
      if not sub_pos1==sub_pos2:


             #if there are diff chromosomes, we have 3 groups: 1. both adj linear, 2. one adj linear, 3. no adj linear
             #1st option: both adj linear: both sublist contain 0
             #formula: [0,L1+-L2(inverted,0)][0,-R2+R1,0]
             if (0 in sub_list1 and 0 in sub_list2):

                 #append everything left of the 1st adj including ad1 in the same chromosome including T
                 for i in sub_list1[:adj1+1]:
                    evolved_sublist.append(i)

                 #appending everything of the left of ad2 including it and everything inverted(-) and end->beg
                 for i in reversed(sub_list2[:adj2+1]):
                         evolved_sublist.append(-i)

                 lst[sub_pos1]=evolved_sublist

                 #another sublist
                 evolved_sublist=[]

                 #append everything right of ad1 excluding adj1 and including T as it is
                 for i in reversed(sub_list2[adj2+1:]):
                     evolved_sublist.append(-i)

                 for i in sub_list1[adj1+1:]:
                     evolved_sublist.append(i)

                 #append the sublist to the main list
                 lst[sub_pos2]=evolved_sublist


            #either adj is not linear
             else:
                if 0 in sub_list1 or 0 in sub_list2:
                    if 0 in sub_list1:
                      linear_sublist=sub_list1
                      circular_sublist=sub_list2
                    else:
                      linear_sublist=sub_list2
                      circular_sublist=sub_list1

                    #append everything left of the 1st adj including ad1 in the same chromosome including T
                    for i in linear_sublist[:adj1+1]:
                       evolved_sublist.append(i)

                    #append everything right of the 2nd adj exluding adj2 and T, inverted(-) and end->begining(reversed)
                    for i in reversed(circular_sublist[:adj2+1]):
                          evolved_sublist.append(-i)
                       

                    #appeding things present in the right of adj1 excluding adj1, including T, within same chromosome
                    for i in reversed(circular_sublist[adj2+1:]):
                        evolved_sublist.append(-i)

                    for i in linear_sublist[adj1+1:]:
                        evolved_sublist.append(i)

                    #add sublist to the main list
                    lst[sub_pos1]=evolved_sublist



                else:
                   #both chromosomes are circular
                   #formula:[L1+|-L2|+|-R2|+R1]
                   #one merged chromosome

                  if not (adj1==len(sub_list1)-1):
                   for i in sub_list1[:adj1+1]:
                      evolved_sublist.append(i)
                  else:
                   for i in sub_list1:
                      evolved_sublist.append(i)
                   

                   #appending everything of the left of ad2 including it and everything inverted(-) and end->beg
                  if not (adj2==len(sub_list2)-1):
                     for i in reversed(sub_list2[:adj2+1]):
                       evolved_sublist.append(-i)
                  else:
                     for i in reversed(sub_list2):
                       evolved_sublist.append(-i)
                     


                  #append everything right of ad1 excluding adj1 and including T as it is
                  if not (adj2==len(sub_list2)-1):
                    for i in reversed(sub_list2[adj2+1:]):
                      evolved_sublist.append(-i)

                  for i in sub_list1[adj1+1:]:
                      evolved_sublist.append(i)

                  #append the sublist to the main list
                  lst[sub_pos1]=evolved_sublist


                
                
                #remove the second sublist
                if not sub_pos2==len(lst)-1:
                    lst=lst[:sub_pos2]+lst[sub_pos2+1:]
                else:
                     lst=lst[:sub_pos2]






      #if both adj in the same chromosome: circular or linear
      else:
            #append everything left of the 1st adj including it and T as it is
            for i in sub_list1[:adj1+1]:
                evolved_sublist.append(i)

            #code will change here based on linear or circular chromosome

            #if linear: formula=[0+L1+|-L2|+R2+0]
            if 0 in sub_list1:
                #appeding things present in the left of adj2 including itself but untill u encounter adj1, all should be inverted(-) and end->beg within same chromosome
                for i in reversed(sub_list1[adj1+1:adj2+1]):
                     evolved_sublist.append(-i)

                #append everything right of the adj2 excluding it
                for i in sub_list1[adj2+1:]:
                      evolved_sublist.append(i)

                #add sublist to the main list
                lst[sub_pos1]=evolved_sublist

            else:
               #if circular: formula: [L1+|-L2|+R2] #### I changed adj2 to adj2+1
               if not (adj2==len(sub_list1)-1):
                 for i in reversed(sub_list1[adj1+1:adj2+1]):
                   evolved_sublist.append(-i)
               else:
                 for i in reversed(sub_list1[adj1+1:]):
                   evolved_sublist.append(-i)
              
               if  not (adj2==len(sub_list1)-1): 
                 for i in sub_list1[adj2+1:]:
                   evolved_sublist.append(i)

               lst[sub_pos1]=evolved_sublist




      return lst






def perform_deletion(lst, all_gene, sub_pos, adj, length):


    #creatign a new sublist
    evolved_sublist=[]

    #getting the sublist
    sub_list=lst[sub_pos]

    #append everything before and not including adj
    if 0 in sub_list:
        if adj==0:   
          for i in sub_list[:adj+1]:
            evolved_sublist.append(i)
        else:
          for i in sub_list[:adj]:
            evolved_sublist.append(i)

        if adj==0:
           #append everything after the deleted genes
           for i in sub_list[adj + length+1:len(sub_list)+1]:
               evolved_sublist.append(i)
        else:
           for i in sub_list[adj + length:len(sub_list)+1]:
               evolved_sublist.append(i)

    else:
        if adj==0:
          for i in sub_list[adj+length:]:
            evolved_sublist.append(i)
        else:
          for i in sub_list[:adj]:
            evolved_sublist.append(i)
          for i in sub_list[adj+length:]:
            evolved_sublist.append(i)
     

    #replace the modified sublist
    lst[sub_pos]=evolved_sublist

    return lst






def perform_insertion(lst, all_gene,sub_pos, adj, length):

    #creating a new sub_list
    evolved_sublist=[]

    #find the largest absolute value in the list
    largest_abs = max(all_gene, key=abs)
    print("largest abs: " + str(largest_abs))

    #getting the sublist
    sublist=lst[sub_pos]

    #performing insertion:
    
    #if largest number was negative
    if largest_abs<0:
       largest=largest_abs*-1
    else:
       largest=largest_abs
    
    #append new genes based on the number of length chosen after adj
    #converting length to int
    final_length=int(length)###### changed length[0] to length

    #if the list to be inserted is an empty circular chromosome, the adj1 passed on from main function will be -5
    if adj==-5:
       for i in range(1, final_length+1):
             evolved_sublist.append(int(largest)+int(i))
    #list is non_empty linear, circular or empty linear list
    else:

       #append everything in the sublist from begining to adj
       for i in sublist[:adj+1]:
           evolved_sublist.append(i)
    

       for i in range(1,final_length+1):
           evolved_sublist.append(int(largest)+int(i))
    
       #append whatever is left
       for i in sublist[adj+1:]:
           evolved_sublist.append(i)

    
    #replace the changed sublist
    lst[sub_pos]=evolved_sublist


    return lst




def write_file_dup(evolved_list,i, file_name):

  if i==0 or i==1:
     access_type='w'
  else:
    access_type='a'

  print("this is i:  " + str(i))

  with open(file_name, access_type) as file:
     file.write(">")
     file.write(str(i))
     file.write("\n")
     for i in evolved_list:
         #print(i)
         for j in i:
            #print(j)
            if j=='[' or j==']' or j==0:
              pass
            else:
              file.write(str(j)+ " ")

         if 0 in i:
          file.write("|")
         else:
          file.write(")")

     file.write('\n')
     if file_name=="original_genome.txt":
        file.write(">1")





#picking 2 adj for DCJ and insertion duplication and 1 for insertion and deletion
def pick_adj(list, weights_sublist, length, operation): ######changed chosen_length to length

  #pick a sublist
  sub_list1=[]


  while len(sub_list1)==0:
    sub_list1=random.choices(list, weights=weights_sublist, k=1)[0]
    print("inside the adj function")
    
    #find the index of sub_list
    sub_pos1=list.index(sub_list1)

  adj1=-5
  #pick an adj:
  #if linear, can't pick the last 0
  if 0 in sub_list1:
    adj1=-5
    if not len(sub_list1)==0:
       while adj1==len(sub_list1)-1 or adj1==-5:
           adj1=random.randint(0,len(sub_list1)-2)
           print("inside the while")
  else:
    if not len(sub_list1)==0:
       adj1=random.randint(0,len(sub_list1)-1)

  #DCJ and duplication require two adj
  if operation=="DCJ":
     #pick a second sublist
     sub_list2=[]
     while len(sub_list2)==0:
        sub_list2=random.choices(list, weights=weights_sublist, k=1)[0]

        #find the index of sub_list
        sub_pos2=list.index(sub_list2)

     #initially set to -5
     adj2=-5

     #if adj2 has not been picked yet or adj1 and adj2 are the same, pick again; can't choose the same adj twice
     while(sub_pos1==sub_pos2 and adj1==adj2)or adj2==-5:
           print("subpos1"+ str(sub_pos1))
           print("subpos2" + str(sub_pos2))
           print("adj1" + str(adj1))
           #pick a second adj2
           #if linear, can't pick the last 0
           if 0 in sub_list2:
              print("0 is in the sublist2")
              print("adj2: " + str(adj2))
              while adj2==-5 or (adj1==adj2 and sub_pos1==sub_pos2):
                   print("inside the while loop")
                   if len(sub_list2)<3 and (adj2 is not -5):
                       print("adj is" + str(adj2))
                       print("len is" + str(len(sub_list2)-1))
                       #adj2=random.randint(0,len(sub_list2)-2)
                       print("adj is" + str(adj2))
                       print("inside the else")
                       sub_list2=random.choices(list, weights=weights_sublist, k=1)[0]
                       while len(sub_list2)==0:
                             print("inside the else while loop")
                             sub_list2=random.choices(list, weights=weights_sublist, k=1)[0]
                             print("both adj are the same and there are no more adj to pick from the same list")

                       if 0 in sub_list2:
                           adj2=random.randint(0,len(sub_list2)-2)
                       else:
                           adj2=random.randint(0, len(sub_list2)-1)
                   else:
                       
                       adj2=random.randint(0,len(sub_list2)-2)


                   sub_pos2=list.index(sub_list2)
                   print("subpos2: " + str(sub_pos2)+ "len is:" + str(len(sub_list2)))
           else:
              if (adj1==adj2 and sub_pos1==sub_pos2) and len(sub_list2)<=1: 
                   sub_list2=random.choices(list, weights=weights_sublist, k=1)[0]
                   while len(sub_list2)==0:
                       sub_list2=random.choices(list, weights=weights_sublist, k=1)[0]

              else:
                   adj2=random.randint(0,len(sub_list2)-1)
              

              sub_pos2=list.index(sub_list2)
                          

  else:
    #-5 indicates these variables are not required for those operations and -5 is just a placeholder
    adj2=-5
    sub_pos2=-5

  if operation=="Deletion":
    #print(chosen_length)
    sub_list=list[sub_pos1]
    if 0 in sub_list:
      #final length to be duplicated or deleted can not be longer than the remaining length
      if adj1==0:
         print('adj 0 has been picked for deletion')
         final_length=min(length, len(sub_list)-adj1-2)
      else:
         final_length=min(length, len(sub_list)-adj1-1)
         
    else:
      #final length to be duplicated or deleted can not be longer than the remaining length
      final_length=min(length, len(sub_list)-adj1)

    print("final length is:" + str(final_length))

    while (final_length==0):
         sub_list=random.choices(list, weights=weights_sublist, k=1)[0]
         while 0 in sub_list and len(sub_list)==2:
                   sub_list=random.choices(list, weights=weights_sublist, k=1)[0]
         print("sublist: " + str(list.index(sub_list)))
         if 0 in sub_list:
                adj1=random.randint(0, len(sub_list)-2)
         else: 
                adj1=random.randint(0, len(sub_list)-1)

         if 0 in sub_list:
         #final length to be duplicated or deleted can not be longer than the remaining length
            if adj1==0:
              final_length=min(length, len(sub_list)-adj1-2)
            else:
              final_length=min(length, len(sub_list)-adj1-1)
      
         else:
            #final length to be duplicated or deleted can not be longer than the remaining length
            final_length=min(length, len(sub_list)-adj1)

    sub_pos1=list.index(sub_list)

  else:
    #-5 is a placeholder for operations that do not require a length
    final_length=-5

  return adj1, adj2, sub_pos1, sub_pos2, final_length








def write_file2(evolved_list,i, file_name='Gi.txt'):

  with open("Gzero.txt","r") as file1:
    Firstline=file1.readline()
    Secondline=file1.readline()

  with open(file_name, "w") as file:
     file.write(Firstline)
     file.write(Secondline)
     file.write("\n")
     file.write("> G"+ str(i))
     file.write("\n")
     for k in evolved_list[:]:
         #print(i)
         for j in k:
            #print(j)
            if not j==0:
              file.write(str(j)+ " ")
         if 0 in k:
          file.write("| ")
         else:
          file.write(") ") 



def write_file(evolved_list,i, file_name):

  if i==0:
     access_type='w'
  else:
    access_type='a'


  with open(file_name, access_type) as file:
     file.write("> G"+ str(i))
     file.write("\n")
     for k in evolved_list[:]:
         #print(i)
         for j in k:
            #print(j)
            if not j==0:
              file.write(str(j)+ " ")
         if 0 in k:
          file.write("| ") ### I changed "|" to "| "
         else:
          file.write(") ") ### I changed ")" to ") "

     file.write('\n')




def distance(evolved_list, i):
    write_file2(evolved_list, i, file_name='Gi.txt')
    command = [
        "java",
        "-jar",
        "UniMoG-java11.jar",  # Updated filename
        "-m=6",
        "Gi.txt",
        "-p"
    ]
    pipe = Popen(command, shell=False, stdout=PIPE, stderr=PIPE)
    stdout, stderr = pipe.communicate()

    if stderr:
        print("Error:", stderr.decode())
    
    output_lines = stdout.decode().splitlines()
    
    for line in output_lines:
	 print("this is the output line from unimog:")
         print(line)
        if "(DCJ-indel) :" in line:
            distance_str = line.split("(DCJ-indel) :")[1].strip()
            try:
                distance_value = int(distance_str)
                print("Distance Value:", distance_value)  # Add this line for debugging
                return distance_value
            except ValueError:
                print("Failed to convert the distance value to an integer:", distance_str)
    
    print("No valid distance value found in the output.")
    return None








def generate_genome_NoDup():

    #linear: list of all linear chromosome
    linear=[]

     #circular:list of length for al circular chromosomes
    circular=[]

    #ask the user to input the length for all linear chromosomes
    user_input=input("Enter the lengths of all linear chromosomes as a list:")

    #convert the asnwer to a list
    linear= [int(l) for l in user_input.split(",")]
    
    #ask the user to input the length for all linear chromosomes
    user_circular=input("Enter the lengths of all circular chromosomes as a list:")

    #writing the initial user input into a file
    with open ("user_input.txt", 'w') as file:
        file.write("Linear Chromosome: "+ '\n')
        file.writelines(','.join(map(str,linear)))
        file.write('\n'+ "Circular Chromosome: "+ '\n')
        file.writelines (map(str,user_circular))
        file.close()
    #convert the asnwer to a list
    circular=[int(l) for l in user_circular.split(",")]

    #list: list is the genoem the function will make
    list=[]

    #sublist: chromosomes that we make
    sublist=[]

    #all_gene: contains all gene that have already been added to the genome
    all_gene=[]


    count=0
    if not linear[0]==0:
     for i in range(0,len(linear)):     
     #append 0 at the begining of linear chromosome
        sublist.append(0)
        for k in range(1+count,count+linear[i]+1):
            sublist.append(k)
            all_gene.append(k)
        count=count+linear[i]
        #0 at the end of linear chromosome
        sublist.append(0)
        #add teh sublist to the main list which is the genome
        list.append(sublist)
        #empty the sublist for next round
        sublist=[]

    count=sum(linear)
    if not circular[0]==0:
     for i in range(0,len(circular)):
        for k in range(1+count,count+circular[i]+1):
            sublist.append(k)
            all_gene.append(k)
        count=count+circular[i]
        #add teh sublist to the main list which is the genome
        list.append(sublist)
        #empty the sublist for next round
        sublist=[]       
    return list, all_gene




def main():
  
       #ask the user if they want to give a genome or want the program to generate one
       ans=input("Do you want the program to generate a genome for you?(Y=yes or N=No)")
       if ans=='Y':
           list,all_gene=generate_genome_NoDup()
           print(list)
           
       else:
           input_string = input("Enter a sequence of numbers(except for 0) separated by '|' and for linear chromosome, add a 'L' before '|' to indicate linear ")
           print(input_string)
           # Split the input string by '|'
           number_groups = input_string.split('|')
           #list: list the whole genome with chromosomes being sublist
           #each sublist is a chromosome
           #0 at the end of a sublist indicates linear chromosome
           list=[]
           #all_gene: list of all genes or markers
           all_gene=[]


           # Process each group of numbers
           item='L'

           for group in number_groups:
                if len(group)>0:
                    # Split the group by whitespace and convert each number to an integer
                    #print(group)
                    if item in group:
                        new_group=group.replace('L', '0')
                    else:
                        new_group=group
                    numbers = [int(num) for num in new_group.strip().split()]

                    if 0 in numbers:
                        numbers.insert(0, 0)

                    list.append(numbers)

           print(list)

       #saving the original genome given by user to a separate variable
       original_genome=list
       my_genome = copy.deepcopy(original_genome)
       #original_gene: the gene content of the original genome
       original_gene=[element for sublist in my_genome for element in sublist if element!=0]
  
       #creating a list for weights
       weights_sublist=[]

       #list of ditances
       dList=[]
       dList.append(0)

       #num_steps:number of generations for evolution
       num_steps=input("Enter the number of steps: ")
       print(num_steps)

       ###operations:list with the 3 possible genomic operators
       operations = ['DCJ',  'Deletion', 'Insertion']
    
       ###weights: list of weights for genomic operators
       ###Adjust the weights as per your preference
       weight_DCJ=input("Weight of DCJ: ")
       weight_insertion=input("Weight of insertion: ")
       weight_deletion=input("Weight of deletion: ")
       weights = [float(weight_DCJ),float(weight_deletion),float(weight_insertion)]
         

       #determining the length:
       #ask the user what the max length will be for insertion and deletion
       max_length_insertion = int(input("Enter the value of max length for insertion: "))
       max_length_deletion = int(input("Enter the value of max length for deletion: "))
       #ask the user for the number of times the model should run(average)
       avg=input("How many times you want to run the model?" )

       #write down user_input into the user_input.txt file
       with open ("user_input.txt", "a") as file:
            file.write('\n'+ "Max length insertion: "+str(max_length_insertion)+'\n')
            file.write("Max length deletion: "+str(max_length_deletion)+ '\n')
            file.write('\n'+"Number of steps: "+ str(num_steps))
            file.write('\n'+"The number of time user wants to run the model(avg): "+str(avg))
            file.write('\n'+ "weight of DCJ: "+ str(weight_DCJ))
            file.write("\n"+ "weight of insertion: " + str(weight_insertion))
            file.write("\n" + "weight of deletion: " + str(weight_deletion))
            file.close()
  
       #writing the original genome in Gzero.txt
       write_file(original_genome,0,"Gzero.txt")
     
       print("original genome before loop:")
       print(my_genome)
       
       



       # looping for calculating avg distance
       for q in range(int(avg)):
                list=copy.deepcopy(my_genome)
                print("original genome within loop: ")
                print(my_genome)
                weights_sublist=[]
                
                #list of ditances
                dList=[]
                dList.append(0)
              
                all_gene=copy.deepcopy(original_gene)
                
                print("This is the  step number for the avg: "+ str(q+1))
                for p in range(0,int(num_steps)):
                      print("this is step within nested loop: "+ str(p+1))
                      if not p==0:
                             #updating variables:
                             #each step, the evolved_list from last step will become the original genome
                             list=evolved_list
             
                             #update all_gene which contains all genes without any sub_list
                             all_gene=[item for sublist in list for item in sublist]

                             #weight_sublist: list containing the weights for each sublist
                             weights_sublist=[]

                             #create the resulting list



                      evolved_list=[]

                      #randomly pick an operation
                      operation = random.choices(operations, weights=weights, k=1)[0]
                      print("operation has been picked: " + str(operation)) 
                      # #creating the weighst for each sub_list
                      #count:number of non_zero elements
                      count = 0
                      num_zero = 0
                      for num in all_gene:
                         if num != 0:
                            count += 1
                         else:
                            num_zero+=1

                      N=count+ num_zero/2

                      for m in list:
                           #sub_count:non-zero numbers in each sublist
                           sub_count=0
                           #sub_zero:number of zeroes in the sublist
                           sub_zero=0
                           for j in m:
                               if j != 0:
                                   sub_count += 1
                               else:
                                   sub_zero+=1

                           weight=sub_count + sub_zero/2
                           weights_sublist.append(weight/N)
                      print("counting")

                      #non_empty:keeps track of the number of sublist that has more than 1 element which includes the telomeres(0)
                      non_empty=0
                      for m in list:
                        if len(m)>=1:
                            non_empty+=1
                      
                      if non_empty<=1:
                          for m in list:
                             if len(m)==1:
                                while operation=="DCJ":
                                   print("while loop inside main")
                                   operation=random.choices(operations, weights, k=1)[0]
                        
                          
                      #based on the picked operation, call appropriate functions
                      if operation=='DCJ':
                               #chosen_length: placeholder
                               chosen_length=-5
                               print("inside DCJ calling")
                               #call function to pick adj
                               adj1, adj2, sub_pos1, sub_pos2, final_length=pick_adj(list, weights_sublist, chosen_length, operation)
                               evolved_list=perform_DCJ(list, adj1, adj2, sub_pos1, sub_pos2)

                      elif operation=='Insertion':
                               #a list with all possible lengths
                               list_of_length = []
                               for i in range(1, max_length_insertion + 1):
                                         list_of_length.append(i)
                               #randomly choose a length between 1 and the max length given by user
                               chosen_length = random.choices(list_of_length)[0]
                               #call function to pick adj
                               adj1, adj2, sub_pos1, sub_pos2, final_length=pick_adj(list, weights_sublist, chosen_length, operation)

                               evolved_list=perform_insertion(list, all_gene, sub_pos1, adj1,chosen_length)


                      else: #operation=='Deletion':
                               #a list with all possible lengths
                               list_of_length = []
                               for i in range(1, max_length_deletion + 1):
                                     list_of_length.append(i)
                               #randomly choose a length between 1 and the max length given by user
                               chosen_length = random.choices(list_of_length)[0]
                               print("this is chosen length" + str(chosen_length))
                               #call function to pick adj
                               adj1, adj2, sub_pos1, sub_pos2, final_length=pick_adj(list, weights_sublist, chosen_length, operation)
                               #print("this is final length " + str(final_length))
                               evolved_list=perform_deletion(list, all_gene, sub_pos1, adj1, final_length)
                               print("adj picked for deletion: " + str(adj1))
                               print("subposition picked: " + str(sub_pos1))
                               print("final length chosen "+ str(final_length))

                      if p==0:
                         mode="w"
                      else:
                         mode="a"
                      print("Evolved_list:  ")
                      print(evolved_list)
                      
                      #num_chromosome:keeps track of number of non-zero list in the genome
                      num_chromosome=[]

                      # Count the number of non-zero lists to see how the number of chromosomes change over generations
                      non_zero_count = sum(1 for sub_list in evolved_list if any(sub_list))
                      num_chromosome.append(non_zero_count)
                      print("Number of non-zero lists:", num_chromosome)
                      with open("num_chromosomes_evolved_1.txt",mode) as file:
                            file.write("num of step " + str(p)+ ":")
                            file.write(str(len(evolved_list)))
                            file.write("\n")
                            file.close()
 
                      
                      #calling the gene_content function to write info about gene content
                      gene_content(q,p,original_gene,evolved_list)
                      dList.append(distance(evolved_list,p+1))
                      print(dList)
                     
                    
                      #if the genome is empty meaning no lists with non-zero item, break out of the inner loop(generations)
                      if non_zero_count==0:
                         break


                      #when it is the first step of the avg, create the file with w mode 
                      if q==0:
                         mode="w"
                      else:
                         mode="a"

                with open("Distance.txt",mode) as file_d: 
                      #file_d.write("Distances: ")
                      #file_d.write("\n")
                      file_d.write(str(dList))
                      file_d.write("\n")
		  
                with open ("unique_original_genes.txt", "a") as file:
                      file.write("\n")
                with open ("unique_evolved_genes.txt", "a") as file:
                      file.write("\n")
                with open ("common_genes.txt", "a") as file:
                      file.write("\n")


                print("original genome within nested for loop:")
                print(my_genome)
               
    


    
def gene_content(q, p, all_gene, evolved_list):
    flattened_list = [element for sublist in evolved_list for element in sublist if element != 0]

    set1 = set(map(abs, all_gene))
    set2 = set(map(abs, flattened_list))

    unique_elements_list1 = list(set1 - set2)
    len_unique_original = len(unique_elements_list1)
    print("len original" + str(len_unique_original))
    unique_elements_list2 = list(set2 - set1)
    len_unique_evolved = len(unique_elements_list2)
    print("len evolved" + str(len_unique_evolved))
    common_elements = list(set1.intersection(set2))
    len_common = len(common_elements)

    # if this is the first evolved genome, we will create a new file
    mode = 'w' if (q == 0 and p==0) else 'a'

    # Print or use the results as needed
    with open("unique_original_genes.txt", mode) as file:
        file.write(f"{len_unique_original} ")
        file.write(" ")
        print("len original" + str(len_unique_original))

    with open("unique_evolved_genes.txt", mode) as file:
        file.write(f"{len_unique_evolved} ")
        file.write(" ")

    with open("common_genes.txt", mode) as file:
        file.write(f"{len_common} ")
        file.write(" ")


if __name__ == '__main__':
    main()





