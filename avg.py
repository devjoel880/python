# use mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        print(line)
        ipos = line[18+2:]
        
        # Convert to a floating-point data type
        try:
            val = float(ipos)
            total = total + val
            # val = val + val
        except:
            print('ERROR')

print('Line count:', count)
if count > 0:
    avg = total / count
    print("Average spam confidence:", avg)
else:
    print("No lines found")
