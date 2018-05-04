import csv
import logging


## File Processing Functions
def read_controls(control_filename):
	""" Load Controls from controls.csv """
	with open(control_filename, 'r') as control_file:
		control_reader = csv.DictReader(control_file)
		controls = {}
		for file in control_reader:
			controls[file['file_name']] = {'join_cols': file['columns_in_join'], 'display_cols': file['display_columns']}
		return controls

def process_file(file_name, control_params):
	""" Process single file using definitions in controls, into memory """
	with open(file_name, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		file_dict = {}
		for row in csv_reader:
			k = '-'.join([row[col] for col in control_params['join_cols'].split(', ')])
			v = [row[col] for col in control_params['display_cols'].split(', ')]
			file_dict[k] = v
		return file_dict

def join_files(file_dict1, file_dict2):
	""" Given two pre-processed file dictionaries, left join it together by the join columns """
	new_dict = {}
	for k in file_dict1:
		row = []
		row.extend(file_dict1[k])
		row.extend(file_dict2.get(k, ''))
		new_dict[k] = row
	return new_dict


if __name__ == '__main__':
	
	## set logging to see where script is going
	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger()

	## read control file, which is a flexible way to deal with different files
	control_filename = 'controls.csv'
	controls = read_controls(control_filename)
	logger.info('Read Control File')

	## process files one by one into a dictionary
	output_headers = []
	file_dicts = []
	for i, file in enumerate(controls):
		file_dicts.append(process_file(file, controls[file]))
		output_headers.extend(controls[file]['display_cols'].split(', '))
	logger.info('Read {} files'.format(i+1))

	## join files one by one using python reduce, then put into output file with only desired columns
	rows = reduce(join_files, file_dicts).values()
	with open('output.csv', 'w') as out_file:
		csv_writer = csv.writer(out_file)
		csv_writer.writerow(output_headers)
		csv_writer.writerows(rows)
	logger.info('file output generated to output.csv')
