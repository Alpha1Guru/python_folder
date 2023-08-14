import re
def count_smileys(valid_smiley_re_pattern: str, faces: list ):
    faces_combined = "_".join(faces)
    num_of_smileys = len(re.findall(valid_smiley_re_pattern, faces_combined))
    return num_of_smileys
if __name__ == "__main__":
    smiley_regex = r"[:;]([~-])?[)D]"
    print(count_smileys(smiley_regex, [':)', ';(', ';}', ':-D']))