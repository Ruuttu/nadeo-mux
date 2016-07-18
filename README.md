# nadeo-mux
Some of the games from Nadeo use an undocumented "mux" file format to store the custom songs added by players. This is apparently to avoid copyright issues, as plenty of these files will be floating around the world. 

Mux files hold a standard Ogg Vorbis file ciphered with XOR, prepended with a minimal header. 
That's all I know.

Currently included just the one python script you need to generate valid mux files. 
