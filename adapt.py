from fluent_tui.utils import journal_writer

class Adapt():
    """Commands related to Mesh Adaption"""
    def __init__(self):
        self.base = '/display/'
        self.commands = []
    
    def write_journal(self, flush=True, **kwargs):
        journal_writer(self.commands, **kwargs)
        if flush:
            self.commands = []
        
    def add(self,*commands):
        self.commands.append(self.base + ' '.join([str(cmd) for cmd in commands]) + '\n')
            
    def adapt_boundary_cells():
        """Adapts boundary cells based on a list of face zones."""

    def adapt_to_gradients():
        """Adapts mesh based on the gradient adaption function from the selected scalar quantity, the adaption threshold values, and the adaption limits."""

    def adapt_to_ref_lev():
        """Adapts cells based on refinement level differences."""

    def adapt_to_register():
        """Adapts mesh based on the selected adaption register and adaption limits."""

    def adapt_to_vol_change():
        """Adapts cells with large changes in cell volume."""

    def adapt_to_volume():
        """Adapts cells that are larger than a prescribed volume."""

    def adapt_to_y_plus():
        """Adapts cells associated with all wall zones based on the specified threshold values and adaption limits."""

    def adapt_to_y_plus_zones():
        """Adapts cells associated with specified wall zones based on the specified threshold values and adaption limits."""

    def anisotropic_adaption():
        """Anisotropically refines boundary layers. Cells will be split in the normal direction to the boundary face."""

    def adapt_to_y_star():
        """Adapts cells associated with all wall zones based on the specified threshold values and adaption limits."""

    def adapt_to_y_star_zones():
        """Adapts cells associated with specified wall zones based on the specified threshold values and adaption limits."""

    def change_register_type():
        """Toggles specified register between refinement and mask."""

    def combine_registers():
        """Combines the selected adaption and/or mask registers to create hybrid adaption functions."""

    def delete_register():
        """Deletes an adaption register."""

    def display_register():
        """Displays the cells marked for adaption in the specified adaption register."""

    def exchange_marks():
        """Exchanges the refinement and coarsening marks of the specified adaption register."""

    def fill_crsn_register():
        """Marks all cells to coarsen that are not marked for refinement in the adaption register."""

    def free_parents():
        """Deletes the hanging node face and cell hierarchy."""

    def free_registers():
        """Deletes all adaption and mask registers."""

    def invert_mask():
        """Changes all the active cells to inactive cells in a mask register."""

    def limit_register():
        """Applies the adaption volume limit to the selected register."""

    def list_registers():
        """Prints a list of the current registers including the ID, description (name), number of cells marked for refinement and coarsening, and the type."""

    def mark_boundary_cells():
        """Marks boundary cells based on a list of zones for refinement."""

    def mark_boundary_normal():
        """Marks cells for refinement based on target boundary normal distance."""

    def mark_boundary_vol():
        """Marks cells for refinement based on target boundary volume."""

    def mark_inout_circle():
        """Marks cells with centroids inside/outside the circular region defined by text or mouse input."""

    def mark_inout_cylinder():
        """Marks cells with centroids inside/outside the arbitrarily oriented cylindrical region defined by text or mouse input."""

    def mark_inout_hexahedron():
        """Marks cells with centroids inside/outside the hexahedral region defined by text or mouse input."""

    def mark_inout_iso_range():
        """Marks cells for refinement that have values inside/outside the specified isovalue ranges of the selected field variable."""

    def mark_inout_rectangle():
        """Marks cells with centroids inside/outside the rectangular region defined by text or mouse input."""

    def mark_inout_sphere():
        """Marks cells with centroids inside/outside the spherical region defined by text or mouse input."""

    def mark_percent_of_ncells():
        """Marks percent of total cell count for adaption based on gradient or isovalue."""

    def mark_with_gradients():
        """Marks cells for adaption based on flow gradients for refinement."""

    def mark_with_ref_lev():
        """Marks cells based on refinement level differences."""

    def mark_with_vol_change():
        """Marks cells with large changes in cell volume for refinement."""

    def mark_with_volume():
        """Marks cells for adaption based on maximum allowed volume."""

    def mark_with_y_plus():
        """Marks cells associated with all wall zones for refinement or coarsening based on the specified threshold values."""

    def mark_with_y_plus_zones():
        """Marks only cells associated with specified wall zones for refinement or coarsening based on the specified threshold values."""

    def mark_with_y_star():
        """Marks cells associated with all wall zones for refinement or coarsening based on the specified threshold values."""

    def mark_with_y_star_zones():
        """Marks only cells associated with specified wall zones for refinement or coarsening based on the specified threshold values."""

    def set_cell_zones():
        """Sets cell zones to be used for marking adaption."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_coarsen_mesh():
        """Turns on/off ability to coarsen mesh."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'
    def set_display_crsn_settings():
        """Prompts for coarsening wireframe visibility and shading, and the marker visibility, color, size and symbol."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'
        
    def set_display_node_flags():
        """Displays s color coded markers at the nodes specifying the node type."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_display_refn_settings():
        """Prompts for refinement wireframe visibility and shading, and the marker visibility, color, size and symbol."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_grad_vol_weight():
        """Controls the volume weighting for the gradient adaption function."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_init_node_flags():
        """Initializes the node flags."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_max_level_refine():
        """Sets maximum level of refine in the mesh."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_max_number_cells():
        """Limits the total number of cells produced by refinement."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_method():
        """Sets the adaption method."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_min_cell_volume():
        """Restricts the size of the cells considered for refinement."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_min_number_cells():
        """Sets limit on the number of cells in the mesh."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_reconstruct_geometry():
        """Enables/disables geometry_based adaption."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_refine_mesh():
        """Turns on/off mesh adaption by point addition."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_geometry_controls():
        """Sets geometry controls for wall zones."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'

    def set_verbosity():
        """Allows to set the adaption verbosity."""
        self.base = '/adapt/set/'
        #Reset self.base
        self.base='/adapt/'
            
    def smooth_mesh():
        """Smoothes the mesh using the quality_based, Laplacian, or skewness methods."""

    def swap_mesh_faces():
        """Swaps the faces of cells that do not meet the Delaunay circle test."""