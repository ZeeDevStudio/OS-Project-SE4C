import os
import shutil
import time
from datetime import datetime
import subprocess
import platform

def browse_and_select_folder(current_path):
	while True:
		os.system('cls')
		print(f"\n*** Create File / Folder ***")
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		folders_files=sorted(items)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. Create File')
		print('3. Create Folder')
		print('-------------------------------')
		for(idx,item)in enumerate(folders_files,start=4):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.')
				else:
					current_path=parent_path
			elif choice==2:
				file_name=input('Enter the file name with extension (e.g., file.txt): ').strip()
				if not file_name:
					print('File name cannot be empty. Please try again.')
				elif os.path.sep in file_name:
					print(f"File name cannot contain '{os.path.sep}'. Please try again.")
				else:
					file_path=os.path.join(current_path,file_name)
					try:
						with open(file_path,'w')as f:0
						print(f"File '{file_name}' created successfully at: {current_path}");time.sleep(3)
					except Exception as e:print(f"Error creating file: {e}")
			elif choice==3:
				new_folder_name=input('Enter the name for the new folder: ').strip()
				if new_folder_name:
					new_folder_path=os.path.join(current_path,new_folder_name)
					try:
						os.makedirs(new_folder_path,exist_ok=False)
						print(f"Folder '{new_folder_name}' created successfully.");time.sleep(3)
					except FileExistsError:
						print(f"Folder '{new_folder_name}' already exists. Please try a different name.")
					except Exception as e:
						print(f"Error creating folder: {e}")
				else:print('Folder name cannot be empty. Please try again.')
			elif 4<=choice<4+len(folders_files):
				selected_item=folders_files[choice-4]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:
					print(f"'{selected_item}' is a file. Please select a folder.")
			else:
				print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def create_file_or_folder():
	os.system('cls')
	print('\n*** File Management System ***\n')
	print('*** Create File / Folder ***\n')
	current_path=os.getcwd()
	result=browse_and_select_folder(current_path)
	if result is None:
		print('\nReturning to the main menu...')

def browse_and_delete_item(current_path):
	while True:
		os.system('cls')
		print(f"\n*** Delete File / Folder ***")
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		items_sorted=sorted(items)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		if os.path.basename(current_path):print('2. Delete this Folder')
		print('-------------------------------')
		for(idx,item)in enumerate(items_sorted,start=3):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2 and os.path.basename(current_path):
				confirm=input(f"Are you sure you want to delete the folder '{os.path.basename(current_path)}'? (Y/N): ").strip().lower()
				if confirm=='y':
					try:
						os.rmdir(current_path)
						print(f"Folder '{os.path.basename(current_path)}' deleted successfully.")
						time.sleep(3)
						return os.path.dirname(current_path)
					except OSError as e:print(f"Error deleting folder: {e}. Ensure the folder is empty.");time.sleep(3)
			elif 3<=choice<3+len(items_sorted):
				selected_item=items_sorted[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:
					confirm=input(f"Are you sure you want to delete the file '{selected_item}'? (Y/N): ").strip().lower()
					if confirm=='y':
						try:
							os.remove(selected_path)
							print(f"File '{selected_item}' deleted successfully.");time.sleep(3)
						except OSError as e:print(f"Error deleting file: {e}");time.sleep(3)
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def delete_file_or_folder():
	os.system('cls')
	print('\n*** File Management System ***\n')
	print('*** Delete File / Folder ***\n')
	current_path=os.getcwd()
	while True:
		result=browse_and_delete_item(current_path)
		if result is None:break
		else:current_path=result
	print('\nReturning to the main menu...')

def browse_and_rename_item(current_path):
	while True:
		os.system('cls')
		print(f"\n*** Rename File / Folder ***")
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		items_sorted=sorted(items)
		original_display_map={idx:item for(idx,item)in enumerate(items_sorted,start=3)}
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		if os.path.basename(current_path):print('2. Rename this Folder')
		print('-------------------------------')
		for(idx,item)in original_display_map.items():print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2 and os.path.basename(current_path):
				new_folder_name=input(f"Enter the new name for the folder '{os.path.basename(current_path)}': ").strip()
				if new_folder_name:
					parent_dir=os.path.dirname(current_path)
					new_folder_path=os.path.join(parent_dir,new_folder_name)
					try:
						os.rename(current_path,new_folder_path)
						print(f"Folder renamed to '{new_folder_name}'.");time.sleep(3)
						current_path=new_folder_path
					except OSError as e:print(f"Error renaming folder: {e}");time.sleep(3)
				else:print('Folder name cannot be empty.');time.sleep(3)
			elif 3<=choice<3+len(items_sorted):
				selected_item=items_sorted[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):current_path=selected_path
				else:
					file_root,file_extension=os.path.splitext(selected_item)
					new_file_name=input(f"Enter the new name for the file '{selected_item}' (without extension): ").strip()
					if new_file_name:
						full_new_file_name=f"{new_file_name}{file_extension}"
						new_file_path=os.path.join(current_path,full_new_file_name)
						try:
							os.rename(selected_path,new_file_path)
							print(f"File renamed to '{full_new_file_name}'.");time.sleep(3)
						except OSError as e:print(f"Error renaming file: {e}");time.sleep(3)
					else:print('File name cannot be empty.');time.sleep(3)
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def rename_file_or_folder():
	os.system('cls')
	print('\n*** File Management System ***\n')
	print('*** Rename File / Folder ***\n')
	current_path=os.getcwd()
	while True:
		result=browse_and_rename_item(current_path)
		if result is None:break
		else:current_path=result
	print('\nReturning to the main menu...')

def copy_file_or_folder(current_path):
	selected_items=[]
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print(f"\n*** Copy File/Folder ***")
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		items_sorted=sorted(items)
		original_display_map={idx:item for(idx,item)in enumerate(items_sorted,start=4)}
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. Select Files/Folders')
		print('3. Paste here')
		print('-------------------------------')
		for(idx,item)in original_display_map.items():print(f"{idx}. {item}")
		if selected_items:
			print('\nSelected Items for Copying:')
			for item in selected_items:print(f"- {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2:
				selected_item=select_items_for_copy(current_path,items_sorted,original_display_map)
				if selected_item:selected_items.extend(selected_item)
				print('Items added to the selection.');time.sleep(2)
			elif choice==3:
				if not selected_items:print('No items selected to copy. Please select items first.');time.sleep(3)
				else:paste_items(selected_items,current_path)
				selected_items=[]
			elif 4<=choice<4+len(items_sorted):
				selected_item=items_sorted[choice-4]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):current_path=selected_path
				else:print('Invalid option. Please try again.');time.sleep(3)
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def select_items_for_copy(current_path,items_sorted,original_display_map):
	try:
		item_numbers=input('Enter the numbers of the items to copy (comma-separated): ').strip()
		if not item_numbers:
			print('No input provided.')
			return[]
		selected_numbers=list(map(int,item_numbers.split(',')))
		selected_items=[]
		for num in selected_numbers:
			if num in original_display_map:
				selected_items.append(os.path.join(current_path,original_display_map[num]))
			else:print(f"Invalid number: {num}. Skipping.")
		return selected_items
	except ValueError:print('Invalid input. Please enter valid numbers separated by commas.');time.sleep(3)
	return[]

def paste_items(selected_items,destination_path):
	try:
		for item in selected_items:
			item_name=os.path.basename(item);destination=os.path.join(destination_path,item_name)
			if os.path.isdir(item):shutil.copytree(item,destination,dirs_exist_ok=True)
			else:shutil.copy2(item,destination)
			print(f"Copied: {item_name} -> {destination}")
		print('\nAll items copied successfully.');time.sleep(3)
	except Exception as e:print(f"Error while copying items: {e}");time.sleep(3)

def browse_and_move_items(current_path):
	selected_items=[]
	original_paths=[]
	while True:
		os.system('cls');print('\n*** File Management System ***\n')
		print('\n*** Move File/Folder ***')
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		items_sorted=sorted(items)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. Select Files/Folders')
		if selected_items:
			print('3. Paste Here')
		print('-------------------------------')
		for(idx,item)in enumerate(items_sorted,start=4):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2:
				print('\nEnter the numbers of the files/folders to move (comma-separated):')
				try:
					selection_input=input('').strip()
					selection_indices=[int(x)for x in selection_input.split(',')]
					for idx in selection_indices:
						if 4<=idx<4+len(items_sorted):
							selected_item=items_sorted[idx-4]
							selected_full_path=os.path.join(current_path,selected_item)
							if selected_full_path not in original_paths:selected_items.append(selected_item)
							original_paths.append(selected_full_path)
					print(f"Selected items for moving: {', '.join(selected_items)}");time.sleep(3)
				except ValueError:print('Invalid input. Please enter valid numbers separated by commas.');time.sleep(3)
			elif choice==3 and selected_items:
				for(src_path,item_name)in zip(original_paths,selected_items):
					dest_path=os.path.join(current_path,item_name)
					try:
						os.rename(src_path,dest_path)
						print(f"Moved '{item_name}' to '{current_path}'.")
					except OSError as e:print(f"Error moving '{item_name}': {e}")
				selected_items.clear()
				original_paths.clear();time.sleep(3)
			elif 4<=choice<4+len(items_sorted):
				selected_item=items_sorted[choice-4]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:print(f"'{selected_item}' is a file. Please select a folder to navigate into.");time.sleep(3)
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def browse_and_list_items(current_path):
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print('\n*** List File/Folder ***')
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		items_sorted=sorted(items)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. List All Files/Folders')
		print('-------------------------------')
		for(idx,item)in enumerate(items_sorted,start=3):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2:
				os.system('cls')
				print(f"\n*** Full Tree View of '{current_path}' ***\n")
				for(root,dirs,files)in os.walk(current_path):
					level=root.replace(current_path,'').count(os.sep)
					indent=' '*4*level
					print(f"{indent}{os.path.basename(root)}/")
					sub_indent=' '*4*(level+1)
					for file in files:print(f"{sub_indent}{file}")
				print('\nPress Enter to return to normal view...')
				input()
			elif 3<=choice<3+len(items_sorted):
				selected_item=items_sorted[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:print(f"'{selected_item}' is a file. Please select a folder to navigate into.");time.sleep(3)
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def browse_and_search_items(current_path):
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print('\n*** Search File/Folder ***')
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		items_sorted=sorted(items)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. Search here')
		print('-------------------------------')
		for(idx,item)in enumerate(items_sorted,start=3):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2:
				search_term=input('Enter the file or folder name to search for: ').strip()
				if not search_term:
					print('Search term cannot be empty.');time.sleep(2)
					continue
				print('\nSearching, please wait...')
				found_path=search_item(current_path,search_term)
				if found_path:
					os.system('cls')
					print(f"\n*** Search Results for '{search_term}' ***\n")
					print(f"Item found at: {found_path}\n")
					print('1. Open containing folder')
					print('2. Back to normal view')
					while True:
						try:
							action=int(input('\nEnter your choice: '))
							if action==1:
								if os.path.isdir(found_path):
									current_path=found_path
								else:current_path=os.path.dirname(found_path)
								break
							elif action==2:
								break
							else:print('Invalid option. Please try again.')
						except ValueError:print('Invalid input. Please enter a valid number.')
				else:print(f"'{search_term}' not found in '{current_path}' or its subfolders.");time.sleep(3)
			elif 3<=choice<3+len(items_sorted):
				selected_item=items_sorted[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:print(f"'{selected_item}' is a file. Please select a folder to navigate into.");time.sleep(3)
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def search_item(start_path,search_name):
	search_name_lower=search_name.lower()
	for(root,dirs,files)in os.walk(start_path):
		for folder in dirs:
			if search_name_lower in folder.lower():
				return os.path.join(root,folder)
		for file in files:
			if search_name_lower in file.lower():
				return os.path.join(root,file)

def view_properties(current_path):
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print(f"\n*** View Properties ***")
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		items_sorted=sorted(items)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. View Properties')
		print('-------------------------------')
		for(idx,item)in enumerate(items_sorted,start=3):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:
				return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2:
				selected_item=select_file_or_folder(current_path,items_sorted)
				if selected_item:
					os.system('cls')
					selected_path=os.path.join(current_path,selected_item)
					print(f"\n*** Properties of '{selected_item}' ***")
					if os.path.isfile(selected_path):
						display_file_properties(selected_path)
					elif os.path.isdir(selected_path):
						display_folder_properties(selected_path)
					input('\nPress Enter to return to normal view...')
			elif 3<=choice<3+len(items_sorted):
				selected_item=items_sorted[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:print(f"'{selected_item}' is a file. Use 'View Properties' to view its details.");time.sleep(2)
			else:print('Invalid option. Please try again.');time.sleep(2)
		except ValueError:print('Invalid input. Please enter a valid number.');time.sleep(2)

def select_file_or_folder(current_path,items_sorted):
	try:
		choice=int(input('\nSelect an item by entering its number: '))
		if 3<=choice<3+len(items_sorted):
			return items_sorted[choice-3]
		else:print('Invalid selection. Please try again.');time.sleep(2)
	except ValueError:print('Invalid input. Please enter a valid number.');time.sleep(2)
	
def display_file_properties(file_path):
	file_name=os.path.basename(file_path)
	file_size=os.path.getsize(file_path)
	created_time=datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
	modified_time=datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
	file_type=get_file_type(file_path)
	print(f"File Path: {file_path}")
	print(f"File Name: {file_name}")
	print(f"File Size: {file_size} bytes")
	print(f"Date Modified: {modified_time}")
	print(f"File Type: {file_type}")

def display_folder_properties(folder_path):
	folder_name=os.path.basename(folder_path)
	total_size,file_count,folder_count=get_folder_details(folder_path)
	print(f"Folder Path: {folder_path}")
	print(f"Folder Name: {folder_name}")
	print(f"Total Size: {total_size} bytes")
	print(f"Total Files: {file_count}")
	print(f"Total Sub-Folders: {folder_count}")

def get_file_type(file_path):
	_,extension=os.path.splitext(file_path)
	extension=extension.lower()
	file_types={'.txt':'Text Document','.jpg':'JPEG Image','.png':'PNG Image','.pdf':'PDF Document','.docx':'Word Document','.xlsx':'Excel Spreadsheet','.py':'Python Script'}
	return file_types.get(extension,'Unknown File Type')
	
def get_folder_details(folder_path):
	total_size=0
	file_count=0
	folder_count=0
	for(root,dirs,files)in os.walk(folder_path):
		folder_count+=len(dirs)
		file_count+=len(files)
		total_size+=sum(os.path.getsize(os.path.join(root,f))for f in files)
	return total_size,file_count,folder_count

def sorting(current_path,sort_method='Ascending (A-Z)'):
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print(f"\n*** Browse and Sort ***")
		print(f"Current Directory: {current_path}\n")
		print(f"Current Sort Method: {sort_method}\n")
		items=os.listdir(current_path)
		items_sorted=apply_sorting(items,current_path,sort_method)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. Sort Items')
		print('-------------------------------')
		for(idx,item)in enumerate(items_sorted,start=3):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2:sort_method=select_sort_method()
			elif 3<=choice<3+len(items_sorted):
				selected_item=items_sorted[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:print(f"'{selected_item}' is a file. Open it if required!");time.sleep(3)
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def apply_sorting(items,current_path,sort_method):
	if sort_method=='Ascending (A-Z)':
		return sorted(items)
	elif sort_method=='Descending (Z-A)':
		return sorted(items,reverse=True)
	elif sort_method=='Date Modified':
		return sorted(items,key=lambda item:os.path.getmtime(os.path.join(current_path,item)),reverse=True)
	elif sort_method=='Size':
		return sorted(items,key=lambda item:os.path.getsize(os.path.join(current_path,item)),reverse=True)
	return items

def select_sort_method():
	while True:
		os.system('cls')
		print('\n*** Select Sort Method ***')
		print('1. Ascending (A-Z')
		print('2. Descending (Z-A)')
		print('3. Date Modified')
		print('4. Size')
		print('-------------------------------')
		try:
			choice=int(input('Enter the number of your choice: '))
			if choice==1:
				return'Ascending (A-Z)'
			elif choice==2:
				return'Descending (Z-A)'
			elif choice==3:
				return'Date Modified'
			elif choice==4:
				return'Size'
			else:print('Invalid selection. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')
		time.sleep(2)

def open_files(current_path):
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print('\n*** File Browser ***')
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		directories=[item for item in items if os.path.isdir(os.path.join(current_path,item))]
		files=[item for item in items if os.path.isfile(os.path.join(current_path,item))]
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('-------------------------------')
		print('Folders:')
		for(idx,folder)in enumerate(directories,start=2):print(f"{idx}. {folder}")
		print('-------------------------------')
		print('Files:')
		for(idx,file)in enumerate(files,start=2+len(directories)):print(f"{idx}. {file}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.')
				else:current_path=parent_path
			elif 2<=choice<2+len(directories):
				selected_folder=directories[choice-2]
				current_path=os.path.join(current_path,selected_folder)
			elif 2+len(directories)<=choice<2+len(directories)+len(files):
				selected_file=files[choice-(2+len(directories))]
				open_file(os.path.join(current_path,selected_file))
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def open_file(file_path):
	try:
		if platform.system()=='Windows':os.startfile(file_path)
		elif platform.system()=='Darwin':subprocess.run(['open',file_path])
		else:subprocess.run(['xdg-open',file_path])
	except Exception as e:print(f"Error: Could not open file '{file_path}'. {str(e)}");time.sleep(2)

def find_duplicates(current_path):
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print('\n*** Duplicate Files Finder ***')
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		print('Options:')
		print('0. Main Menu')
		print('1. Back')
		print('2. Find Duplicate Files Here')
		print('-------------------------------')
		for(idx,item)in enumerate(items,start=3):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:print('You are already at the root directory.')
				else:current_path=parent_path
			elif choice==2:
				file_name=input('Enter the file name to search (with or without extension): ').strip()
				find_duplicate_files(current_path,file_name)
			elif 3<=choice<3+len(items):
				selected_item=items[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:print('You can only navigate into folders.')
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')

def find_duplicate_files(start_path,search_name):
	os.system('cls')
	print(f"Searching for duplicate files matching '{search_name}'...\n")
	duplicates=[]
	for(root,_,files)in os.walk(start_path):
		for file in files:
			if search_name in file if'.'not in search_name else search_name==file:duplicates.append(os.path.join(root,file))
	if len(duplicates)>1:
		print(f"Duplicate Files Found ({len(duplicates)}):\n")
		for dup in duplicates:print(f"- {dup}")
	elif len(duplicates)==1:print('Only one instance of the file was found. No duplicates detected.\n')
	else:print('No files matching the search criteria were found.\n')
	input('\nPress Enter to return to normal view.')

def convert_file_type_run(current_path):
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print('\n*** File Type Conversion ***')
		print(f"Current Directory: {current_path}\n")
		items=os.listdir(current_path)
		print('Options:')
		print('0. Main Menu');print('1. Back')
		print('2. Convert File Type')
		print('-------------------------------')
		for(idx,item)in enumerate(items,start=3):print(f"{idx}. {item}")
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==0:return
			elif choice==1:
				parent_path=os.path.dirname(current_path)
				if parent_path==current_path:
					print('You are already at the root directory.');time.sleep(2)
				else:current_path=parent_path
			elif choice==2:convert_file_type(current_path,items)
			elif 3<=choice<3+len(items):
				selected_item=items[choice-3]
				selected_path=os.path.join(current_path,selected_item)
				if os.path.isdir(selected_path):
					current_path=selected_path
				else:print('You can only navigate into folders.');time.sleep(2)
			else:print('Invalid option. Please try again.');time.sleep(2)
		except ValueError:print('Invalid input. Please enter a number.');time.sleep(2)

def convert_file_type(current_path,items):
	try:
		file_index=int(input('Enter the file number to convert its type: '))-3
		if 0<=file_index<len(items):
			selected_item=items[file_index]
			selected_path=os.path.join(current_path,selected_item)
			if os.path.isfile(selected_path):
				new_extension=input(f"Enter the new file type for '{selected_item}' (e.g., 'html'): ").strip().lstrip('.')
				if new_extension:
					base_name,_=os.path.splitext(selected_item)
					new_file_name=f"{base_name}.{new_extension}"
					new_path=os.path.join(current_path,new_file_name)
					os.rename(selected_path,new_path)
					print(f"File '{selected_item}' successfully converted to '{new_file_name}'.")
				else:print('Invalid file type entered. Conversion canceled.')
			else:print('The selected item is not a file. Conversion canceled.')
		else:print('Invalid file number. Please try again.')
	except ValueError:print('Invalid input. Please enter a valid number.')
	except Exception as e:print(f"An error occurred during conversion: {e}")
	time.sleep(2)

def main_menu():
	current_path=os.getcwd()
	while True:
		os.system('cls')
		print('\n*** File Management System ***\n')
		print('1. Create')
		print('2. Delete')
		print('3. Rename')
		print('4. Copy')
		print('5. Move')
		print('6. List View')
		print('7. Search')
		print('8. View Properties')
		print('9. Sorting')
		print('10. Open')
		print('11. Duplicate Files Finder')
		print('12. File Type Conversion')
		print('13. Exit')
		try:
			choice=int(input('\nEnter the option number: '))
			if choice==1:
				create_file_or_folder()
			elif choice==2:
				delete_file_or_folder()
			elif choice==3:
				rename_file_or_folder()
			elif choice==4:
				copy_file_or_folder(current_path)
			elif choice==5:
				browse_and_move_items(current_path)
			elif choice==6:
				browse_and_list_items(current_path)
			elif choice==7:
				browse_and_search_items(current_path)
			elif choice==8:
				view_properties(current_path)
			elif choice==9:
				sorting(current_path)
			elif choice==10:
				open_files(current_path)
			elif choice==11:
				find_duplicates(current_path)
			elif choice==12:
				convert_file_type_run(current_path)
			elif choice==13:
				print('\nThanks for using File Management System. Exiting.')
				break
			else:print('Invalid option. Please try again.')
		except ValueError:print('Invalid input. Please enter a number.')
if __name__=='__main__':main_menu()