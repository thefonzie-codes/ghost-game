class Camera:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.offset_x = 0
        self.offset_y = 0

    # Center camera on target - if target changes, camera will follow.
    def follow_target(self, target):
        target_center_x = target.x + target.width // 2
        target_center_y = target.y + target.height // 2

        self.offset_x = target_center_x - (self.width // (2 * target.pixel_size))
        self.offset_y = target_center_y - (self.height // (2 * target.pixel_size))
    
    def screen_coords_to_world_coords(self, target):
        return (target.x - self.offset_x, target.y - self.offset_y)