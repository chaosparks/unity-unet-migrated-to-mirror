import os
import Helper.FileUtil

def get_UNet_ref_Config(file):
    name_to_guid = {}
    lines = Helper.FileUtil.read_lines_from_file(file)
    for line in lines:
        index = line.find('=>')
        name = line[:index].strip()
        guid = line[index+len('=>'):].strip()
        name_to_guid[name] = guid

        if name == 'UnityEngine.Networking.NetworkTransform':
            name_to_guid['UnityEngine.Networking.NetworkTransformHybrid'] = guid

    return name_to_guid

def get_UNet2Mirror_mapping(Mirror_folder, unet_name_2_guid):
    guid_mapping = {}
    files = Helper.FileUtil.list_files_in_folder(Mirror_folder, None, '.cs')
    files_dict = {}
    for file in files:
        basename = os.path.basename(file)
        file_name, file_extension = os.path.splitext(basename)
        if not file_name in files_dict:
            files_dict[file_name] = []
        files_dict[file_name].append(file)

    for (name, old_ref) in unet_name_2_guid.items():
        pure_name = name[name.rfind('.')+1:]

        if pure_name in files_dict:
            if len( files_dict[pure_name] ) == 1:
                file = files_dict[pure_name][0]
                guid = Helper.FileUtil.read_meta_guid(file + '.meta')
                new_ref = '{fileID: 11500000, guid: ' + guid + ', type: 3}'                
                guid_mapping[old_ref] = new_ref
            else :
                print('> 1 files found for ' + pure_name)    
        else :
            print('could not find class: ' + pure_name)

    return guid_mapping

## correct the guid ref in .unity, .prefab, and .asset YAML file
def correct_guid_ref(folder, guid_mappings):

    files = Helper.FileUtil.list_files_in_folder_with_exts(folder, None, ['.unity', '.prefab', '.asset'])
    for file in files:
        
        lines = Helper.FileUtil.read_asset_as_YAML_lines(file)
        
        bChanged = False
        
        for i in range(len(lines)):
            line = lines[i]
            index = line.find(', guid: dc443db3e92b4983b9738c1131f555cb,')
            if index != -1:
                old_part = line[line.find('{'):line.rfind('}')+1]
                if old_part in guid_mappings:
                    line = line.replace(old_part, guid_mappings[old_part])
                    # print(old_part)
                    lines[i] = line
                    bChanged = True
                else :
                    print('can not find ' + old_part)

                

        if bChanged:
            print('correct guid ref: ' + file)
            Helper.FileUtil.save_lines_to_file(file, lines)    

# step 1
unet_ref_file = "path to UNet_ref.txt"
unet_name_2_guid = get_UNet_ref_Config(unet_ref_file)

# step2 
asset_folder = "you project asset folder"
mirror_folder = os.path.join(asset_folder, "Mirror")
guid_mapping = get_UNet2Mirror_mapping(mirror_folder, unet_name_2_guid)

# step 3
correct_guid_ref(asset_folder, guid_mapping)
