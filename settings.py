level_map = [
'                           ',
'                           ',
'                           ',
' XX    XXX           XX    ',
' XX P                      ',
' XXXX       XX          XX ',
' XXXX     XX               ',
' XX   X  XXXX    XX  XX    ',
'      X  XXXX    XX  XXX   ',
'   XXXX  XXXXXX  XX  XXXX  XXXXXXXXXXXXXXXXX',
'XXXXXXX  XXXXXX  XX  XXXX  ',]

tile_size = 64 # for smaller screens change it to 32 // scaling not working yet // try scaling the blocks resolution down
screen_width = 1200 # for smaller screens change it to 600 // scaling not working yet
screen_height = len(level_map) * tile_size