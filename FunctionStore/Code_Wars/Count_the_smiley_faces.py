def count_smileys(faces: list):
    
    def is_smiley_face(face: str):
        eyes = set([":",";"])
        nose = set(["~","-"])
        mouth = set([")","D"])
        if len(face) > 3 or len(face) < 2:
            return False
        if face[0] not in eyes:
            return False
        if face[-1] not in mouth:
            return False
        if len(face) == 3:
            if face[1] not in nose:
                return False
        return True
    num_of_smiley_faces = 0
    for face in faces:
        if  is_smiley_face(face):
            num_of_smiley_faces += 1
    return num_of_smiley_faces
print(count_smileys([':)', ';(', ';}', ':-D']))