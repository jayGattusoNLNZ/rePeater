# rePeater
This little tool takes in a list of "instructions" and replays them against a file system


The first script is a an instruction building tool. 

Its all very manual. 

You add the name of the file you want to create (e.g. "my_log_file")

You add the name of the colleciton root. It could be a drive mount/share, or it could be a sub folder. The only important thing is that one partent folder is used for the whole set of instructions. 

The buttons are the "magic". Each one adds a line to your log file thats tab separated and includes all the data needed to repeat the action. 

You log the instruction, hit the button, and it records your instruction. 

The collection root label is removed from your instrucion, and the scripts that are used to "replay" the instuctions will deal with turning the relative paths into absolute paths as needed

It supports the following instuctions.

Delete

Instuction: 

delete  thing_to_be_deleted

Move

instruction:

move  source_item destination_folder

Extract {needs some work}... 

extract path_to_container path_of_etracted_item

I need to work out the best way of indicating the destination of the file


Rename

rename  original_path new_path
