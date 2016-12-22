
mygame = Target(
	script = "mygame.py",
	dest_base = "MyGame",
	icon_resurces=[(1, r"pico2d.ico")],
	other_resources = [(RT_MANIFEST, 1, (manifest_template % dict(prog = "mygame", level="asInvoker")).encode("utf-8")),
	resources = "animation_sheet.png\
				ConsolaMalun.ttf KPU_GROUND.png".split()
	
	if platform.architecture()[0] == '32bit':
		sdl_folder = './SLD2/X86/'
	else:
		sdl_folder = './SDL2/X64/'
		
	sdl_dlls = [sdl_folder + file_name for file_name in os.listdir(sdl_folder)]
	
	setup(name="name",
	      windows=[mygame],
	      data_files=[('.',resources), (sdl_folder,sdl_dlls)],
	      zipfile=None,
	      options={"py2exe": py2exe_options},
	      )

	
