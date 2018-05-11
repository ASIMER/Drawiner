class GeometryEngine:

    @staticmethod
    def dist_square(coords1, coords2):
        return (coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2

    @staticmethod
    def are_circles_intersected(coords1, size1, coords2, size2):
        if GeometryEngine.dist_square(coords1, coords2) < (size1 + size2)**2:
            return True
        else:
            return False
