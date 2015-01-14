#!/usr/bin/env python
"""Random Point Generator is a small utility script that creates 
a number of points with random values based on a template string.
A template can be passed with the --template option. Characters
inside brackets are evaluted and replaced. For instance {Ri},{Ri} 
would produce two random integers separated by a comma. Inside 
brackets R = Random, i=integer, and f=floating point. If no
template is provided the default Well-Known Text template is used
(i.e. "POINT ({Rf} {Rf})")"""

import argparse
import random
import re

__author__ = "Sean Taylor Hutchison"
__website__ = "http://taylorhutchison.com"
__email__ = "seanthutchison@gmail.com"
__version__ = "1.0.0"
__license__ = "MIT"


def validate_range(random_range):
	if(random_range!=None):
		if(len(random_range)!=2):
			return None
		else:
			if(random_range[0]<random_range[1]):
				return random_range
			else:
				return None
	else:
		return None


def getPointSubstitionList(point_template):
	subs = re.findall('\{R[if]*}',point_template)
	return subs

def replaceFormatWithRandoms(point_template, point_templates, min, max):
	for t in point_templates:
		if(t=="{Ri}"):
			point_template = point_template.replace(t,str(random.randint(int(min),int(max))),1)
		if(t=="{Rf}"):
			point_template = point_template.replace(t,str(random.uniform(min,max)),1)
	return point_template

def main():
	DEFAULT_POINT_COUNT = 100
	DEFAULT_POINT_FORMAT = "POINT ({Ri} {Ri})"
	argumentParser = argparse.ArgumentParser(description=__doc__)
	argumentParser.add_argument("-t,--template", dest="template", type=str, required=False, help="Template of the generated point, such as \"{Ru},{Rd},{Rd},{Rd}\".")
	argumentParser.add_argument("-r,--range", dest="range", nargs=2,type=float, required=False, help="Two numbers (integer or floating point) given as Min Max so that random numbers are calculated inclusively.")
	argumentParser.add_argument("-c,--count", dest="count", type=int, required=False, help="Number of points.")

	args = argumentParser.parse_args()

	point_template = args.template or DEFAULT_POINT_FORMAT
	point_templates = getPointSubstitionList(point_template)

	random_range = validate_range(args.range) or [0,100]
	number_of_points = args.count or DEFAULT_POINT_COUNT

	random_points = []
	for _ in range(0,number_of_points):
		random_points.append(replaceFormatWithRandoms(point_template,point_templates,random_range[0],random_range[1]))

	for p in random_points:
		print(p)

if __name__ == "__main__":
	main()