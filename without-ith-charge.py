from tempfile import mkstemp
from shutil import move
from os import remove, close
import re

def replace(file_path, pattern, subst, new_file_path):
    #Create temp file
    lineNumber = 0
    maxLine = 32
    i = 6
    changed = 0
    molecule = "A"
    while(changed <= maxLine) :
        lineNumber = 0
        fh, abs_path = mkstemp()
        with open(file_path) as old_file:
            with open(str(changed) + file_path,'w') as new_file:    
                for line in old_file:
                    # new_file.write(line.replace(pattern, subst))
                    if lineNumber < 13:
                        lineNumber = lineNumber + 1
                        new_file.write(line)
                        continue
                    if len(line.split()) >= 1 :
                        my_string = line;
                        words = my_string.split( )
        
                        
                        ##print(words[6])
                        try:
                            if words[1] == molecule and lineNumber == 13 + changed :
                                my_string = line
                                words = my_string.split( )
                                words[0] = words[0].rjust(8)
                                words[1] = words[1].ljust(4)
                                words[2] = words[2].ljust(4)
                                words[3] = words[3].ljust(4)
                                words[4] = words[4].ljust(4)
                                words[5] = words[5].ljust(5)
                                words[6] = words[6].rjust(10)
                                words[7] = words[7].rjust(13)
                                words[8] = words[8].rjust(11)
                               
                                
                            
                                words[i]=" 0.000000"
                                
                               ## i = i+(lineNumber*9)
                                line = " ".join(words)
                                line += '\n'
                        except:
                            print("index oob at:" + str(changed+1) +"  " + str(lineNumber))
                    lineNumber = lineNumber + 1
                    new_file.write(line)
              ##  close(fh)
                ##move(abs_path, ( str(changed) + new_file_path))

            changed += 1

    
replace("phe_solvated.txt", "charge", "0.00", "newphe_solvated.txt.psf")
