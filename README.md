# DNA-Sequence-Manipulator

 This is a program that receives a DNA sequence as a string input, and performs actions such as DNA validation, transcription, reverse, compliment, translation, reading frame prediction on the given sequence.

 To use: Run main.py, and follow the command line prompts.

 Requires Python version 3.10 and term color module installed.

## Example:

### *Input*: 
 
 cgaaggcccagcagtacttttacctcaaaagaacgtttcctaaatatgtgatcattgaga

### *Output*: 

 ====================================================================================

 Original Sequence: gccatgggctatagttaccatcagactgcttcctcttattggtaagcaca

 Reverse: ACACGAATGGTTATTCTCCTTCGTCAGACTACCATTGATATCGGGTACCG

 Complement: CGGTACCCGATATCAATGGTAGTCTGACGAAGGAGAATAACCATTCGTGT

 Reverse Complement: TGTGCTTACCAATAAGAGGAAGCAGTCTGATGGTAACTATAGCCCATGGC

 Transcribed RNA Sequence: GCCAUGGGCUAUAGUUACCAUCAGACUGCUUCCUCUUAUUGGUAAGCACA

 Reverse Amino Acid Sequence:  AMGYSYHQTASSYW_A CA

 Reading Frame:  GCC <span style="color:green">ATG</span> GGC TAT AGT TAC CAT CAG ACT GCT TCC TCT TAT TGG <span style="color:red">TAA</span> GCA CA

 ====================================================================================

