from scipy.spatial import distance as dist

def mouthAspectRatio(mouth_points):
	# -------------------- Calculate the vertical line ---------------------
	ver_line_1 = dist.euclidean(mouth_points[2], mouth_points[10]) # 51, 59
	ver_line_2 = dist.euclidean(mouth_points[4], mouth_points[8]) # 53, 57

	# -------------------- Calculate the horizontal line ---------------------
	hor_line = dist.euclidean(mouth_points[0], mouth_points[6]) # 49, 55

	# -------------------- Calculate mouth ratio ---------------------
	mouth_ratio = (ver_line_1 + ver_line_2) / (2.0 * hor_line)
	
	return mouth_ratio
