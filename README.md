
[ The specification of my calculator ]

1. It only receives POST request (by clicking on the button),
   and it has no respose to GET request.



[ The special rules of my calculator opration ]:

1. At the begining, when first enter this page:
   Display 0

2. When first click the button:
   (1) if it is the operator, give a error message and reset to 0, waiting for next click.
   (2) if it is the digit, the digit dispalys.

3. When click two continuos operators
   like '2' '-' '+'
   Give an error message and reset to 0, waiting for next click.

4. When there is no unused oprator and click the "=" button
   like '2' '1' '=' :
   There is no response for this "=" button, and the state remains.

5. After computing with "="
   (1) If then click the operator, the previous data displayed remains for this calculation.
   Like '2' '+' '1' '=' '+' '3'
   Display 2  2  1   3   3   3

   (2) If then click the digit button, the previous data displayed would be discard. And only current digit is diaplayed and used for this calculation.
   Like   '2' '+' '1' '=' '5' '+' '2' '='
   Display 2   2   1   3   5   5   2   7
