from scipy.spatial import distance as dist

def mouth_aspect_ratio(mouth_points):
	# compute the euclidean distances between the two sets of
	# vertical mouth landmarks (x, y)-coordinates
	ver_line_1 = dist.euclidean(mouth_points[2], mouth_points[10]) # 51, 59
	ver_line_2 = dist.euclidean(mouth_points[4], mouth_points[8]) # 53, 57

	# compute the euclidean distance between the horizontal
	# mouth landmark (x, y)-coordinates
	hor_line = dist.euclidean(mouth_points[0], mouth_points[6]) # 49, 55

	# compute the mouth aspect ratio
	mouth_ratio = (ver_line_1 + ver_line_2) / (2.0 * hor_line) 

	# return the mouth aspect ratio
	return mouth_ratio