### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: 
      # card.value == 1
      return True
    else
    # missing colon
      return False
   
# should be def not dif and comma between parameters
  dif highest_card(self, card1 card2):
  # indentation error
  if card1.value > card2.value:
    return card
    # what is card? should it be return card1
  else:
    return card2
  

# indentation error?
def cards_total(self, cards):
  total
  # total is undefined, total = 0
  for card in cards:
    total += card.value
    # have to turn total into a string
    # total_str = str(total)
    return "You have a total of" + total
    # return ("You have a total of " + total_str) outside of for loop
  
```
