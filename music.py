from auto.capabilities import list_caps, acquire, release

buzz = acquire("Buzzer")


# Place your music notes inside the strings below, create more lines as needed
def coconut_mall():
  mall1 = '!T264 MS CDD+ ML E R8 MS DD+ E8 F'
  mall2 = 'T264 MS O5 CDCDC ML O4 L6 T274 B-AGF r8'
  mallend2 = 'T264 MS L4 O5 CFD L6 T274 O4 B-AGF r2'
  mall3 = 'T264 L4 ML O5 CFDC O4 B- L6 T274 AB-B> L4 T264 MS O5 C D'
  mall4 = 'T264 L8 D L4 MS FF ML A8. G8 R8 F'

  buzz.play(mall1)
  buzz.play(mall2)
  buzz.play(mall1)
  buzz.play(mallend2)
  buzz.play(mall1)
  buzz.play(mall2)
  buzz.play(mall3)
  buzz.play(mall4)

def ice_cream_man():
    part1 = "V10 T90 ML L16 O5 C#O4B MSA8 MLAB A E C# D E F# E C# E R32"
    part2 = "T90 ML L16 O4 AO4B O5MSC#8 C#8 ML O5C#O4BO4AB MSL8O5C# O4B8 B8"
    part3 = "T90 ML L16 O4 ABO5C# E8 F#EC# O4 AB O5 C# O4 A B G# A R8"
    part4 = "T90 ML L16 O5 D F#8 D MS F#8 MLF#8 D F#8 D "
    part5 = "T90 ML L16 O5 F#DF#G# MS A8A8 E8E8 C#8C#8 O4 B8"
    fs8 = "T90 ML L16 F#8 R8"
    buzz.play(part1)
    buzz.play(part2)
    buzz.play(part1)
    buzz.play(part3)
    buzz.play(part4)
    buzz.play(fs8)
    buzz.play(part4)
    buzz.play(part5)
    buzz.play(part3)

