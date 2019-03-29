from os import path
import re
from fluent_tui.utils import journal_writer

class Display():
    """ lists commands used to control the rendering of your model and mesh in the graphical window."""
    def __init__(self):
        self.base = '/display/'
        self.commands = []
        self.picture_extension = '.ps'
        self.xy = [0,0]
    
    def write_journal(self, flush=True, **kwargs):
        journal_writer(self.commands, **kwargs)
        if flush:
            self.commands = []
        
    def add(self,*commands):
        self.commands.append(self.base + ' '.join([str(cmd) for cmd in commands]) + '\n')
    
    def add_raw(self,commands):
        if not isinstance(commands,list):
            commands = [commands]
        self.commands.append('\n'.join([str(cmd) for cmd in commands]) + '\n')
        
    def add_custom_vector():
        """Adds new custom vector definition."""

    def annotate():
        """Adds annotation text to a graphics window. It will prompt you for a string to use as the annotation text, and then a dialog box will prompt you to select a screen location using the mouse_probe button on your mouse."""

    def clear_annotations():
        """Removes all annotations and attachment lines from the active graphics window."""

    def close_window():
        """Closes a graphics window."""

    def contour():
        """Prompts for a scalar field and minimum and maximum values, and then displays a contour plot."""

    def display_custom_vector():
        """Displays custom vector."""

    class flamelet_data():
        """Displays flamelet data."""

        def carpet_plot():
            """Enables or disables display of carpet plot of a property."""

        def draw_number_box():
            """Enables or disables display of the numbers box."""

        def plot_1d_slice():
            """Enables or disables plot of the 1D_slice."""

        def write_to_file():
            """Enables or disables writing the 1D_slice to file instead of plot."""

    def graphics_window_layout():
        """Arranges the graphics window layout."""

    def hsf_file():
        """Loads an HSF file for viewing."""

    def mesh():
        """Displays the entire mesh. For 3D, you will be asked to confirm that you really want to draw the entire mesh (not just the mesh_outline)."""

    def mesh_outline():
        """Displays the mesh boundaries."""

    def mesh_partition_boundary():
        """Displays mesh partition boundaries."""

    def multigrid_coarsening():
        """Displays a coarse mesh level from the last multigrid coarsening."""

    def objects(self,**kwargs):
        """Enters the graphics objects menu."""
        self.base = '/display/object/'

        def add_to_graphics(object):
            """Adds a contour, vector, pathline, particle track, scene, or mesh plot to the existing content in the graphics window."""
            self.add('add-to-graphics/'+object)

        def copy():
            """Copies an existing contour, vector, pathline, particle track, scene, mesh, or XY plot definition."""

        def create():
            """Creates a contour, vector, pathline, particle track, scene, mesh, or XY plot definition."""

        def delete():
            """Deletes a contour, vector, pathline, particle track, scene, mesh, or XY plot definition."""

        def display(object):
            """Displays a contour, vector, pathline, particle track, scene, mesh, or XY plot in the graphic windows replacing the existing content."""
            self.add('display/'+object)
        def edit():
            """Edits a contour, vector, pathline, particle track, scene, or mesh plot definition."""
            
        # Switch Case Setup    
        switch = {
            'add_to_graphics':add_to_graphics,
            'copy':copy,
            'create':create,
            'delete':delete,
            'display':display,
            'edit':edit,
        }
    
        # Disperse kwargs to functions
        for key,value in kwargs.items():
            switch[key](value)
            
        # Reset self.base
        self.base = '/display/'

    def open_window():
        """Opens a graphics window."""

    def particle_tracks():
        """Enters the particle tracks menu."""

        def particle_tracks():
            """Calculates and displays particle tracks from defined injections."""

        def plot_write_xy_plot():
            """Plots or writes an XY plot of particle tracks."""

    def path_lines():
        """Enters the pathlines menu."""

        def path_lines():
            """Displays pathlines from a surface."""

        def plot_write_xy_plot():
            """Plots or writes an XY plot of pathlines."""

        def write_to_files():
            """Writes pathlines to a file."""

    def pdf_data():
        """Enters the PDF data menu."""

        def carpet_plot():
            """Enables or disables the display of a carpet plot of a property."""

        def draw_number_box():
            """Enables or disables the display of the numbers box."""

        def plot_1d_slice():
            """Enables or disables a plot of the 1D_slice."""

        def write_to_file():
            """Enables or disables writing the 1D_slice to file instead of plot."""

    def reacting_channel_curves():
        """Plots the reacting channel variables."""

    def profile():
        """Displays profiles of a flow variable."""

    def re_render():
        """Re_renders the last contour, profile, or vector plot with updated surfaces, meshed, lights, colormap, rendering options, and so on, without recalculating the contour data."""

    def re_scale():
        """Re_renders the last contour, profile, or vector plot with updated scale, surfaces, meshes, lights, colormap, rendering options, and so on, but without recalculating the field data."""

    def save_picture(self,filename=None,overwrite=True):
        """Generates a “hardcopy" of the active window."""
        
        if filename is None:
            filename = path.join(path.expanduser('~'),'Desktop','image.ps')
        
        if ((filename[0]!='"') or (filename[0]!="'")) and (' ' in filename):
            filename = '"'+filename+'"'
            
        if overwrite:
            ow = 'y'
        else:
            ow = 'n'
    
        root,ext = path.splitext(filename)
        self.picture_options(driver=ext)
        filename = root+self.picture_extension
        self.add('save-picture/', filename, ow)
        
    def picture_options(self, **kwargs):
        """Enters the save_picture options menu."""
        self.base = '/display/set/picture/'
        
        def set_color_mode(mode):
            """Enters the hardcopy or save_picture color mode menu."""
            
            if 'color' in mode:
                """Plots hardcopies in color."""
                self.add('color-mode/ color')
                
            elif ('grey' in mode) or ('gray' in mode):
                """Converts color to grayscale for hardcopy."""
                self.add('color-mode/ grayscale')

            elif 'list' in mode:
                """Displays the current hardcopy color mode."""
                self.add('color-mode/ list')

            elif ('mono' in mode) or ('bw' in mode):
                """Converts color to monochrome (black and white) for hardcopy."""
                self.add('color-mode/ mono_chrome')
            
        def set_dpi(value):
            """Sets the resolution for EPS and Postscript files; specifies the resolution in dots per inch (DPI) instead of setting the width and height."""
            self.add('dpi/', value)
            
        def set_driver(ext='ps'):
            """Enters the set hardcopy driver menu."""
            ext = ext.strip('.')
            options = {
                'eps':'eps',
                'ppm':'ppm',
                'hsf':'hsf',
                'png':'png',
                'tiff':'tiff',
                'tif':'tiff',
                'jpg':'jpeg',
                'vrml':'vrml',
                'ps':'post-script',
            }
            
            if ext in options.keys():
                if (re.search('driver/'+options[ext],' '.join(self.commands)) is None):
                    self.add('driver/'+options[ext])
                self.picture_extension = '.'+ext
            else:
                print('Can not use extension "'+ext+'". Defaulting to "ps", please use one of the following next time:')
                print(options.keys())
                if (re.search('driver/png',' '.join(self.commands)) is None):
                    self.add('driver/png')
                self.picture_extension = '.png'
                
            def dump_window():
                """Sets the command used to dump the graphics window to a file."""

            def options():
                """Sets the hardcopy options. Available options are: “no gamma correction", disables gamma correction of colors; “pen speed = f", where f is a real number in [0,1]; “physical size = (width, height)", where width and height are the actual measurements of the printable area of the page in centimeters; “subscreen = (left, right, bottom, top)", where left, right, bottom, and top are numbers in [_1,1] describing a subwindow on the page in which to place the hardcopy. The options may be combined by separating them with commas. The pen speed option is only meaningful to the HPGL driver."""

            def post_format():
                """Enters the PostScript driver format menu."""

                def fast_raster():
                    """Enables a raster file that may be larger than the standard raster file, but will print much more quickly."""

                def raster():
                    """Enables the standard raster file."""

                def rle_raster():
                    """Enables a run_length encoded raster file that will be about the same size as the standard raster file, but will print slightly more quickly."""

                def vector():
                    """Enables the standard vector file."""

        def invert_background():
            """Exchanges foreground or background colors for hardcopy."""

        def set_landscape(value='y'):
            """Plots hardcopies in landscape or portrait orientation."""
            if isinstance(value,bool):
                if value:
                    value = 'y'
                else:
                    value = 'n'
            self.add('landscape '+value)

        def set_preview():
            """Applies the settings of the color_mode, invert_background, and landscape options to the currently active graphics window to preview the appearance of printed hardcopies."""

        def use_window_resolution(value):
            """Disables or enables the use of the current graphics window resolution when saving an image of the graphics window. If disabled, the resolution will be as specified for x_resolution and y_resolution."""
            if value:
                self.add('use-window-resolution/','y')
            else:
                self.add('use-window-resolution/','n')
                
        def set_x_resolution(value):
            """Sets the width of raster_formatted images in pixels (0 implies current window size)."""
            if (re.search('use-window-resolution',' '.join(self.commands)) is None):
                use_window_resolution(False)
                
            self.add('x-resolution/',value)
            self.xy[0] = value
            if (0 not in self.xy):
                if (self.xy[0]>self.xy[1]):
                    set_landscape('y')
                else:
                    set_landscape('n')
            
        def set_y_resolution(value):
            """Sets the height of raster_formatted images in pixels (0 implies current window size)."""
            if (re.search('use-window-resolution',' '.join(self.commands)) is None):
                use_window_resolution(False)
                
            self.add('y-resolution',value)
            self.xy[1] = value
            if (0 not in self.xy):
                if (self.xy[0]>self.xy[1]):
                    set_landscape('y')
                else:
                    set_landscape('n')
                
        # Switch Case Setup    
        switch = {
            'color_mode':set_color_mode,
            'dpi':set_dpi,
            'invert_background':invert_background,
            'landscape':set_landscape,
            'preview':set_preview,
            'use_window_resolution':use_window_resolution,
            'x':set_x_resolution,
            'y':set_y_resolution,
            'driver':set_driver,
        }
    
        # Disperse kwargs to functions
        for key,value in kwargs.items():
            switch[key](value)
            
        # Reset self.base
        self.base = '/display/'

    class set():
        """Enters the set menu to set display parameters."""
        #self.base = '/display/set/'
        
        def color_map():
            """Enters the color map menu, which contains names of predefined and user_defined (in the Colormap Editor panel) colormaps that can be selected. It prompts you for the name of the colormap to be used."""

        def colors():
            """Enters the color options menu."""

            def background():
                """Sets the background (window) color."""

            def color_by_type():
                """Determines whether to color meshes by type or by ID."""

            def color_scheme():
                """Sets the color scheme. You can choose to display your graphics in the classic ANSYS Fluent color scheme, or you can use the default Workbench color scheme."""

            def axis_faces():
                """Sets the color of axisymmetric faces."""

            def far_field_faces():
                """Sets the color of far field faces."""

            def free_surface_faces():
                """Sets the color of free_surface faces."""

            def foreground():
                """Sets the foreground (text and window frame) color."""

            def highlight_color():
                """Sets highlight color."""

            def inlet_faces():
                """Sets the color of inlet faces."""

            def interface_faces():
                """Sets the color of mesh interfaces."""

            def interior_faces():
                """Sets the color of interior faces."""

            def internal_faces():
                """Sets the color of internal interface faces."""

            def outlet_faces():
                """Sets the color of outlet faces."""

            def periodic_faces():
                """Sets the color of periodic faces."""

            def rans_les_interface_faces():
                """Sets the color of RANS or LES interface faces."""

            def symmetry_faces():
                """Sets the color of symmetric faces."""

            def traction_faces():
                """Sets the color of traction faces."""

            def wall_faces():
                """Sets the color of wall faces."""

            def list():
                """Lists available colors."""

            def reset_colors():
                """Resets individual mesh surface colors to the defaults."""

            def skip_label():
                """Sets the number of labels to be skipped in the colormap scale."""

            def surface():
                """Sets the color of surfaces."""

        def contours():
            """Enters the contour options menu."""

            def auto_range():
                """Enables or disables auto_computation of the contour range."""

            def clip_to_range():
                """Turns the clip to range option for filled contours on or off."""

            def coloring():
                """Specifies whether contours are displayed in bands or with smooth transitions. Note that you can only display smooth contours if node_values are enabled."""

            def filled_contours():
                """Turns the filled contours option on or off (deselects line_contours?)."""

            def global_range():
                """Turns the global range for contours on or off."""

            def line_contours():
                """Turns the line contours option on or off (deselects filled_contours?)."""

            def log_scale():
                """Specifies a decimal or logarithmic color scale for contours."""

            def n_contour():
                """Sets the number of contour levels."""

            def node_values():
                """Sets the option to use scalar field at nodes when computing the contours."""

            def render_mesh():
                """Determines whether or not to render the mesh on top of contours, vectors, and so on."""

            def surfaces():
                """Sets the surfaces on which contours are drawn. You can include a wildcard (*) within the surface names."""

        def element_shrink():
            """Sets shrinkage of both faces and cells. A value of zero indicates no shrinkage, while a value of one will shrink each face or cell to a point."""

        def filled_mesh():
            """Determines whether the meshes are drawn as wireframe or solid."""

        def mesh_level():
            """Sets coarse mesh level to be drawn."""

        def mesh_partitions():
            """Enables or disables option to draw mesh partition boundaries."""

        def mesh_surfaces():
            """Sets surface IDs to be drawn as meshes. You can include a wildcard (*) within the surface names."""

        def mesh_zones():
            """Sets zone IDs to be drawn as meshes."""

        def lights():
            """Enters the lights menu."""

            def headlight_on():
                """Turns the light that moves with the camera on or off."""

            def lighting_interpolation():
                """Sets lighting interpolation method."""

                def flat():
                    """Uses flat shading for meshes and polygons."""

                def gouraud():
                    """Uses Gouraud shading to calculate the color at each vertex of a polygon and interpolates it in the interior."""

                def phong():
                    """Uses Phong shading to interpolate the normals for each pixel of a polygon and computes a color at every pixel."""

            def lights_on():
                """Turns all active lighting on or off."""

            def set_ambient_color():
                """Sets the ambient color for the scene. The ambient color is the background light color in a scene."""

            def set_light():
                """Adds or modifies a directional, colored light."""

        def line_weight():
            """Sets the line_weight factor for the window."""

        def marker_size():
            """Sets the size of markers used to represent points."""

        def marker_symbol():
            """Sets the type of markers used to represent points."""

        def mesh_display_configuration():
            """Changes the default mesh display. If set to meshing, it draws the mesh on edges and faces of the outline surfaces, colored by their zone ID with lighting enabled. If set to solution, it draws the mesh on edges and faces of the outline surfaces, colored by their zone type with lighting enabled. If set to post_processing, it draws the object outline with lighting disabled. If set to classic, it draws the mesh on all edges of the outline surfaces.
            Note:  This only applies for 3D cases."""

        def mirror_zones():
            """Sets the zones about which the domain is mirrored (symmetry planes)."""

        def mouse_buttons():
            """Prompts you to select a function for each of the mouse buttons."""

        def mouse_probes():
            """Enables or disables mouse probe capability."""

        def n_stream_func():
            """Sets number of iterations used in computing stream function."""

        def nodewt_based_interp():
            """Disables or enables the use of node weights for node_based gradients in postprocessing."""

        def overlays():
            """Enables or disables overlays."""

        def particle_tracks():
            """Enters the particle_tracks menu to set parameters for display of particle tracks."""

            def arrow_scale():
                """Sets the scale factor for arrows drawn on particle tracks."""

            def arrow_space():
                """Sets the spacing factor for arrows drawn on particle tracks."""

            def coarsen_factor():
                """Sets the coarsening factor for particle tracks."""

            def display():
                """Determines whether particle tracks shall be displayed or only tracked."""

            def filter_settings():
                """Sets filter for particle display."""

                def enable_filtering():
                    """Specifies whether particle display is filtered."""

                def filter_variable():
                    """Selects a variable used for filtering of particles."""

                def inside():
                    """Specifies whether filter variable must be inside min or max to be displayed (else outside min or max)."""

                def maximum():
                    """Specifies the upper bound for the filter variable."""

                def minimum():
                    """Specifies the lower bound for the filter variable."""

            def history_filename():
                """Specifies the name of the particle history file."""

            def line_width():
                """Sets the width for particle track."""

            def marker_size():
                """Sets the size of markers used to represent particle tracks."""

            def particle_skip():
                """Specifies how many particle tracks should be displayed."""

            def radius():
                """Sets the radius for particle track (ribbon or cylinder only) cross_section."""

            def report_to():
                """Specifies the destination for the report (console, file, none)."""

            def report_type():
                """Sets the report type for particle tracks."""

            def report_variables():
                """Sets the report variables."""

            def report_default_variables():
                """Sets the report variables to default."""

            def sphere_attrib():
                """Specifies the size and number of slices to be used in drawing spheres."""

            def sphere_settings():
                """Sets filter for particle display."""

                def auto_range():
                    """Specifies whether displayed spheres should include auto range of variable to size spheres."""

                def diameter():
                    """Diameter of the spheres when vary_diameter is disabled."""

                def maximum():
                    """Sets the maximum value of the sphere to be displayed."""

                def minimum():
                    """Sets the minimum value of the sphere to be displayed."""

                def scale_factor():
                    """Specifies a scale factor to enlarge or reduce the size of spheres."""

                def size_variable():
                    """Selects a particle variable to size the spheres."""

                def smooth_parameter():
                    """Specifies number of slices to be used in drawing spheres."""

                def vary_diameter():
                    """Specifies whether the spheres can vary with another variable."""

            def style():
                """Sets the display style for particle track (line or ribbon or cylinder or sphere)."""

            def track_single_particle_stream():
                """Specifies the stream ID to be tracked."""

            def twist_factor():
                """Sets the scale factor for twisting (ribbons only)."""

            def vector_settings():
                """Sets vector specific input."""

                def color_variable():
                    """Specifies whether the vectors should be colored by variable specified in  or display or particle_track or particle_track (if false use a constant color)."""

                def constant_color():
                    """Specifies a constant color for the vectors."""

                def length_to_head_ratio():
                    """Specifies ratio of length to head for vectors and length to diameter for cylinders."""

                def length_variable():
                    """Specifies whether the displayed vectors have length varying with another variable."""

                def scale_factor():
                    """Specifies a scale factor to enlarge or reduce the length of vectors."""

                def style():
                    """Enables and sets the display style for particle vectors (none or vector or centered_vector or centered_cylinder)."""

                def vector_length():
                    """Specifies the length of constant vectors."""

                def vector_length_variable():
                    """Selects a particle variable to specify the length of vectors."""

                def vector_variable():
                    """Selects a particle vector function to specify vector direction."""

        def path_lines():
            """Sets parameters for display of pathlines."""

            def arrow_scale():
                """Sets the scale factor for arrows drawn on pathlines."""

            def arrow_space():
                """Sets the spacing factor for arrows drawn on pathlines."""

            def display_steps():
                """Sets the display stepping for pathlines."""

            def error_control():
                """Sets error control during pathline computation."""

            def line_width():
                """Sets the width for pathlines."""

            def marker_size():
                """Sets the marker size for particle drawing."""

            def maximum_error():
                """Sets the maximum error allowed while computing the pathlines."""

            def maximum_steps():
                """Sets the maximum number of steps to take for pathlines."""

            def radius():
                """Sets the radius for pathline (ribbons or cylinder only) cross_section."""

            def relative_pathlines():
                """Enables or disables the tracking of pathlines in a relative coordinate system."""

            def reverse():
                """Sets direction of path tracking."""

            def sphere_attrib():
                """Specifies the size and number of slices to be used in drawing spheres."""

            def step_size():
                """Sets the step length between particle positions for pathlines."""

            def style():
                """Selects the pathline style (line, point, ribbon, triangle, cylinder)."""

            def time_step():
                """Sets the time step between particle positions for pathlines."""

            def track_in_phase():
                """Selects the phase in which particle pathlines will be computed (Multiphase Eulerian Model only)."""

            def twist_factor():
                """Sets the scale factor for twisting (ribbons only)."""

        def periodic_repeats():
            """Sets number of periodic repetitions."""

        def proximity_zones():
            """Sets zones to be used for boundary cell distance and boundary proximity."""

        def render_mesh():
            """Enables or disables rendering the mesh on top of contours, vectors, and so on."""

        def rendering_options():
            """Enters the rendering options menu, which contains the commands that allow you to set options that determine how the scene is rendered."""

            def animation_option():
                """Uses of wireframe or all during animation."""

            def auto_spin():
                """Enables or disables mouse view rotations to continue to spin the display after the button is released."""

            def color_map_alignment():
                """Sets the color bar alignment."""

            def device_info():
                """Prints out information about your graphics driver."""

            def double_buffering():
                """Enables or disables double buffering. Double buffering dramatically reduces screen flicker during graphics updates. If your display hardware does not support double buffering and you turn this option on, double buffering will be done in software. Software double buffering uses extra memory."""

            def driver():
                """Changes the current graphics driver."""

                def gl():
                    """IRIS GL"""

                def null():
                    """No graphics driver."""

                def opengl():
                    """OpenGL"""

                def pex():
                    """X11 PEX"""

                def hbx():
                    """HP Starbase"""

                def x11():
                    """X11"""

                def xgl():
                    """Sun XGL"""

                def msw():
                    """Microsoft Windows"""

            def face_displacement():
                """Sets face displacement value in Z_buffer units along the Camera Z_axis."""

            def hidden_line_method():
                """Specifies the method to perform hidden line rendering. This command will appear only when hidden_lines? is true."""

                def normal_hlr_algorithm():
                    """Normal hidden lines algorithm. This is the default."""

                def mesh_dislay_hlr():
                    """For removing hidden lines for surfaces that are very close together. Use this if normal_hlr_algorithm is not working. This will only work for meshes."""

            def hidden_lines():
                """Turns hidden line removal on or off."""

            def hidden_surfaces():
                """Turns hidden surface removal on or off."""

            def hidden_surface_method():
                """Allows you to choose from among the hidden surface removal methods that ANSYS Fluent supports. These options (listed below) are display hardware dependent."""

                def hardware_z_buffer():
                    """Is the fastest method if your hardware supports it. The accuracy and speed of this method is hardware dependent."""

                def painters():
                    """Will show less edge_aliasing effects than hardware_z_ buffer. This method is often used instead of software_z_buffer when memory is limited."""

                def software_z_buffer():
                    """Is the fastest of the accurate software methods available (especially for complex scenes), but it is memory intensive."""

                def z_sort_only():
                    """Is a fast software method, but it is not as accurate as software_z_buffer."""

            def outer_face_cull():
                """Enables or disables discarding outer faces during display."""

            def set_rendering_options():
                """Sets the rendering options."""

            def surface_edge_visibility():
                """Sets edge visibility flags for surfaces."""

        def reset_graphics():
            """Resets the graphics system."""

        def title():
            """Sets problem title. This text only appears if the display or set or windows or text or company? text command is set to yes and if Titles is enabled in the Display Options dialog box."""

            def left_top():
                """Sets the title text for left top in title segment."""

            def left_bottom():
                """Sets the title text for left bottom in title segment."""

            def right_top():
                """Sets the title text for right top in title segment."""

            def right_middle():
                """Sets the title text for right middle in title segment."""

            def right_bottom():
                """Sets the title text for right bottom in title segment."""

        def velocity_vectors():
            """Enters the menu to set parameters for display of velocity vectors."""

            def auto_scale():
                """Auto_scales all vectors so that vector overlap is minimal."""

            def color():
                """Sets the color of all velocity vectors to the color specified. The color scale is ignored. This is useful when overlaying a vector plot over a contour plot."""

            def color_levels():
                """Sets the number of colors used from the colormap."""

            def component_x():
                """Sets the option to use only the  component of the velocity vectors during display."""

            def component_y():
                """Sets the option to use only the  component of the velocity vectors during display."""

            def component_z():
                """Sets the option to use only the  component of the velocity vectors during display."""

            def constant_length():
                """Sets the option to draw velocity vectors of constant length. This shows only the direction of the velocity vectors."""

            def global_range():
                """Turns global range for vectors on or off."""

            def in_plane():
                """Toggles the display of velocity vector components in the plane of the surface selected for display."""

            def log_scale():
                """Toggles whether color scale is logarithmic or linear."""

            def node_values():
                """Enables or disables the plotting of node values. Cell values will be plotted if "no"."""

            def relative():
                """Toggles the display of relative velocity vectors."""

            def render_mesh():
                """Enables or disables rendering the mesh on top of contours, vectors, and so on."""

            def scale():
                """Sets the value by which the vector length will be scaled."""

            def scale_head():
                """Sets the value by which the vector head will be scaled."""

            def style():
                """Specifies the vector style that will be used when the vectors are displayed. You can choose from: 3d arrow, 3d arrowhead, cone, filled_arrow, arrow, harpoon, or headless."""

            def surfaces():
                """Sets surfaces on which vectors are drawn. You can include a wildcard (*) within the surface names."""

        def windows():
            """Enters the windows option menu, which contains commands that allow you to customize the relative positions of subwindows inside the active graphics window."""

            def aspect_ratio():
                """Sets the aspect ratio of the active window."""

            def axes():
                """Enters the axes window options menu (3D only)."""

                def border():
                    """Sets whether to draw a border around the axes window."""

                def bottom():
                    """Sets the bottom boundary of the axes window."""

                def clear():
                    """Sets the transparency of the axes window."""

                def logo():
                    """Enables or disables visibility of the logo in graphics window."""

                def logo_color():
                    """Sets logo color to white or black in graphics window."""

                def right():
                    """Sets the right boundary of the axes window."""

                def visible():
                    """Turns axes visibility on or off."""

            def main():
                """Enters the main view window options menu."""

                def border():
                    """Sets whether or not to draw a border around the main viewing window."""

                def bottom():
                    """Sets the bottom boundary of the main viewing window."""

                def left():
                    """Sets the left boundary of the main viewing window."""

                def right():
                    """Sets the right boundary of the main viewing window."""

                def top():
                    """Sets the top boundary of the main viewing window."""

                def visible():
                    """Turns visibility of the main viewing window on or off."""

            def ruler():
                """Turns the ruler on or off. Note that if you are running Fluent in 3D, then the view must be set to orthographic."""

            def scale():
                """Enters the color scale window options menu."""

                def alignment():
                    """Sets the colormap position to the bottom, left, top, or right."""

                def border():
                    """Sets whether or not to draw a border around the color scale window."""

                def bottom():
                    """Sets the bottom boundary of the color scale window."""

                def clear():
                    """Sets the transparency of the scale window."""

                def format():
                    """Sets the number format of the color scale window. (for example, %0.2e)"""

                def font_size():
                    """Sets the font size of the color scale window."""

                def left():
                    """Sets the left boundary of the color scale window."""

                def margin():
                    """Sets the margin of the color scale window."""

                def right():
                    """Sets the right boundary of the color scale window."""

                def top():
                    """Sets the top boundary of the color scale window."""

                def visible():
                    """Turns visibility of the color scale window on or off."""

            def text():
                """Enters the text window options menu."""

                def application():
                    """Shows or hides the application name in the picture."""

                def border():
                    """Sets whether or not to draw a border around the text window."""

                def bottom():
                    """Sets the bottom boundary of the text window."""

                def clear():
                    """Enables or disables text window transparency."""

                def company():
                    """Enables or disables the display of your company name or other text defined using the display or set or titles or  text command. The text appears in the title box. See Controlling the Titles, Axes, Ruler, Logo, and Colormap in the Fluent User's Guide for additional information."""

                def date():
                    """Shows or hides the date in the picture."""

                def left():
                    """Sets the left boundary of the text window."""

                def right():
                    """Sets the right boundary of the text window."""

                def top():
                    """Sets the top boundary of the text window."""

                def visible():
                    """Turns visibility of the text window on or off."""

            def video():
                """Enters the video window options menu."""

                def background():
                    """Sets the background color of the graphics window. The color is specified as a string of three comma_separated numbers between 0 and 1, representing red, green, and blue. For example, to change the background from black (default) to gray, you would enter ".5,.5,.5" after selecting the background command."""

                def color_filter():
                    """Sets the video color filter. For example, to change the color filter from its default setting to PAL video with a saturation of 80% and a brightness of 90%, you would enter "video=pal,sat=.8,gain=.9" after selecting the color_filter command."""

                def foreground():
                    """Sets the foreground (text) color of the graphics window. The color is specified as a string of three comma_separated numbers between 0 and 1, representing red, green, and blue. For example, to change the foreground from white (default) to gray, you would enter ".5,.5,.5" after selecting the foreground command."""

                def on():
                    """Enables or disables video picture settings."""

                def pixel_size():
                    """Sets the window size in pixels."""

            def xy():
                """Enters the XY plot window options menu."""

                def border():
                    """Sets whether or not to draw a border around the XY plot window."""

                def bottom():
                    """Sets the bottom boundary of the XY plot window."""

                def left():
                    """Sets the left boundary of the XY plot window."""

                def right():
                    """Sets the right boundary of the XY plot window."""

                def top():
                    """Sets the top boundary of the XY plot window."""

                def visible():
                    """Turns visibility of the XY plot window on or off."""

        def zero_angle_dir():
            """Sets the vector having zero angular coordinates."""

    def set_list_tree_separator():
        """Sets the separator character for list tree."""

    def set_window():
        """Sets a graphics window to be the active window."""

    def surface():
        """Enters the data surface_manipulation menu. For a description of the items in this menu, see surface/."""

    def surface_cells():
        """Draws the cells on the specified surfaces. You can include a wildcard (*) within the surface names."""

    def surface_mesh():
        """Draws the mesh defined by the specified surfaces. You can include a wildcard (*) within the surface names."""

    def update_scene():
        """Enters the scene options menu."""

        def delete():
            """Deletes selected geometries."""

        def display():
            """Displays selected geometries."""

        def draw_frame():
            """Enables or disables drawing the bounding frame."""

        def iso_sweep():
            """Changes iso_sweep values."""

        def overlays():
            """Enables or disables the overlays option."""

        def pathline():
            """Changes pathline attributes."""

        def select_geometry():
            """Selects geometry to be updated."""

        def set_frame():
            """Changes frame options."""

        def time():
            """Changes time_step value."""

        def transform():
            """Applies transformation matrix on selected geometries."""

    def vector():
        """Displays vectors of a space vector variable."""

    def velocity_vector():
        """Prompts for a scalar field by which to color the vectors, the minimum and maximum values, and the scale factor, and then draws the velocity vectors."""

    def view():
        """Enters the view manipulation menu. For a description of the items in this menu, see views/"""

    def zone_mesh():
        """Draws the mesh defined by specified face zones. Zone names can be indicated using wildcards (*)."""