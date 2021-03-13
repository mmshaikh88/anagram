#!/usr/bin/python

import itertools
import sys

__version__ = "1.0"

# -------------------------------------------------------------
def generate_anagram(word):
   """
   Generate all possible combination of the given string/word
   provided as parameter.
   @type word: [str]
   @rtype: [str]
   """

   return_list = []
   for i in range(0, len(word)+1):
      for subset in itertools.permutations(word, i):
         possible = ''
         for letter in subset:
           possible += letter
         if len(possible) == len(word):
            return_list.append(possible)
      
   return (return_list)

# -------------------------------------------------------------
def find_solution(word_list,word_set_dictionary):
   """
   Find the solution of the given string by exhaustively search the dictionary for all anagrams
   @type word: [str]
   @type word_set_dictionary: set[str]
   @rtype: set[str]
   """

   return_list = []
   for word in word_list:
     if word in word_set_dictionary:
        return_list.append(word)
   return(return_list)

# -------------------------------------------------------------
def verify_solution(word, word_set_dictionary):
   """
   Verify if the given solution is valid
   @type word: [str]
   @type word_set_dictionary: set[str]
   @rtype: True or False 
   """

   if word in word_set_dictionary:
      return (True)
   return (False)

# -------------------------------------------------------------
def load_dictionary(dictionary_file_path):
   """
   Loading english dictionary as word list
   @type dictionary_file_path: [str] 
   @rtype: set[str]
   """

   contents_list = []
   dictionary_file = open(dictionary_file_path, "r")
   contents = dictionary_file.read()
   contents_list = contents.split("\n")
   dictionary_file.close()
   return (set(contents_list))

# -------------------------------------------------------------
def main():
   """
   main section of the program
   """
   # loadding dictionary
   dictionary_set = load_dictionary("/usr/share/dict/words")

   # parameter as an input to generate the anagrams of the provided word
   anagrams_of = sys.argv[1]

   valid_invalid = verify_solution (anagrams_of, dictionary_set)
   if (valid_invalid): print ("====> " + anagrams_of + ": is valid string as far as dictionary word is concerned.")
   else: print ("====> " + anagrams_of + ": is invalid string as far as dictionary word is concerned")
   
# -------------------------------------------------------------
if __name__ == '__main__':
    main()

	
