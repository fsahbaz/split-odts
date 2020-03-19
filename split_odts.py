import re
# It is suggested to have a back up of the file to be operated on, since mistakes can lead to a loss of data.
# Constants regarding files to be separated.
file_no = 0
found = False
src_path = 'oommf/app/oxs/examples/finalCheck3.odt'
dest_path = 'ODTs/'
''' 
Can be generalized to other text files by changing the start and end points according their
reference points/texts.
'''
s = re.compile('# Table Start')
e = re.compile('# Table End')
# Naming conventions, may change with context.
widths = [1e3 * 0.0500, 1e3 * 0.0698, 1e3 * 0.0973, 1e3 * 0.1357]
amps = [1e04*0.5179, 1e04*0.6105, 1e04*0.7197, 1e04*0.8483, 1e04*1]
file_names = [] 
for i in range(len(amps)):
	for j in range(len(widths)):
		file_names.append((str(int(amps[i])) + '-' + str(int(widths[j]))))
# Empty list to store the lines to be saved.			  
lines = []
# A while loop to iterate through and separate the odt file.
while file_no < len(file_names):
    with open(src_path,'r') as in_file:
        for line in in_file.readlines():
            line = line.strip()
            if re.match(s, str(line)):
                found = True
            elif re.match(e, str(line)):
                found = False
                with open(dest_path + file_names[file_no] + '.odt', 'w') as out_file:
                	lines.append('# Table End')
                	out_file.write('\n'.join(lines))
                	lines = []
                with open(src_path,'w') as in_file:
                	if line.strip() not in lines:
                		in_file.write(line)
                print(file_names[file_no] + " is saved and file is reset, moving on.")
                file_no += 1
            if found:
                lines.append(line)
# When the process ends:
print('Done splitting files.')
