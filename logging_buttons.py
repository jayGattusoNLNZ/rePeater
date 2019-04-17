from tkinter import font
from tkinter import ttk
import tkinter as tk


root = tk.Tk()
file_name_frame = tk.Frame(root)
col_root_frame = tk.Frame(root)
delete_frame = tk.Frame(root)
move_frame = tk.Frame(root)
extract_frame = tk.Frame(root)
rename_frame = tk.Frame(root)
last_command_frame  = tk.Frame(root)
my_button_font = ('helvetica', 16, 'bold')
my_guide_font = ('helvetica', 8)


def deleteCallBack():
	my_path = delete_path_name.get().replace(collection_root.get().strip(), "", 1)
	my_path = my_path.replace(collection_root.get(), "", 1)
	log_f_name = "{}.txt".format(log_file_name.get())
	log_row = f"delete\t{my_path}"
	with open(log_f_name, "a") as data:
		data.write(log_row+"\n")

	last_command_text.delete( 1.0, tk.END)
	last_command_text.insert(tk.END, log_row)

	delete_path_name.delete( 0, tk.END)

def moveCallBack():
	my_path_orginal = move_source_name.get().replace(collection_root.get().strip(), "", 1).strip()
	my_path_destination = move_destination_name.get().replace(collection_root.get().strip(), "", 1).strip()
	log_f_name = "{}.txt".format(log_file_name.get().strip())

	log_row = f"move\t{my_path_orginal}\t{my_path_destination}"
	with open(log_f_name, "a") as data:
		data.write(log_row+"\n")
	
	last_command_text.delete( 1.0, tk.END)
	last_command_text.insert(tk.END, log_row)

	move_source_name.delete( 0, tk.END)
	move_destination_name.delete( 0, tk.END)

def extractCallBack():
	my_zip_file = extract_zip_file.get().replace(collection_root.get().strip(), "", 1).strip()
	my_file_from_zip = extract_file_from_zip.get().strip()
	my_new_zip_file_location = extract_new_file_from_zip_location.get().replace(collection_root.get().strip(), "", 1).strip()
	log_f_name = "{}.txt".format(log_file_name.get().strip())

	log_row = f"extract\t{my_zip_file}\t{my_file_from_zip}\t{my_new_zip_file_location}"
	with open(log_f_name, "a") as data:
		data.write(log_row+"\n")

	last_command_text.delete( 1.0, tk.END)
	last_command_text.insert(tk.END, log_row)

	# extract_zip_file.delete( 0, tk.END) ### hmmm. TODO - poss include a check box.. 
	extract_file_from_zip.delete( 0, tk.END)
	extract_new_file_from_zip_location.delete( 0, tk.END)

def renameCallBack():
	my_original_file_path = rename_source_name.get().replace(collection_root.get().strip(), "", 1).strip()
	my_destination_file_path = rename_destination_name.get().replace(collection_root.get().strip(), "", 1)
	log_f_name = "{}.txt".format(log_file_name.get().strip())

	log_row = f"rename\t{my_original_file_path}\t{my_destination_file_path}"
	with open(log_f_name, "a") as data:
		data.write(log_row+"\n")

	last_command_text.delete( 1.0, tk.END)
	last_command_text.insert(tk.END, log_row)

	rename_source_name.delete( 0, tk.END)


log_file_name = tk.Entry(file_name_frame, width=30)
log_file_label = tk.Label(file_name_frame, text ="Logfile name")
collection_root = tk.Entry(col_root_frame, width=30)
collection_root_label = tk.Label(col_root_frame, text ="Collection root")

delete_logger = tk.Button(delete_frame, text ="Delete", command=lambda: deleteCallBack(),  height=2, width=10, bg = "indian red")
delete_logger.config(font=my_button_font)
delete_label = tk.Label(delete_frame, text="Full path to folder or file:")
delete_label.config(font=my_guide_font)
delete_path_name = tk.Entry(delete_frame, width=30)

move_logger = tk.Button(move_frame, text ="Move", command=lambda: moveCallBack(), height=2, width=10, bg = "DarkSeaGreen2")
move_logger.config(font=my_button_font)
move_source_name = tk.Entry(move_frame, width=30)
move_source_label = tk.Label(move_frame, text="Full path of source folder or file:")
move_source_label.config(font=my_guide_font)
move_destination_name = tk.Entry(move_frame, width=30)
move_destingation_label = tk.Label(move_frame, text="Full path of destination folder:")
move_destingation_label.config(font=my_guide_font)

extract_logger = tk.Button(extract_frame, text ="Extract", command=lambda: extractCallBack(), height=2, width=10, bg="SteelBlue2")
extract_logger.config(font=my_button_font)
extract_zip_label = tk.Label(extract_frame, text="Path to zip file:")
extract_zip_label.config(font=my_guide_font)
extract_zip_file = tk.Entry(extract_frame, width=30)
extract_file_label = tk.Label(extract_frame, text="Path in zip file if file or folder")
extract_file_label.config(font=my_guide_font)
extract_file_from_zip = tk.Entry(extract_frame, width=30)
extract_new_file_from_zip_location = tk.Entry(extract_frame, width=30)
extract_new_file_from_zip_location_label = tk.Label(extract_frame, text="Destination folder")
extract_new_file_from_zip_location_label.config(font=my_guide_font)

rename_logger = tk.Button(rename_frame, text ="Rename", command=lambda: renameCallBack(), height=2, width=10, bg = "MediumPurple2")
rename_logger.config(font=my_button_font)
rename_source_name = tk.Entry(rename_frame, width=30)
rename_source_label = tk.Label(rename_frame, text="Full path of original file:")
rename_source_label.config(font=my_guide_font)
rename_destination_name = tk.Entry(rename_frame, width=30)
rename_destingation_label = tk.Label(rename_frame, text="New full path of file:")
rename_destingation_label.config(font=my_guide_font)

last_command_text = tk.Text(last_command_frame,  height=2, width=55, wrap=tk.WORD)

##### layout

log_file_label.grid(row=1, column=1)
log_file_name.grid(row=1, column=2)
log_file_name.insert(tk.END, 'E.G. log_file_name')
file_name_frame.grid(row=1, column=1, padx=5,  pady=5 )

collection_root_label.grid(row=1, column=1)
collection_root.grid(row=1, column=2)
collection_root.insert(tk.END, 'E.G. c:\my_collection')
col_root_frame.grid(row=2, column=1, padx=5,  pady=5 )

ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=3, column=1, columnspan=3, sticky='we', padx=10,  pady=10 )

delete_logger.grid(row=1, column=1, rowspan=3, padx=10,  pady=10 )
delete_label.grid(row=1, column=2)
delete_path_name.grid(row=2, column=2)
delete_frame.grid(row=4, column=1)

ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=5, column=1, columnspan=3, sticky='we', padx=10,  pady=10 )

move_logger.grid(row=1, column=1, rowspan=5, padx=10,  pady=10 )
move_source_label.grid(row=1, column=2)
move_source_name.grid(row=2, column=2)
move_destingation_label.grid(row=3, column=2)
move_destination_name.grid(row=4, column=2)
move_frame.grid(row=6, column=1)

ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=7, column=1, columnspan=3, sticky='we', padx=10,  pady=10 )

extract_logger.grid(row=1, column=1, rowspan=5, padx=10,  pady=10  )
extract_zip_label.grid(row=1,column=2)
extract_zip_file.grid(row=2,column=2)
extract_file_label.grid(row=3,column=2)
extract_file_from_zip.grid(row=4, column=2)
extract_new_file_from_zip_location_label.grid(row=5, column=2)
extract_new_file_from_zip_location.grid(row=6, column=2)
extract_frame.grid(row=8, column=1)

ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=9, column=1, columnspan=3, sticky='we', padx=10,  pady=10 )

rename_logger.grid(row=1, column=1, rowspan=3, padx=10,  pady=10 )
rename_source_label.grid(row=1, column=2)
rename_source_name.grid(row=2, column=2)
rename_destingation_label.grid(row=3, column=2)
rename_destination_name.grid(row=4, column=2)
rename_frame.grid(row=10, column=1)

ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=11, column=1, columnspan=3, sticky='we', padx=10,  pady=10 )


last_command_text.grid(row = 1, column = 1)
last_command_frame.grid(row=12, column=1)

root.wm_attributes("-topmost", 1)
root.lift()
root.mainloop()
