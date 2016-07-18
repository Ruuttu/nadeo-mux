
import sys 

# This script takes an ordinary Ogg Vorbis audio file 
# and writes out a Nadeo "mux" file. These are compatible 
# with Trackmania 2, and some of their other games too.
# 
# The actual Nadeo implementation would choose a random 
# cipher key each time it's used. Presumably the correct 
# key can somehow be derived from the header. 


header = "".join( map( chr, [
	# ASCII codes
	78, 97, 100, 101, 111, 70, 105, 108, 101, 1, 30, 112, 198, 128
] ) )

key = "".join( map( chr, [
	# ASCII codes
	152, 228, 138, 52, 85, 159, 249, 202, 146, 104, 119, 180, 242, 150, 238, 129, 152, 201, 21, 104, 
	170, 63, 243, 149, 37, 208, 238, 105, 229, 45, 221, 3, 49, 201, 42, 208, 85, 126, 231, 43, 74, 
	161, 221, 210, 203, 90, 187, 6, 98, 147, 42, 161, 170, 252, 207, 86, 148, 67, 187, 165, 151, 
	180, 119, 12, 196, 39, 84, 161, 85, 249, 159, 172, 41, 134, 119, 75, 47, 105, 238, 24, 137, 78,
	168, 67, 85, 243, 63, 89, 82, 13, 238, 150, 94, 210, 221, 48, 19, 156, 81, 134, 170, 243, 126, 
	178, 164, 26, 221, 45, 188, 165, 187, 96, 38, 57, 162, 13, 85, 231, 126, 101, 73, 52, 187, 90, 
	121, 75, 119, 192, 76, 114, 69, 26, 170, 207, 252, 101, 146, 104, 119, 180, 242, 150, 238, 129, 
	152, 228, 138, 52, 85, 159, 249, 202, 146, 208, 238, 105, 229, 45, 221, 3, 49, 201, 21, 104, 
	170, 63, 243, 149, 37, 208, 221, 210, 203, 90, 187, 6, 98, 147, 42, 208, 85, 126, 231, 43, 74, 
	161, 221, 165, 151, 180, 119, 12, 196, 39, 84, 161, 170, 252, 207, 86, 148, 67, 187, 165, 47, 
	105, 238, 24, 137, 78, 168, 67, 85, 249, 159, 172, 41, 134, 119, 75, 47, 210, 221, 48, 19, 156, 
	81, 134, 170, 243, 63, 89, 82, 13, 238, 150, 94, 210, 187, 96, 38, 57, 162, 13, 85, 231, 126, 
	178, 164, 26, 221, 45, 188, 165, 187, 192, 76, 114, 69, 26, 170, 207, 252, 101, 73, 52, 187, 90, 
	121, 75, 119, 192
] ) )

# file paths from command-line
input_path = sys.argv[ 1 ]
output_path = sys.argv[ 2 ]

def xor_strings( s, key ):
	return "".join( map( chr, [
		ord( c ) ^ ord( key[ i % len(key) ] )
		for i, c in enumerate( s ) 
	] ) )


with open( output_path, 'wb' ) as output:
	# write additional header
	output.write( header )
	
	# write input file XOR'd
	with open( input_path, 'rb' ) as input:
		output.write( xor_strings( input.read(), key ) )
