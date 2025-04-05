

def mode_switch(map_editor, mode):

    match mode:
        case 1:
            map_editor.mode = 'digging'
        case 2:
            map_editor.mode = 'trench walls'
        case 3:
            map_editor.mode = 'furnishings'
        case 4:
            map_editor.mode = 'buildings'
        case 5:
            map_editor.mode = 'surface'