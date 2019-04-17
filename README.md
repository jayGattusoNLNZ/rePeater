# rePeater
This little tool takes in a list of "instructions" and replays them against a file system


The first script is a an instruction building tool. 

Its all very manual. 

You add the name of the file you want to create (e.g. "my_log_file")

You add the name of the collection root. It could be a drive mount/share, or it could be a sub folder. The only important thing is that one parent folder is used for the whole set of instructions in your log file. 

The buttons are the "magic". Each one adds a line to your log file that is tab separated and includes all the data needed to repeat the action. 

You log the instruction, hit the button, and it records your instruction. 

The collection root label is removed from your any locations in your instruction, and the scripts that are used to "replay" the instuctions will deal with turning the relative paths into absolute paths as needed downstream

It supports the following instuctions. All units are tab seperated

*Delete*

delete  thing_to_be_deleted

*Move*

move  source_item destination_folder

*Extract* 

extract path_to_container path_of_item_in_zip destination_folder


*Rename*

rename  original_path new_path
