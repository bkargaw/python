#
# Example file for working with loops
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  x = 0
  # while x <5:
  #     print x
  #     x += 1

  # for i in range(5,10):
  #     print i

  days =['mon', 'tue','wed', 'thur', 'fri', 'sat', 'sun']
  # for d in days:
  #     print d

  # for i in range(0,10):
  #     if (i > 5): break
  #     if (i % 2 != 0): continue
  #     print i

  # days =['mon', 'tue','wed', 'thur', 'fri', 'sat', 'sun']
  for i, d in enumerate(days):
      print i, d
if __name__ == "__main__":
  main()
