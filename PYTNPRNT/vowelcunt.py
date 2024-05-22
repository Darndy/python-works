vowels= ['a','e','i','o','u']
def main():
     while True:
            n = vowel_count()
            print(n)
               
      
def vowel_count():
      count = 0
      phrase =input("enter your phrase here \n").lower()
      for char in phrase:
            if char in vowels:
                  count += 1
      return count
main()


      

