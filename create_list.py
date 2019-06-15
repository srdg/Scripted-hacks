import argparse
def main():	
	mails = []

	parser = argparse.ArgumentParser(description='Create mailing lists for batches')
	parser.add_argument('-f','--file', type=str,  help='file containing member details',metavar='')
	parser.add_argument('-o','--output', type=str, help='file to write to',metavar='')
	parser.add_argument('-g','--group', type=str, help='group of mailing list',metavar='')
	args = vars(parser.parse_args())

	with open(args["file"],"r") as f:
		f.seek(1)
		for line in f:
			fname,lname,mail,_,_,_=line.split(",")
			mails.append(mail)
			print(fname+' '+lname)

	mails.pop(0)

	with open(args["output"],"w+") as f:
		f.write("Group Email [Required],Member Email,Member Type,Member Role\n")
		grp = args["group"].lower()
		lines=[]
		for mail in mails:
			line=grp+','+mail+',USER,MEMBER\n'
			lines.append(line)
		f.writelines(lines)


if __name__ == '__main__':
	main()